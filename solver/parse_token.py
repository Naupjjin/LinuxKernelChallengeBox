from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from datetime import datetime
import binascii

TOKEN_SECRET_KEY = b"TomorinIsCute123" 

USER_TOKEN = "fd87866654018d4c75b32a02e38d074fc1f23ce2fc4845f0112889626c061b1fdef67fea94d69e72fe5764733f048218000c5aa04ac15054b7555bd43e52df94d9b6d488b40f767bb5f117ce30cfcc"

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
