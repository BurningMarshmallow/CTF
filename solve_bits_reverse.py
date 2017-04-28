def to_bin(value):
    b = bin(value)[2:].rjust(8, "0")
    return [int(x) for x in b][::-1]
    
    
def lshift(arr):
    tmp = arr[0]
    for i in range(1, 8):
        arr[i - 1] = arr[i]
    arr[7] = tmp
    return arr


values = [107, 44, 125, 92, 105, 62, 110, 104]
xor_values = [0x69, 0xE7, 0x56, 0x5E, 0xB9, 0x82, 0x0F, 0x4D]
xor_bin_values = list(map(to_bin, xor_values))

orig_values = [[0] * 8 for i in range(8)]
for i in range(8):
    bin_values = list(map(to_bin, values))
    for j in range(8):
        orig_values[i][j] = xor_bin_values[j][j] ^ bin_values[j][j]
    values = lshift(values)

answer = [[0] * 8 for i in range(8)]

for t in range(8):
    i = t
    j = 0
    for _ in range(8):
        answer[t][j] = xor_bin_values[j][j] ^ bin_values[i][j]
        i -= 1
        i %= 8
        j += 1
        j %= 8

answer = lshift(answer)
for letter in answer:
    print(chr(int("".join([str(x) for x in letter[::-1]]), 2)), end="")
