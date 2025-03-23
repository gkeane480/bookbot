import sys
from stats import count_words, character_count, sort_dictionary

def get_book_text(book_path):
    with open(book_path) as f:
        contents = f.read()
    return contents

def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    book = get_book_text(sys.argv[1])
    sorted_characters = sort_dictionary(character_count(book))

    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {sys.argv[1]}')
    print('----------- Word Count ----------')
    print(f'Found {count_words(book)} total words')
    print(f'--------- Character Count -------')
    for dict in range(len(sorted_characters)):
        character = sorted_characters[dict]['character']
        count = sorted_characters[dict]['count']
        if character.isalpha():
            print(f'{character}: {count}')
    print('============= END ===============')
main()
