import socket
import time
def encode(str):
   codes = []
   for c in str:
     codes.append(hex(ord(c))[::-1])
   return ' '.join(codes)

sock = socket.socket()

sock.connect(("sibears.ru", 10028))
while True:
    s = sock.recv(4096)
    if "flag" in s:
        break
    x = s.split("\n")[1].split(" ")
    rev = [chr(int(c[::-1], 16)) for c in x]
    expression = ''.join(rev)
    value = eval(expression)
    answer = encode(str(value))
    sock.send(answer)
    time.sleep(0.2)
print s

# flag is ~y@y_I_cod3d_!7_^^