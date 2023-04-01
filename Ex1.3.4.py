password = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"

# Shift by 2 all alphabetic chars, ignore edge case of y&z
print("".join(chr(ord(x) + 2) if x.isalpha() else x for x in password))
