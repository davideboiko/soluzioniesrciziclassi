def F1(t, F1):
    r = []
    for c in t:
        if c.isalpha():
            o = ord('A') if c.isupper() else ord('a')
            r.append(chr((ord(c) - o + F1) % 26 + o))
        else:
            r.append(c)
    return ''.join(r)
print(F1("ciao come stai?", 5))

#questo è cesare
