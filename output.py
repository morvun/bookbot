from stats import get_book_text, word_counter, character_counter
import sys

# output.py

# Function to sort character counts by value in descending order

def sort_by_value(character_count):
    return sorted(character_count.items(), key=lambda item: item[1], reverse=True)
    
# Main output function that processes the book text and prints the results

def output(get_book_text, word_counter, character_counter):
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1] 
    book_text = get_book_text(book_path)
    word_count = word_counter(book_text)
    character_count = character_counter(book_text)
    sorted_characters = sort_by_value(character_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("---------- Character Count -------")
    for character, count in sorted_characters:
        print(f"{character}: {count}")
    print("============= END ===============")