def decryption(msg):
    pt = []
    for char in msg:
        char = char - 18
        char = 179 * char % 256
        pt.append(char)
    return bytes(pt).decode("UTF-8")

with open('msg.enc') as f:
    ct = bytes.fromhex(f.read())

print(decryption(ct))
