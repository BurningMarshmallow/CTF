import socket
import glob
import base64
import time
import re

def solve():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('cm2k-magic_b46299df0752c152a8e0c5f0a9e5b8f0.quals.shallweplayaga.me', 12001))
    print("Connected to server")
    num = 0
    while True:
        time.sleep(0.5)
        buffer = s.recv(1024)
        if b"The flag" in buffer:
            break
        name = buffer.split(b"\n")[1 - (num > 0)]
        print(b"Got a name : " + name)
        num += 1
        with open(b"keys\\" + name, 'rb') as f:
            key = f.read()
            s.send(base64.b64encode(key) + b"\n")
    print(buffer)


def crack(crackme):
    print("[+]Cracking: " + crackme)
    with open(crackme, "rb") as infile:
        content = infile.read()
    key = bytes([])
    found = re.findall(b'\x48\x83\xff(.)', content)
    key = b"".join(found)
    return key
    
def crack_crackmes():
    print("Started cracking")
    crackmes = glob.glob("magic_dist/*")
    for crackme in crackmes:
        key = crack(crackme)
        filename = crackme.split("\\")[1] 
        with open("keys/" + filename, "wb") as outfile:
            outfile.write(key)
    print()

crack_crackmes()
solve()