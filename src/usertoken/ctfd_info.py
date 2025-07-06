import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="usertoken/ctfd_info.env")

CTFd_url = os.getenv("CTFD_URL")