def is_probable_duplicate(title_a: str, title_b: str) -> bool:
    return title_a.strip().lower() == title_b.strip().lower()
