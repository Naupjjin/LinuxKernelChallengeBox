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
web
|_ app.py (main)
|_ templates (web front)
|_ static
|_ users
	|_ user_token
		|_ exploit
		|_ result
challenge
|_ run.sh 
|_ cpio 
|_ bzimage
```
