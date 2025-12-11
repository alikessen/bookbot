import sys
from stats import count_words, get_book_text, count_chars_dict, create_report

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]

    text = get_book_text(book_path)
    count_word = count_words(text)
    count_char = count_chars_dict(text)
    sorted_dict = create_report(count_char)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count_word} total words")
    print("--------- Character Count -------")
    for item in sorted_dict:
        ch = item["char"]
        num = item["num"]

        if not ch.isalpha():
            continue

        print(f"{ch}: {num}")
    print("============= END ===============")


main()