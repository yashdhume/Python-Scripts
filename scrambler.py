def encrypt(word, password):
    o = ""
    import string
    s = string.printable
    for x in range(len(word)):
        o += s[s.index(word[x]) ^ s.index(password[x % len(password)])]
    return o


while (True):
    w = input("Enter a word or an encrypted word: ")
    print("'" + encrypt(w, input("Enter encryption password: ")) + "'")
