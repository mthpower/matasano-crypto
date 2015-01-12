def xor_two_hex(hex_1, hex_2):
    """ XOR two hex strings and return a hex string.

    Strips the 0x prefix before returning the hex string.
    """
    int_1 = int(hex_1, 16)
    int_2 = int(hex_2, 16)

    xor = int_1 ^ int_2

    return hex(xor).lstrip('0x')
