import PoW.PoW as PoW_mod
import requests

SECRET_KEY = "TomorinIsCute"
PATH = ""
EXPLOIT_URL = ""

def PoW_handler():

    PREFIX = PoW_mod.generate_prefix()
    ANSWER = input("[!] Your Answer : ")
    PoW_mod.verify_pow(PREFIX, ANSWER, difficulty = 6)

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

PoW_handler()