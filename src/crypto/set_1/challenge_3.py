from collections import Counter
from string import ascii_lowercase


def count_characters(string):
    """ Takes a string, and counts occurences of characters

    Filters the input string:
        - forces lower case
        - removes all non lower case characters

    Returns a dict with keys of letters, and values of occurences
    """
    filtered_string = filter(lambda x: x in ascii_lowercase, string.lower())

    return Counter(filtered_string)


def score_plaintext():
    pass
