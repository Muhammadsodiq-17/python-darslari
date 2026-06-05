mijozlar = {}



def kirish(ism, xona_raqam,xona_turi):
    mijozlar[ism] = {"Xona": xona_raqam ,"Turi": xona_turi}
    return mijozlar


def ochirish(ism):
    if ism in mijozlar:
        mijozlar.pop(ism)
        return f" {ism} Ro'yhaddan o'chirildi "
    else:
        print("Bunday mijoz topilmadi")


while True:
    print("1 Xona buyurtma qilish \n2 Mijozlar ro'yhati\n3 Mijozni  o'chirish")
    n = int(input("Raqam kiriting:"))
    if n == 1:
        print("Xona buyurtma qilish")
        ism = input(" Ismingiz:")
        xona_raqam = int(input("Xona raqami: "))
        print("Xona turini tanlag: \nLuks\nStandart\nEkanom")
        xona_turi=input("Xona turini tanlang:")
        print(kirish(ism, xona_raqam, xona_turi))
        print(f"{ism} qo'shildi")
    elif n == 2:
        print("Mijozlar ro'yhati")
        print(f"{'Mijoz ismi':<15} | {'Xona':<10} | {'Turi':<10}")
        print("-" * 40)

        for ism, malumot in mijozlar.items():
            if isinstance(malumot, dict):
                xona = malumot.get('Xona raqami', '—')
                turi = malumot.get('Turi', '—')
            else:
                xona = malumot
                turi = "Standart"

            print(f"{ism:<15} | {xona:<10} | {turi:<10}")


    elif n == 3:
        ism=input("O'chirmoqchi bo'lgan ismingizni kiriting:")
        print(ochirish(ism))
