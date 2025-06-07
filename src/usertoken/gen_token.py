import time
from datetime import datetime, timezone
import secret.secret as sec_mod
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

def gen_token(ctfd_token):
    
    iso_time = datetime.now(timezone.utc).isoformat()
    plaintext = (ctfd_token + '|' + iso_time).encode()
    
    nonce = os.urandom(12)

    aesgcm = AESGCM(sec_mod.TOKEN_SECRET_KEY)
    ciphertext = aesgcm.encrypt(nonce, plaintext, None)

    TOKEN = (nonce + ciphertext).hex()

    return TOKEN