# LinuxKernelChallengeBox
> Author : naup96321

To Do list
- CTFd token verify
- xinetd
- Dockerfile and docker compose 

```
├── docker-compose.yml
├── Dockerfile
├── README.md
├── solver
│   └── solve_pow.py
└── src
    ├── app.py
    ├── challenge
    │   ├── bzImage
    │   ├── initramfs.cpio.gz
    │   └── run.sh
    ├── CTFuser
    │   └── 4b1e33920656a5d5bf1b81c8344dbd27179f16826a84ed9a77eba79e126f2260ed688b47566c3c511bcb75651c3f55d878d6ec600d168f5faae5d4e3522791a1
    │       └── exploit
    ├── PoW
    │   └── PoW.py
    ├── secret
    │   └── secret.py
    ├── settings.py
    └── usertoken
        ├── gen_token.py
        └── verify_ctfd.py
```