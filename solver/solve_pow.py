import hashlib
import string
import random
import sys

def solve_pow(prefix, difficulty):
    print(f"[+] Solving PoW: SHA256(prefix + answer) starts with {'0' * difficulty}")
    i = 0
    while True:
        answer = str(i)
        digest = hashlib.sha256((prefix + answer).encode()).hexdigest()
        if digest.startswith('0' * difficulty):
            print(f"[+] Found answer: {answer}")
            print(f"[+] Hash: {digest}")
            return answer
        i += 1

prefix = sys.argv[1]
answer = solve_pow(prefix, difficulty=6)