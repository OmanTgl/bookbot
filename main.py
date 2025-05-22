from stats import count_words, count_char, sorted_dict
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    return get_book_text(book_path)

character_count = count_char(main())

print("============ BOOKBOT ============")
print("Analyzing book found at books/frankenstein.txt...")
print("----------- Word Count ----------")
count_words(main())
print("--------- Character Count -------")
sorted_chars = sorted_dict(character_count)
for item in sorted_chars:
    print(f"{item['char']}: {item['num']}")
print("============= END ===============")
