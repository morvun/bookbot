from output import output
from stats import get_book_text, word_counter, character_counter

# main.py

# Main function to run the output process
# This function calls the output function with the necessary parameters
# and serves as the entry point for the script

def main():
    return output(get_book_text, word_counter, character_counter)

main()