import hashlib
import string
import random

def generate_prefix(length=16):
    print("=" * 0x20)
    prefix = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    print(f"[+] Prefix: {prefix}")
    return prefix

def verify_pow(prefix, answer, difficulty):
    digest = hashlib.sha256((prefix + answer).encode()).hexdigest()
    if digest.startswith('0' * difficulty):
        print("[+] Correct PoW!")
        print("=" * 0x20)
    else:
        print("[-] Incorrect PoW.")
        print("=" * 0x20)
        exit(0)        


