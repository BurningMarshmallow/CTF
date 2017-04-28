with open("smtp.task", "rb") as f:
    message = f.read()
    i = 0
    l = len(message)
    decoded = b""
    fixed_header = False
    print(message[:3])
    while i < l:
        if message[i] == ord("="):
            # Quoted decode
            byte = message[i+1:i+3]
            hex_byte = b"0x" + bytes([byte[0], byte[1]])
            if hex_byte != b"0x\r\n":
                s = chr(int(hex_byte, 16))
                decoded += bytes([int(hex_byte, 16)])
            else:
                print(i, hex_byte)
            i += 3
            continue
        elif message[i] == 0xd and message[i + 1] == 0xa:
            if fixed_header:
                decoded += b"\n"
            else:
                fixed_header = True
                decoded += b"\r\n"
            i += 2
        else:
            decoded += bytes(chr(message[i]), "utf-8")
            i += 1

    with open("smtp.png", "wb") as g:
        g.write(decoded)
