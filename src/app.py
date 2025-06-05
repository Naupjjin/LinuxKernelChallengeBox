import PoW.PoW as PoW_mod

SECRET_KEY = "TomorinIsCute"

PREFIX = PoW_mod.generate_prefix()
ANSWER = input("[!] Your Answer : ")
PoW_mod.verify_pow(PREFIX, ANSWER, difficulty = 6)

PATH = ""