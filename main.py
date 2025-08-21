from os import PathLike

from stats import count_words, count_character_occurrences


def get_book_text(path: str | PathLike) -> str:
    with open(path) as file:
        return file.read()


def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = count_words(book_text)
    print(f"{num_words} words found in the document")
    occurrences = count_character_occurrences(book_text)
    print(occurrences)


if __name__ == "__main__":
    main()
