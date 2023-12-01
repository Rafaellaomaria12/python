import caesar

def caesar(s, k, decode = False):
	if decode: k = 26 - k
	return "".join([chr((ord(i) - 65 + k) % 26 + 65)
				for i in s.upper()
				if ord(i) >= 65 and ord(i) <= 90 ])

msg = "A rápida raposa marrom saltou sobre os cachorros preguiçosos"
print(msg)
enc = caesar(msg, 11)
print(enc)
print (caesar(enc, 11, decode = True))