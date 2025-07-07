from usertoken.ctfd_info import CTFd_URL
import re
import json
import requests

def verify_failed(your_input_token):
    print("[x] Token **{}** verify failed".format(your_input_token))
    exit(0)

def verify_ctfd_token(ctfd_token):
    # check your ctfd token format
    if re.fullmatch(r"^ctfd_[0-9a-f]{64}$", ctfd_token) is None:
        verify_failed(ctfd_token)

    # try to request api by your token
    ctfd_url = f"{CTFd_URL.rstrip('/')}/api/v1/users/me"
    
    response = requests.get(
        ctfd_url,
        headers={
            "Authorization": f"Token {ctfd_token}",
            "Content-Type": "application/json",
        },
        timeout=5
    )

    if response.status_code != 200:
        verify_failed(ctfd_token)
    
    # fetch your team id and email from response
    json_data = json.loads(response.text)

    user_id = json_data["data"]["id"]
    user_email = json_data["data"]["email"]

    print("[!] Success to verify your token **{}**!".format(ctfd_token))
    print("=" * 0x20)
    # use id and email generate folder name
    ctfd_token = f"{user_id}|{user_email}"
    return ctfd_token

    
        
        