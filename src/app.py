import PoW.PoW as PoW_mod
import usertoken.gen_token as gentoken_mod
import usertoken.verify_ctfd as verify_ctfd_mod
import requests
import os

BASE_PATH = "CTFuser/"
EXPLOIT_URL = ""


def get_exploit_handler():
    ### Need edit
    EXPLOIT_URL = input("[!] Enter exploit url : ")
    try:
        response = requests.get(EXPLOIT_URL)
        response.raise_for_status()

        with open("exploit.elf", "wb") as f:
            f.write(response.content)
        print("[+] Exploit ELF saved to exploit.elf")

        return "exploit.elf"
    except Exception as e:
        print(f"[-] Failed to download ELF: {e}")
        return None

# PoW

PREFIX = PoW_mod.generate_prefix()
ANSWER = input("[!] Your Answer : ")
PoW_mod.verify_pow(PREFIX, ANSWER, difficulty = 6)

# gen USER token

USER_CTFD_TOKEN = input("[!] Input your CTFd token : ")
verify_ctfd_mod.verify_ctfd_token(USER_CTFD_TOKEN) # This mod need dev

USER_TOKEN = gentoken_mod.gen_token(USER_CTFD_TOKEN)

# create user dir

TARGET_DIR = os.path.join(BASE_PATH, USER_TOKEN)

os.makedirs(TARGET_DIR, exist_ok=True)

