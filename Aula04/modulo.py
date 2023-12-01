import caesar

am = "Deftones"
print (am)
enc = caesar(am,18)
print(caesar(enc, 18, decode = True))
