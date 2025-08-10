# stats.py

# Function to read the book text from a file
# This function takes the path to the book file as an argument
# and returns the contents of the file as a string

def get_book_text(book_path):
    file_contents = ""
    with open(book_path) as book_file:
        file_contents = book_file.read()
        return file_contents

# Function to count words in the book text
# This function splits the text into words and returns the total count  

def word_counter(book_text):
    words = book_text.split()
    return len(words)

# Function to count characters in the book text
# This function counts each character's occurrences in the text
# and returns a dictionary with characters as keys and their counts as values

def character_counter(book_text):
    book_text_lowercase = book_text.lower()
    book_text_characters = {}
    for character in book_text_lowercase:
        if character.isalpha():
            if character in book_text_characters:
                book_text_characters[character] += 1
            else:
                book_text_characters[character] = 1
    return book_text_characters