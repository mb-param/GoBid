def score_relevance(title: str, description: str) -> float:
    """Rule-first placeholder before LLM integration."""
    text = f"{title} {description}".lower()
    keywords = ["software", "ai", "it", "cloud", "data"]
    hits = sum(1 for k in keywords if k in text)
    return min(1.0, 0.5 + hits * 0.1)
