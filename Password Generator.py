import string
low = string.ascii_lowercase
upp = string.ascii_uppercase
punc = string.punctuation
def pswrdgen(lth):
    import random
    passlist = []
    n = 0
    while n < lth:
        choice = random.randint(1,4)
        if choice == 1:
            x = random.choice(seq=[l for l in low])
            passlist.append(x)
        elif choice == 2:
            x = random.choice(seq=[u for u in upp])
            passlist.append(x)
        elif choice == 3:
            x = random.randint(0, 9)
            passlist.append(str(x))
        elif choice == 4:
            x = random.choice(seq=[p for p in punc])
            passlist.append(x)
        #elif choice == 5:
            #x = random.choice(seq=['!', '#', '/', '$', '^', '*', '(', ')', '@', ',', '?', ':', ';', '~', '&', '+', '%', '_'])
            #passlist.append(x)
        n += 1

    password = ''

    for symbol in passlist:
        password += symbol

    return password

length = int(input("Enter the required password length: "))

print("Required " + str(length) + "-character long password: " + pswrdgen(length))