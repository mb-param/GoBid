import re
from dataclasses import dataclass
from urllib.parse import urljoin

import httpx
from bs4 import BeautifulSoup


AFRICA_GATEWAY_URL = "https://www.africagateway.info/"
LINK_PATTERN = re.compile(r"/(tenderdetails|freetenderdetails)")
DEADLINE_PATTERN = re.compile(r"\b\d{1,2}-[A-Za-z]{3}-\d{4}\b")


@dataclass(slots=True)
class RawTender:
    title: str
    source_url: str
    snippet: str
    deadline: str | None = None


def fetch_homepage(timeout_seconds: int = 20) -> str:
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/125.0.0.0 Safari/537.36"
        )
    }
    with httpx.Client(timeout=timeout_seconds, follow_redirects=True, headers=headers) as client:
        response = client.get(AFRICA_GATEWAY_URL)
        response.raise_for_status()
        return response.text


def parse_tender_links(html: str) -> list[RawTender]:
    soup = BeautifulSoup(html, "html.parser")
    raw_items: list[RawTender] = []
    seen: set[str] = set()

    for link in soup.find_all("a", href=True):
        href = str(link["href"]).strip()
        if not LINK_PATTERN.search(href):
            continue

        title = " ".join(link.get_text(" ", strip=True).split())
        if len(title) < 10:
            continue

        absolute_url = urljoin(AFRICA_GATEWAY_URL, href)
        if absolute_url in seen:
            continue
        seen.add(absolute_url)

        context_text = " ".join(link.parent.get_text(" ", strip=True).split())
        deadline_match = DEADLINE_PATTERN.search(context_text)
        raw_items.append(
            RawTender(
                title=title,
                source_url=absolute_url,
                snippet=context_text[:400],
                deadline=deadline_match.group(0) if deadline_match else None,
            )
        )

    return raw_items
