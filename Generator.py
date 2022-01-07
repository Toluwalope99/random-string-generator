print("WELCOME TO THE RANDOM STRING GENERATOR!")


def display():
    print("Enter type of string required: ")
    print("1: Numeric string")
    print("2: Alphanumeric string")
    print("3: Alphabetic string (lowercase)")
    print("4: Alphabetic string (uppercase)")
    print("5: Alphabetic string (both cases)")
    print("6: Strong password")
    return None


display()

CHOICE = input("Enter the type of string you want to generate: ")

length = int(input("Enter the required length of the string: "))

Number = int(input("Enter the number of strings to be generated: "))

import string

low = string.ascii_lowercase
upp = string.ascii_uppercase
punc = string.punctuation

def numgen(lth):
    import random
    passlist = []
    n = 0

    while n < lth:
        x = random.randint(0, 9)
        passlist.append(str(x))
        n += 1

    numstring = ''

    for symbol in passlist:
        numstring += symbol

    return numstring


def alpnumgen(lth):
    import random
    passlist = []
    n = 0

    while n < lth:
        choice = random.randint(1, 3)
        if choice == 1:
            x = random.choice(seq=[lwr for lwr in low])
            passlist.append(x)
        elif choice == 2:
            x = random.choice(seq=[upr for upr in upp])
            passlist.append(x)
        elif choice == 3:
            x = random.randint(0, 9)
            passlist.append(str(x))
        n += 1

    alpnumstring = ''

    for symbol in passlist:
        alpnumstring += symbol

    return alpnumstring


def alplowgen(lth):
    import random
    passlist = []
    n = 0

    while n < lth:
        x = random.choice(seq=[lwr for lwr in low])
        passlist.append(x)
        n += 1

    alplowstring = ''

    for symbol in passlist:
        alplowstring += symbol

    return alplowstring


def alphighgen(lth):
    import random
    passlist = []
    n = 0

    while n < lth:
        x = random.choice(seq=[upr for upr in upp])
        passlist.append(x)
        n += 1

    alphighstring = ''

    for symbol in passlist:
        alphighstring += symbol

    return alphighstring


def alpbothgen(lth):
    import random
    passlist = []
    n = 0

    while n < lth:
        choice = random.randint(1, 2)
        if choice == 1:
            x = random.choice(seq=[lwr for lwr in low])
            passlist.append(x)
        elif choice == 2:
            x = random.choice(seq=[upr for upr in upp])
            passlist.append(x)
        n += 1

    alpbothstring = ''

    for symbol in passlist:
        alpbothstring += symbol

    return alpbothstring


def pswrdgen(lth):
    import random
    passlist = []
    n = 0

    while n < lth:
        choice = random.randint(1, 5)
        if choice == 1:
            x = random.choice(seq=[lwr for lwr in low])
            passlist.append(x)
        elif choice == 2:
            x = random.choice(seq=[upr for upr in upp])
            passlist.append(x)
        elif choice == 3:
            x = random.randint(0, 9)
            passlist.append(str(x))
        elif choice == 4:
            x = random.choice(seq=[puc for puc in punc])
            passlist.append(x)
        elif choice == 5:
            x = random.choice(seq=[puc for puc in punc])
            passlist.append(x)
        n += 1

    password = ''

    for symbol in passlist:
        password += symbol

    return password


allstr = []
if CHOICE == "1":
    while len(allstr) < Number:
        xx = numgen(length)
        if xx not in allstr:
            allstr.append(xx)

if CHOICE == "2":
    while len(allstr) < Number:
        xx = alpnumgen(length)
        if xx not in allstr:
            allstr.append(xx)

if CHOICE == "3":
    while len(allstr) < Number:
        xx = alplowgen(length)
        if xx not in allstr:
            allstr.append(xx)

if CHOICE == "4":
    while len(allstr) < Number:
        xx = alphighgen(length)
        if xx not in allstr:
            allstr.append(xx)

if CHOICE == "5":
    while len(allstr) < Number:
        xx = alpbothgen(length)
        if xx not in allstr:
            allstr.append(xx)

if CHOICE == "6":
    while len(allstr) < Number:
        xx = pswrdgen(length)
        if xx not in allstr:
            allstr.append(xx)


def display2():
    print("OPTIONS:")
    print("1: Return strings with commas only")
    print("2: Return strings in separate lines only")
    print("3: Return strings in separate lines with commas")


display2()
OPTION = input("Enter return option: ")

choiceList = ['NUMERIC STRINGS', 'ALPHANUMERIC STRINGS', 'LOWERCASE STRINGS', 'UPPERCASE STRINGS', 'ALPHABETIC STRINGS',
              'STRONG PASSWORDS']

fv = open('Strings.txt', 'w')

if OPTION == "1":
    fv.write("JOB DONE!" + "\n")
    fv.write("REQUIRED " + str(Number) + " " + choiceList[int(CHOICE) - 1] + " (" + str(length) + "-CHARACTER-LONG)" + " GENERATED!" + "\n")
    fv.write("\n")
    for xix in range(0, (len(allstr) - 1)):
        fv.write(allstr[xix] + ", ")
    fv.write(allstr[len(allstr) - 1] + ".")
    fv.close()

if OPTION == "2":
    fv.write("JOB DONE!" + "\n")
    fv.write("REQUIRED " + str(Number) + " " + choiceList[int(CHOICE) - 1] + " (" + str(length) + "-CHARACTER-LONG)" + " GENERATED!" + "\n")
    fv.write("\n")
    for item in allstr:
        fv.write(item + "\n")
    fv.close()

if OPTION == "3":
    fv.write("JOB DONE!" + "\n")
    fv.write("REQUIRED " + str(Number) + " " + choiceList[int(CHOICE) - 1] + " (" + str(length) + "-CHARACTER-LONG)" + " GENERATED!" + "\n")
    fv.write("\n")
    for xix in range(0, (len(allstr) - 1)):
        fv.write(allstr[xix] + "," + "\n")
    fv.write(allstr[len(allstr) - 1] + ".")
    fv.close()

# print("Required password: " + password)
