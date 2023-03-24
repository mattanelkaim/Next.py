password = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"

print("".join(chr(ord(x) + 2) if x.isalpha() else x for x in password))
