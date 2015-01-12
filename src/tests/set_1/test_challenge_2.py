from crypto.set_1.challenge_2 import xor_two_hex

HEX_1 = '1c0111001f010100061a024b53535009181c'

HEX_2 = '686974207468652062756c6c277320657965'

EXPECTED_XOR = '746865206b696420646f6e277420706c6179'


def test_xor_two_strings():
    result = xor_two_hex(HEX_1, HEX_2)

    assert result == EXPECTED_XOR
    assert isinstance(result, str)
