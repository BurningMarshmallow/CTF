import socket

def isqrt(n):
  x = n
  y = (x + n // x) // 2
  while y < x:
    x = y
    y = (x + n // x) // 2
  return x

def fermat(n, verbose=True):
    a = isqrt(n) # int(ceil(n**0.5))
    b2 = a*a - n
    b = isqrt(n) # int(b2**0.5)
    count = 0
    while b*b != b2:
        if verbose:
            print('Trying: a=%s b2=%s b=%s' % (a, b2, b))
        a = a + 1
        b2 = a*a - n
        b = isqrt(b2) # int(b2**0.5)
        count += 1
    p=a+b
    q=a-b
    assert n == p * q
    print('a=',a)
    print('b=',b)
    print('p=',p)
    print('q=',q)
    print('pq=',p*q)
    return p, q




def egcd(a, b):  
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):  
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def solve():

    d = modinv(e, phi)  
    dec = pow(data, d, n)  
    print(dec)  
    dec = hex(dec)[2:]
    if dec[-1] == 'L':
        print dec
        dec = dec[:-1]
        print dec
    # print dec
    return ''.join([chr(int(dec[2 * i:2 * i + 2], 16)) for i in range(len(dec) // 2)])



s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('188.226.160.200', 33000))

print s.recv(1000)
s.send('D')
while True:    

    t = s.recv(1000)


    print 'INPUT == ', t
    x = t.split(' ')
    n = int(x[7])
    e = int(x[10])
    data = int(x[13][:-1])


    print 'N =', n
    print 'E =', e
    print 'DATA =', data

    p, q = fermat(n)
    print 'P =', p
    print 'Q =', q

    phi = (p - 1) * (q - 1)

    answer = solve()
    s.send(answer)


# n = 64257037776635899541667043599965185691253416897829867850416996949374574940212292869359743909777808675188730064439730989
# data = 56124132343222174097499667153929094919965178413672634958039140899113493431377512643369779077415372673270097283908280966
# e = 65537






