def get_book_text(book_path):
    file_contents = ""
    with open(book_path) as book_file:
        file_contents = book_file.read()
        return file_contents
    
def word_counter(book_text):
    words = book_text.split()
    return len(words)

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