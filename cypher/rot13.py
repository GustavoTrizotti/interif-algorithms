def dencrypt(s: str, n: int = 13) -> str:
    out = ""
    for c in s:
        if "A" <= c <= "Z":
            out += chr(ord("A") + (ord(c) - ord("A") + n) % 26)
        elif "a" <= c <= "z":
            out += chr(ord("a") + (ord(c) - ord("a") + n) % 26)
        else:
            out += c
    return out

# Encryptation
s1 = dencrypt("Texto secreto", 13)
print(s1)

# >>> Grkgb frpergb

# Decryptation
s2 = dencrypt(s1, 13)
print(s2)

# >>> Texto secreto 