import string

s = string.ascii_lowercase # a-z
s += '_'
d = {}
for c in range(len(s)):
	d[s[(c*4 + 15)%27]] = s[c]
ciphertext = 'ifpmluglesecdlqp_rclfrseljpkq'
s1 = ''
for x in cr:
	s1 += d[x]
print s1 # flag_is_every_haxor_love_math
