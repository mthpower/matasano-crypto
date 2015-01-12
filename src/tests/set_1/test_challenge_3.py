from crypto.set_1.challenge_3 import (
    count_characters,
    score_plaintext,
)


def test_score_plaintext():
    score_plaintext()
    pass


def test_count_characters():
    test_string = 'This is a test string with a number ' \
                  'two (2) and some punctuation!'

    expected_count = {
        't': 8,
        's': 5,
        'i': 5,
        'n': 5,
        'a': 4,
        'o': 3,
        'u': 3,
        'e': 3,
        'h': 2,
        'm': 2,
        'r': 2,
        'w': 2,
        'g': 1,
        'c': 1,
        'p': 1,
        'd': 1,
        'b': 1
    }

    result = count_characters(test_string)

    assert result == expected_count

# 'etaoinshrdlcumwfgypbvkjxqz'
