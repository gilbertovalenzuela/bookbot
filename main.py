from stats import get_num_words, get_num_occurrences, get_sorted_occurrences
import sys


def get_book_text(path_to_book):
    with open(path_to_book) as file:
        book_text = file.read()
    return book_text



def main():
    path_to_book = ""
    if len(sys.argv) > 1:
        path_to_book = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


    book_text = get_book_text(path_to_book)
    num_words = get_num_words(book_text)
    occurrences = get_num_occurrences(book_text)
    print(f"Found {num_words} total words")
    print(occurrences)
    sorted_occurrences = get_sorted_occurrences(book_text)
    for occurrence in sorted_occurrences:
        if occurrence['char'].isalpha():
            print(f"{occurrence['char']}: {occurrence['num']}")

if __name__ == "__main__":
    main()