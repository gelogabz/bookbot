import sys
from stats import get_num_words
from stats import get_char_counts
from stats import sort_char_counts


def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    char_counts = get_char_counts(text)
    print("--------- Character Count -------")
    sorted_chars = sort_char_counts(char_counts)
    for item in sorted_chars:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


main()
