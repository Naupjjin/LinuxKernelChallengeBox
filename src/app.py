import PoW.PoW as PoW_mod
import usertoken.gen_token as gentoken_mod
import usertoken.verify_ctfd as verify_ctfd_mod
import requests
import os
import secrets
import string
import subprocess
from urllib.parse import urlparse
from settings import *

def is_valid_url(url):
    parsed = urlparse(url)
    return all([parsed.scheme in ('http', 'https'), parsed.netloc])

BASE_PATH = "CTFuser/"
EXPLOIT_URL = ""

# PoW

if NEED_POW_FUNCTION:
    PREFIX = PoW_mod.generate_prefix()
    ANSWER = input("[!] Your Answer : ")
    PoW_mod.verify_pow(PREFIX, ANSWER, difficulty = 6)

# gen USER token

if NEED_CTFD_TOKEN_FUNCTION:
    USER_CTFD_TOKEN = input("[!] Input your CTFd token : ")
    verify_ctfd_mod.verify_ctfd_token(USER_CTFD_TOKEN) # This mod need dev
else:
    USER_CTFD_TOKEN = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(16))

USER_TOKEN = gentoken_mod.gen_token(USER_CTFD_TOKEN)

# create user dir

TARGET_DIR = os.path.join(BASE_PATH, USER_TOKEN)
os.makedirs(TARGET_DIR, exist_ok=True)

# Get your exploit

print("[!] Start !!!!!")
NEED_UPLOAD_EXPLOIT = input("NEED_UPLOAD_EXPLOIT (y/n)").strip()
if NEED_UPLOAD_EXPLOIT == "y":
    EXPLOIT_URL = input("[!] Input your exploit url : ").strip()
    if not is_valid_url(EXPLOIT_URL):
        print("[X] Invalid URL.")
        exit(1)

    try:
        response = requests.get(EXPLOIT_URL, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"[X] Failed to download file: {e}")
        exit(1)

    output_path = os.path.join(TARGET_DIR, "exploit")
    with open(output_path, "wb") as f:
        f.write(response.content)

    print("[!] Wait ... your challenge will start ...")
    try:
        subprocess.run(["./challenge/run.sh", output_path])
    except Exception as e:
        print(f"[X] {e}")
else:
    try:
        subprocess.run(["./challenge/run.sh"])
    except Exception as e:
        print(f"[X] {e}")
