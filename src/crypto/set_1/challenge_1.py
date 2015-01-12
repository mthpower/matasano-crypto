from base64 import b64encode


def convert_hex_to_base64(hex_string):
    return b64encode(hex_string)
