import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="secret/secret.env")

TOKEN_SECRET_KEY = os.getenv("TOKEN_SECRET_KEY").encode()
CTFd_API_KEY = os.getenv("CTFD_API_KEY")