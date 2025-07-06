#!/bin/bash
echo "[+] Waiting for connections"
source /opt/venv/bin/activate
socat -T 120 tcp-l:13370,reuseaddr,fork EXEC:"python3 /opt/app.py",pty,stderr
echo "[+] Exiting"