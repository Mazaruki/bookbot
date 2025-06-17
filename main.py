from stats import get_word_count
from stats import get_all_character_counts
from stats import sort_alphanumerical
import sys

def get_book_text(book_path):
    """
    Reads the content of a book file and returns it as a string.
    
    Args:
        book_path (str): The path to the book file.
        
    Returns:
        str: The content of the book file.
    """
    with open(book_path, 'r', encoding="utf-8") as file:
        return file.read()
    

    
def main():
    """
    Main function to execute the script.
    """
    """book_path = '/home/mazaruki/bookbot/books/frankenstein.txt'  # Example path, adjust as needed"""
    if not len(sys.argv) == 2: 
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        book_text = "~/" + get_book_text(book_path)
        word_count = get_word_count(book_text)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at: {book_path}")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words.")
        print("--------- Character Count -------")
        for item, value in sort_alphanumerical(get_all_character_counts(book_text)):
            if item[0].isalpha():
                print(f"{item}: {value}")
        print("============= END ===============")

main()