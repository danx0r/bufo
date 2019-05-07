import random

vowels = "aeiouyEO"
consonants = "bcdfgjkmnprstvxz"

def bufo_(bits):
    s = ""
    while bits:
        bittle = bits & 0x0f
        bits >>= 4
        t = consonants[bittle]
        s += t
        bittle = bits & 0x07
        bits >>= 3
        t = vowels[bittle].replace("E", "ee").replace("O", "oo")
        s += t
    return s

def bufo(bits):
    s = ""
    while bits:
        s += bufo_(bits & 0x3fff)
        bits >>= 14
        s += " "
    return s.strip().capitalize()

def rebufo_(b):
    h = 0
    b = b.replace("ee", "E").replace("oo", "O")
    b = list(b)
    b[0] = b[0].lower()
    b.reverse()
    for c in b:
        if c in vowels:
            h <<= 3
            h += vowels.find(c)
        elif c in consonants:
            h <<= 4
            h += consonants.find(c)
        else:
            return "That doesn't look like anything to me"
    return h

def rebufo(b):
    h = 0
    x = b.split()
    x.reverse()
    for w in x:
        h <<= 14
        h += rebufo_(w)
    return h

if __name__=="__main__":
    r = random.randint(0, 2 ** 72)
    print (hex(r))
    b = bufo(r)
    print (b)
    bb = rebufo(b)
#    print (hex(bb))
    print (bb==r)
