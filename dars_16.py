ismlar=["akmal","rano ","nodir"]
parollar=12

while True:
    ism =input("Ismingizni kiriting:")
    parol=int(input("Parolni kiriting:"))

    if ism in ismlar and parol==parollar:
        print("Xush kelibsiz!")
        break
    else:
         print("Xato qayta uriningg!")
