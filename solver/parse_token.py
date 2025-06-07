from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from datetime import datetime
import binascii

TOKEN_SECRET_KEY = b"TomorinIsCute123" 

USER_TOKEN = "4b1e33920656a5d5bf1b81c8344dbd27179f16826a84ed9a77eba79e126f2260ed688b47566c3c511bcb75651c3f55d878d6ec600d168f5faae5d4e3522791a1"  

def parse_token(token_hex):

    token_bytes = bytes.fromhex(token_hex)
    nonce = token_bytes[:12]
    ciphertext = token_bytes[12:]

    aesgcm = AESGCM(TOKEN_SECRET_KEY)
    plaintext = aesgcm.decrypt(nonce, ciphertext, None)

    decoded = plaintext.decode()
    ctfd_token, iso_time = decoded.split("|", 1)

    return ctfd_token, iso_time

ctfd_token, timestamp = parse_token(USER_TOKEN)
print("CTFd Token:", ctfd_token)
print("Time:", timestamp)
