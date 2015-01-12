from crypto.set_1.challenge_1 import convert_hex_to_base64

HEX_STRING = '49276d206b696c6c696e6720' \
             '796f757220627261696e206c' \
             '696b65206120706f69736f6e' \
             '6f7573206d757368726f6f6d'

BASE64_STRING = b'SSdtIGtpbGxpbmcgeW91c' \
                b'iBicmFpbiBsaWtlIGEgcG' \
                b'9pc29ub3VzIG11c2hyb29t'


def test_convert_hex_to_base64():
    assert convert_hex_to_base64(HEX_STRING) == BASE64_STRING
