#!/bin/bash
set -e

if [ ! -f src/secret/secret.env ]; then
    cp src/secret/secret_sample.env src/secret/secret.env
    echo "[prepare.sh] Created src/secret/secret.env from sample."
else
    echo "[prepare.sh] src/secret/secret.env already exists, skip."
fi

if [ ! -f src/usertoken/ctfd_info.env ]; then
    cp src/usertoken/ctfd_info_sample.env src/usertoken/ctfd_info.env
    echo "[prepare.sh] Created src/usertoken/ctfd_info.env from sample."
else
    echo "[prepare.sh] src/usertoken/ctfd_info.env already exists, skip."
fi