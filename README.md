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
    └── PoW
        └── PoW.py
```