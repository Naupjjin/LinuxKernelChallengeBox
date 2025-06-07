# LinuxKernelChallengeBox

- PoW 
- input CTFd token and verify
- gen token = AES(CTFd.random_string, "TomorinIsCute")
- Upload your exploit
- Start your qemu and bind your exploit to qemu
- run qemu and run your exploit
- after some seconds read result and show
- after some seconds kill all process about qemu


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