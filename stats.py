from collections import Counter


def count_words(text: str) -> int:
    words = text.split()
    return len(words)


def count_character_occurrences(text: str) -> dict[str, int]:
    text = text.lower()
    counts = Counter(text)
    return counts
