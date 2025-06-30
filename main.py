from stats import get_num_words
from stats import get_char_counts


def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    char_counts = get_char_counts(text)
    print(char_counts)


main()
