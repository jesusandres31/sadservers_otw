import base64
import json

ciphertext = b"HmYkBwozJw4WNyAAFyB1VUcqOE1JZjUIBis7ABdmbU1GIjEJAyIxTRg="
ciphertext = base64.decodebytes(ciphertext)
plaintext = {"showpassword": "no", "bgcolor": "#ffffff"}
# Here, we remove the space as JSON implementation in Python is different from PHP
plaintext = json.dumps(plaintext).encode("utf-8").replace(b" ", b"")


def xor_decrypt(plaintext, ciphertext):
    secret = ""

    for x in range(len(plaintext)):
        secret += str(chr(ciphertext[x] ^ plaintext[x % len(plaintext)]))

    return secret


secret = xor_decrypt(ciphertext, plaintext)
print(secret)
