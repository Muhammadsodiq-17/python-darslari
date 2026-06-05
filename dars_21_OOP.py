# class foydalanuvchi:
#     def __init__(self ,ism,fammilya,tugilgan_yil,yosh):
#         self.ism=ism
#         self.familya=fammilya
#         self.tugilgan_yil=tugilgan_yil
#         self.yosh=yosh
#     def oqish(self,matn):
#         print(f" {self.ism} salom {matn} yaxshimisiz")
# Yasinaxon=foydalanuvchi(ism="Yasinaxon",fammilya="Farhodova",tugilgan_yil=2025,yosh=1)
# Muhammadsodiq=foydalanuvchi(ism="Muhammadsodiq",fammilya="Farhodov",tugilgan_yil=2006,yosh=20)
# Mashxuraxon=foydalanuvchi(ism="Mashxuraxon", fammilya="O'ktamjonova",tugilgan_yil=2008,yosh=18)
# Muhammadziyo=foydalanuvchi(ism="Muhammadziyo",fammilya="Xidirov",tugilgan_yil=2024,yosh=2)
# Muhammadrizo=foydalanuvchi(ism="Muhammadrizo",fammilya="Xidirov",tugilgan_yil=2021,yosh=5)
# print(Mashxuraxon.ism, Mashxuraxon.familya ,Mashxuraxon.yosh)
# print(Muhammadsodiq.ism, Muhammadsodiq.familya ,Muhammadsodiq.yosh)
# Muhammadsodiq.oqish("Muhammadziyo")
# Muhammadziyo.oqish("Yasinaxon")



#
# class Oson1:
#     a=111111111111111111111111111111111111111
#     def __init__(self ,a):
#         self.a=a
#
#
# print(Oson1.a)
# class Oson1:
#      a=2
#
#      def oson(cls):
#       print(cls.a)
# Oson1.oson(Oson1)


# class Oson2:
#     a = 2
#     b = 56
#
#     def summa(cls):
#         print(cls.a + cls.b)
#
#
# Oson2.summa(Oson2)

#
# class Oson3:
#     a = -1
#
#     def plus_minus(cls):
#         if cls.a >= 0:
#             print("Musbat son ")
#         else:
#             print("Manfiy son ")
#
#
# Oson3.plus_minus(Oson3)

# class Oson4:
#     a = 4
#
#     def add_wen(cls):
#         if cls.a % 2 == 0:
#             print("Juft son")
#         elif cls.a % 2 != 0:
#             print("Toq son")
#
#
# Oson4.add_wen(Oson4)

#
# class Oson5:
#     a = 3
#     b = 2
#
#     def daraja(cls):
#         print(cls.a ** cls.b)
#
#
# Oson5.daraja(Oson5)

##@classmethod--> Dekorator bu qator orqali funksiyalar chaqirilganda qavslar ichiga class nomini yozish shart bo'lmaydi
#
#
# class my_class:
#     word = []
#
#     @classmethod
#     def add_word(cls):
#         cls.word.append("Muhammadsodiq")
#         print(cls.word)
#
#     @classmethod
#     def remowe(cls):
#         cls.word.remove("Muhammadsodiq")
#         print(cls.word)
#
#
# my_class.add_word()
# my_class.remowe()


# class my_class:
#     mydict={}
#     @classmethod
#     def add_elmen(cls,key,val):
#         if cls.mydict[key]!=key:
#            return cls.mydict.update(key,val)
#         else:
#             return key
#     @classmethod
#     def update(cls, key,val):
#         if cls.mydict[key]==key:
#             return cls.mydict.update(key, val)
#         else :
#             return  key
# my_class.add_elmen(key=1,val="Muhammadsodiq")
# my_class.update(key=3, val="Muhammadsodiq")

#
#
# class mashina:
#
#     def __init__(self,modeli,yili,nomi,yurgan_masofasi):
#          self.modeli=modeli
#          self.yili=yili
#          self.nomi=nomi
#          self.yurgan_masofasi=yurgan_masofasi
#     def sotuv_bolimi(cls,mant):
#         print(f"Mashina  haqidagi malumotlar {mant}")
# Malibu=mashina(modeli="Sedan",yili=2020,nomi="Malibu",yurgan_masofasi=1000)
# Malibu = mashina(modeli="Sedan", yili=2020, nomi="Malibu", yurgan_masofasi=1000)
# Gentra = mashina(modeli="Sedan", yili=2022, nomi="Gentra", yurgan_masofasi=5000)
# Cobalt = mashina(modeli="Sedan", yili=2023, nomi="Cobalt", yurgan_masofasi=1200)
# Tracker = mashina(modeli="Krossover", yili=2021, nomi="Tracker", yurgan_masofasi=15000)
# Onix = mashina(modeli="Sedan", yili=2023, nomi="Onix", yurgan_masofasi=500)
# Tahoe = mashina(modeli="Yo'ltanlamas", yili=2022, nomi="Tahoe", yurgan_masofasi=8000)
# Equinox = mashina(modeli="Krossover", yili=2021, nomi="Equinox", yurgan_masofasi=12000)
# Tesla = mashina(modeli="Elektromobil", yili=2023, nomi="Tesla Model S", yurgan_masofasi=2000)
# BMW = mashina(modeli="Sportkar", yili=2022, nomi="BMW M5", yurgan_masofasi=3000)
# Mercedes = mashina(modeli="Lyuks", yili=2023, nomi="Mercedes S-Class", yurgan_masofasi=1000)
# Toyota = mashina(modeli="Sedan", yili=2021, nomi="Toyota Camry", yurgan_masofasi=20000)
# Hyundai = mashina(modeli="Sedan", yili=2022, nomi="Hyundai Elantra", yurgan_masofasi=11000)
# Kia = mashina(modeli="Sedan", yili=2021, nomi="Kia K5", yurgan_masofasi=14000)
# Audi = mashina(modeli="Sportkar", yili=2023, nomi="Audi RS7", yurgan_masofasi=5000)
# Porsche = mashina(modeli="Sportkar", yili=2022, nomi="Porsche 911", yurgan_masofasi=2500)
# RangeRover = mashina(modeli="Yo'ltanlamas", yili=2023, nomi="Range Rover", yurgan_masofasi=3500)
# Lexus = mashina(modeli="Yo'ltanlamas", yili=2020, nomi="Lexus LX570", yurgan_masofasi=45000)
# Nissan = mashina(modeli="Sportkar", yili=2019, nomi="Nissan GT-R", yurgan_masofasi=22000)
# Ford = mashina(modeli="Kupe", yili=2021, nomi="Ford Mustang", yurgan_masofasi=9000)
# Ferrari = mashina(modeli="Superkar", yili=2023, nomi="Ferrari SF90", yurgan_masofasi=100)
# # mashina.sotuv_bolimi("Yangi Modellari keldi")
# print(f"Nomi:{Malibu.nomi}\nModeli:{Malibu.modeli}\nYili:{Malibu.yili}\nYurgan masofasi:{Malibu.yurgan_masofasi}km\n")
# print(f"Nomi:{Malibu.nomi}\nModeli:{Malibu.modeli}\nYili:{Malibu.yili}\nYurgan masofasi:{Malibu.yurgan_masofasi}km\n")
# print(f"Nomi:{Gentra.nomi}\nModeli:{Gentra.modeli}\nYili:{Gentra.yili}\nYurgan masofasi:{Gentra.yurgan_masofasi}km\n")
# print(f"Nomi:{Cobalt.nomi}\nModeli:{Cobalt.modeli}\nYili:{Cobalt.yili}\nYurgan masofasi:{Cobalt.yurgan_masofasi}km\n")
# print(f"Nomi:{Tracker.nomi}\nModeli:{Tracker.modeli}\nYili:{Tracker.yili}\nYurgan masofasi:{Tracker.yurgan_masofasi}km\n")
# print(f"Nomi:{Onix.nomi}\nModeli:{Onix.modeli}\nYili:{Onix.yili}\nYurgan masofasi:{Onix.yurgan_masofasi}km\n")
# print(f"Nomi:{Tahoe.nomi}\nModeli:{Tahoe.modeli}\nYili:{Tahoe.yili}\nYurgan masofasi:{Tahoe.yurgan_masofasi}km\n")
# print(f"Nomi:{Equinox.nomi}\nModeli:{Equinox.modeli}\nYili:{Equinox.yili}\nYurgan masofasi:{Equinox.yurgan_masofasi}km\n")
# print(f"Nomi:{Tesla.nomi}\nModeli:{Tesla.modeli}\nYili:{Tesla.yili}\nYurgan masofasi:{Tesla.yurgan_masofasi}km\n")
# print(f"Nomi:{BMW.nomi}\nModeli:{BMW.modeli}\nYili:{BMW.yili}\nYurgan masofasi:{BMW.yurgan_masofasi}km\n")
# print(f"Nomi:{Mercedes.nomi}\nModeli:{Mercedes.modeli}\nYili:{Mercedes.yili}\nYurgan masofasi:{Mercedes.yurgan_masofasi}km\n")
# print(f"Nomi:{Toyota.nomi}\nModeli:{Toyota.modeli}\nYili:{Toyota.yili}\nYurgan masofasi:{Toyota.yurgan_masofasi}km\n")
# print(f"Nomi:{Hyundai.nomi}\nModeli:{Hyundai.modeli}\nYili:{Hyundai.yili}\nYurgan masofasi:{Hyundai.yurgan_masofasi}km\n")
# print(f"Nomi:{Kia.nomi}\nModeli:{Kia.modeli}\nYili:{Kia.yili}\nYurgan masofasi:{Kia.yurgan_masofasi}km\n")
# print(f"Nomi:{Audi.nomi}\nModeli:{Audi.modeli}\nYili:{Audi.yili}\nYurgan masofasi:{Audi.yurgan_masofasi}km\n")
# print(f"Nomi:{Porsche.nomi}\nModeli:{Porsche.modeli}\nYili:{Porsche.yili}\nYurgan masofasi:{Porsche.yurgan_masofasi}km\n")
# print(f"Nomi:{RangeRover.nomi}\nModeli:{RangeRover.modeli}\nYili:{RangeRover.yili}\nYurgan masofasi:{RangeRover.yurgan_masofasi}\nkm")
# print(f"Nomi:{Lexus.nomi}\nModeli:{Lexus.modeli}\nYili:{Lexus.yili}\nYurgan masofasi:{Lexus.yurgan_masofasi}km\n")
# print(f"Nomi:{Nissan.nomi}\nModeli:{Nissan.modeli}\nYili:{Nissan.yili}\nYurgan masofasi:{Nissan.yurgan_masofasi}km\n")
# print(f"Nomi:{Ford.nomi}\nModeli:{Ford.modeli}\nYili:{Ford.yili}\nYurgan masofasi:{Ford.yurgan_masofasi}km\n")
# print(f"Nomi:{Ferrari.nomi}\nModeli:{Ferrari.modeli}\nYili:{Ferrari.yili}\nYurgan masofasi:{Ferrari.yurgan_masofasi}km\n")













class Hayvon:
    def __init__(self, nomi, turi ):
        self.nomi=nomi
        self.turi=turi
    def mushuk(self, ovozi):
        self.ovozi=ovozi
        print(f" {ovozi} ")
print(

)