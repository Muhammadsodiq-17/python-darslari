
# mevalar= ["olma","banan","nok"]
# mevalar.append("shaftoli") #append->listning elementlari ohiriga yana bitta element qo'shib beradi
# print(mevalar)

#sonlar=[1,2,2,3,4,5,6453,4,5,6,7,8,6]
# sonlar.clear() # clear->listning barcha elementlarini o'chirib yuboradi
# print(sonlar)

# mevalar=["olcha","anor","olma","qulupnay"]
# x=mevalar.copy() # copy->listning elementlaridan nusxa oladi
# print(x)

# sonlar=[1,2,3,4,5,6,7,7,8,8,99,2,2,]
# x=sonlar.count(7) # count->list elementlarini necha marta qatnashganini sanaydi
# print(x)

# mevalar=["olma","anjir","o'rik","shaftoli"]
# mashinalar=["BMW","Tayotta","Ferrari"]
# mevalar.extend(mashinalar) # extend->Ikta list elementlarini bir biriga qo'shib qo'yadi
# print(mevalar)

# mevalar=["olcha","anor","olma","qulupnay"]
# x=mevalar.index("anor") # index->listning elementlarini indeksini aniqlaydi
# print(x)

# mevalar=["olma","shaftoli","banan"]
# mevalar.insert(4,"olxori") # insert->listning istalgan joyiga yangi elmentni qo'shadi
# print(mevalar)

# mevalar=["olcha","anor","olma","qulupnay","anjir","o'rik","shaftoli"]
# mevalar.pop(3)  #pop-> Qavsning ichiga qanday son yosak o'sha indeksdagi sonni listning elementlari qatoridan olib tashlaydi
# print(mevalar)

# mevalar = ['olma', 'banan', 'anjir']
# mevalar.remove("banan") # remove->listning tanlangan elementlarini o'chiradi
# print(mevalar)

# mevalar = ['olma ', 'banan', 'olcha']
# mevalar.reverse() # reverse->listning elementlarini o'rnini almashtiradi oxiridan boshiga qarab yozib qo'yadi
# print(mevalar)

# mashinalar= ['Ford', 'BMW', 'Volvo','chevrolet','kia']
# mashinalar.sort() # sort-> list elementlarini tartiblaydi
# print(mashinalar)


import math

a = float(input("a sonni kirit:"))
b = float(input("b sonni kirit:"))
c = float(input("c sonni kirit:"))
D = b ** 2 - 4 * a * c
if D > 0:
    x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / ( 2 * a)
    print(f"Kvadrat tenglamaning ikkita ildizi bor x1={x1}, x2={x2}")
elif D == 0:
    x = (-b / (2 * a))
    print(f"kvadrat tenglamani bitta yechimi bor x1={x}")
else:
    print("Kvadrat tenglama musbat yechimga ega emas")
