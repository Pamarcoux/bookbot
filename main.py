from stats import *
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return(contents)


def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    contents = get_book_text(sys.argv[1])
    num_words = count_words(contents)
    characters = count_character(contents)
    list_char =sort_character(characters) 
    print("========= BOOKBOT ==========")
    print(f"Analyzing book found at ")
    print(" --------- Word Count ---------- ")
    print(f"Found {num_words} total words")
    print(" --------- Character Count ---------")
    for character in list_char:
        if character["char"].isalpha():
            print(f"{character['char']}: {character['num']}")
main()
