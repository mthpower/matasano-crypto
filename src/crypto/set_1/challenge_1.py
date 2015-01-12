from base64 import b64encode


def convert_hex_to_base64(hex_string):
    """ Given a hex string, return the base64 encoded bytes. """
    decoded_hex = bytes.fromhex(hex_string)
    return b64encode(decoded_hex)
