from hashlib import md5


def get_seed(login):
    modulo_bytes = [0xFB, 0x0F1, 0x0EF, 0x0E9, 0x53, 0x25, 0x17, 0x0D, 0x0B, 7]
    login_length = len(login)
    modulo = modulo_bytes[login_length - 1]
    seed = 0
    reversed_login = login[::-1]
    tmp_value = 0
    for c in reversed_login:
        seed *= modulo
        seed += (ord(c) - 48) % modulo
    return seed


def rand(seed):
    new_seed = seed * 0x343fd+0x269EC3
    return new_seed, (new_seed >> 0x10) & 0x7FFF


def crack_login(login):
    password = ""
    seed = get_seed(login)
    for i in range(10):
        seed, rand_value = rand(seed)
        password += str(rand_value % 10)
    return password

concatenated_passwords = ""
with open("logins.txt") as f:
    logins = f.read().split()
    for login in logins:
        concatenated_passwords += crack_login(login)
print(md5(concatenated_passwords.encode()).hexdigest())
