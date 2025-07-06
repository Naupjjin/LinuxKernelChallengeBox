import secret.secret as sec_mod
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

def gen_token(ctfd_token):

    plaintext = (ctfd_token).encode()
    
    nonce = os.urandom(12)

    aesgcm = AESGCM(sec_mod.TOKEN_SECRET_KEY)
    ciphertext = aesgcm.encrypt(nonce, plaintext, None)

    TOKEN = (nonce + ciphertext).hex()

    return TOKEN