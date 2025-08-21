from os import PathLike

from stats import count_words, count_character_occurrences, sort_occurrences


def get_book_text(path: str | PathLike) -> str:
    with open(path) as file:
        return file.read()


def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    occurrences = count_character_occurrences(book_text)
    sorted_occurrences = sort_occurrences(occurrences)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for d in sorted_occurrences:
        if d['char'].isalpha():
            print(f"{d['char']}: {d['num']}")
    print("============= END ===============")


if __name__ == "__main__":
    main()
