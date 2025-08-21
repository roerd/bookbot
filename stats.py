from collections import Counter


def count_words(text: str) -> int:
    words = text.split()
    return len(words)


def count_character_occurrences(text: str) -> dict[str, int]:
    text = text.lower()
    counts = Counter(text)
    return counts


def get_num(d: dict) -> int:
    return d["num"]


def sort_occurrences(occurrences: dict[str, int]) -> list[dict[str, str | int]]:
    occurrences_list = [{"char": c, "num": n} for c, n in occurrences.items()]
    occurrences_list.sort(key=get_num, reverse=True)
    return occurrences_list
