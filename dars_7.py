# 1.txt="salom dunyo"
# x=txt.center(12,'/') # center-> Matnni markazga joylashtiradi
# print(x)
# 2.txt = "hello, and welcome to my world."
# x = txt.capitalize() # capitalize->Birinchi harfni katta harfga o‘zgartiradi
# print (x)
# 3.txt = " salom talabalar ."
# x = txt.casefold() # casefold-> Barcha harflarni kichik harflarga o‘zgartiradi
# print (x)
# 4.txt = "Dunyoda eng kopistemolqilinadi meva bu olma"
# x = txt.count("olma") # count-> Belgilangan qiymat necha marta uchrashganini qaytaradi
# print(x)
# 5.txt = "salom mening ismim:Muhammadsodiq"
# x = txt.encode() # encode-> Matnni kodlangan  versiyasini qaytaradi
# print(x)
# 6.txt = "Dunyodagi eng kichkina qush bu kalibri."
# x = txt.endswith(".") # endswith-> Matn belgilangan qiymat bilan tugasa True qaytaradi
# print(x)
# 7.txt = "s\ta\tl\to\tm  "
# x = txt.expandtabs(8) # expendtabs->Matndagi tab belgilari (\t)ni belgilangan o‘lchamdagi bo‘sh joy bilan almashtiradi
# print(x)
# 8.txt = " Dasturlash metodlari string list ..."
# x=txt.find("list")
# print(x)
# 9.txt = " Dasturlash metodlari string list ..."
# x=txt.index("list") # index->find() kabi ishlaydi, ammo topilmasa xatolik chiqaradi
# print(x)
# 10.txt = "Farg'ona viloyati  "
# x=txt.isupper()	# isupper-> Barcha harflar katta bo‘lsa, True
# print(x)
# 11.txt ="	Barcha harflar kichik bo‘lsa, True"
# x=txt.islower()
# print(x)
# 11.txt ="123345678987654321234567"
# x=txt.isdigit()# #isdigit->Faqat raqamlardan iborat bo‘lsa, True
# print(x)
# 12.txt= "123456765"
# x=txt.isalnum() #isalnum->Matndagi barcha belgilar harf yoki raqam bo‘lsa, True qaytaradi
# print(x)
# 13.txt= "12345"
# x=txt.join(txt)# join->Takrorlanuvchi elementlarni birlashtirib, bitta matn yaratadi
# print(x)
# 14.txt= "python"
# x=txt.ljust(10) #ljust->Matnni chapga tekislab, o‘ng tomonni bo‘sh joylar bilan to‘ldiradi
# print(x)
# 15.txt = "banana"
# x = txt.rjust(20) # rjust->Matnni o‘ngga tekislaydi va chap tomonni to‘ldiradi
# print(x)
# 16.txt= "OLMA"
# x=txt.lower() #lower->Barcha harflarni kichik harfga o‘zgartiradi
# print(x)
#   17.txt= "mening ismim muhammadsodiq men farg'ona viloyatida tugilganman"
# x=txt.title() # title->Har bir so‘zning birinchi harfini katta qiladi
# print(x)
# 18.txt= "O'zbekiston"
# x=txt.upper()    # upper->Barcha harflarni katta harfga o‘zgartiradi
# print(x)
# 19.txt= "uzum"
# x=txt.split() # split->Belgilangan ajratuvchi bo‘yicha matnni bo‘ladi
# print(x)
# 20.txt= "OLMA"
#  x=txt.lstrip() # lstrip->Chap tomondan bo‘sh joylarni olib tashlaydi
#  print(x)
# 21.txt = "  salom  "
# x=txt.strip()#  strip -> Ikkala tomondagi bo‘sh joylarni olib tashlaydi
# print(x)
# 22.txt = "Salom DUNYO"
# x=txt.swapcase()  # swapcase -> Katta harflarni kichik, kichik harflarni katta qiladi
# print(x)
# 23.txt = "42"
# x=txt.zfill(5) # zfill -> Matnni 0 raqamlari bilan to‘ldiradi
# print(x)
# 24.txt= "salom"
# x=txt.replace("s", "S")    # replace->Belgini boshqasi bilan almashtiradi
# print(x)
# 25.txt= "salom dunyo salom"
# x=txt.rfind("salom")    # rfind->Belgining oxirgi uchrashgan joyini topadi
# print(x)
# 26.txt= " kvadrat hamma tomoni bir biriga teng bo'lgan tortburchak"
# x=txt.rindex("kvadrat")    # rindex->rfind() kabi, lekin topilmasa xatolik chiqaradi
# print(x)
# 27.txt= "salom dunyo hayr"
# x=txt.rpartition(" ")    # rpartition->Oxirgi uchragan ajratuvchi bo‘yicha 3 qismga ajratadi
# print(x)
# 28.txt= "olma,banan,nok"
# x=txt.rsplit(",", 1)    # rsplit->Matnni o‘ngdan chapga qarab ajratadi
# print(x)
# 29.txt= "Salom\nDunyo"
# x=txt.splitlines()    # splitlines->Matnni satr bo‘yicha bo‘ladi
# print(x)
# 30.txt= "Salom DUNYO"
# x=txt.swapcase()    # swapcase->Katta harflarni kichik, kichik harflarni katta qiladi
# print(x)
# 31.txt= "salom 23456"
# x=txt.isascii()    # isascii->Faqat ASCII belgilardan iborat bo‘lsa, True
# print(x)
# 32.txt= "12345"
# x=txt.isdecimal()    # isdecimal->Faqat o‘nlik raqamlardan iborat bo‘lsa, True
# print(x)
# 33.txt= "salom dunyo"
# x=txt.isidentifier()    # isidentifier->Python identifikatori sifatida yaroqli bo‘lsa, True
# print(x)
# 34.txt= "23456"
# x=txt.isnumeric()    # isnumeric->Faqat sonlardan iborat bo‘lsa, True
# print(x)
txt="Dasturlash tillari"
x=txt.isprintable()    # isprintable->Barcha belgilar chop etilishi mumkin bo‘lsa, True
print(x)
