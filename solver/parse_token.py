from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from datetime import datetime
import binascii

TOKEN_SECRET_KEY = b"TomorinIsCute123" 

USER_TOKEN = "9aab97dca69a377a0c208cb88efeb1db138a5cdeb9695c0cdfe810d6e7df00e5ca070c45437f566b1e1bf3a4f3eb"

def parse_token(token_hex):

    token_bytes = bytes.fromhex(token_hex)
    nonce = token_bytes[:12]
    ciphertext = token_bytes[12:]

    aesgcm = AESGCM(TOKEN_SECRET_KEY)
    plaintext = aesgcm.decrypt(nonce, ciphertext, None)

    p = plaintext.decode()

    return p

ctfd_token = parse_token(USER_TOKEN)
print("CTFd Token:", ctfd_token)
