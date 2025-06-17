def get_word_count(text):
    """
    Counts the number of words in a given text.
    
    Args:
        text (str): The text to count words in.
        
    Returns:
        int: The number of words in the text.
    """
    return len(text.split())

def get_all_character_counts(text):
    """
    Counts the occurrences of each character in a given text.
    
    Args:
        text (str): The text to count characters in.
        
    Returns:
        dict: A dictionary with characters as keys and their counts as values.
    """
    char_count = {}
    for char in text:
        if char.lower() not in char_count:
            char_count[char.lower()] = 0
        char_count[char.lower()] += 1
    return char_count

def sort_alphanumerical(dictionary):
    """
    Sorts a dictionary by its keys in alphanumerical order.
    
    Args:
        dictionary (dict): The dictionary to sort.
        
    Returns:
        dict: A new dictionary sorted by keys.
    """
    sorted_list = sorted(dictionary.items(), key =lambda x: -x[1])
    return sorted_list