#!/bin/sh
TIMEOUT=40

CHALLENGE_DIR="$(dirname "$(readlink -f "$0")")"

if [ -z "$1" ]
then
    echo "No exploit supplied"
    # No exploit executable supplied
    timeout 180 qemu-system-x86_64 \
        -kernel "$CHALLENGE_DIR/bzImage" \
        -initrd "$CHALLENGE_DIR/initramfs.cpio" \
        -cpu qemu64,+smap,+smep \
        -smp 1 \
        -m 256M \
        -append "console=ttyS0 quiet loglevel=3 oops=panic panic_on_warn=1 panic=-1 pti=on nokaslr" \
        -no-reboot \
        -nographic \
        -monitor /dev/null 
else
    echo "Exploit supplied"
    # Exploit executable supplied as first argument
    timeout 180 qemu-system-x86_64 \
        -kernel "$CHALLENGE_DIR/bzImage" \
        -initrd "$CHALLENGE_DIR/initramfs.cpio" \
        -cpu qemu64,+smap,+smep \
        -smp 1 \
        -m 256M \
        -append "console=ttyS0 quiet loglevel=3 oops=panic panic_on_warn=1 panic=-1 pti=on nokaslr" \
        -no-reboot \
        -nographic \
        -monitor /dev/null \
        -drive file=$1,format=raw,index=0,media=disk
fi
