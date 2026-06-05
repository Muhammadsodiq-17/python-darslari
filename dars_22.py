class student:
    def name(self):
        print("Student name")
st=student()
# st.name()



#
#
# class sonlar:
#     count=0
#     def __init__(self):
#         sonlar.count=sonlar.count+1
# son=sonlar()
# son1=sonlar()
# son2=sonlar()
# son3=sonlar()
# son4=sonlar()
# print( "sanoq",sonlar.count)






class Odam:
    qollari=2
    oyoqlari=2
class jangchi(Odam):
    energiyasi=100
    jang_energiyasi=30
    def jang_qil(self):
     if self.energiyasi>=self.jang_energiyasi:
         self.energiyasi-=self.jang_energiyasi
         print(f"Energiya {self.energiyasi} Jangda {self.jang_energiyasi} energiya yo'qotildi")
     else:
         print("Jang qilish uchun energiya yetarli emas")
Ali=jangchi()
# Ali.jang_qil()
# Ali.jang_qil()
# Ali.jang_qil()
# Ali.jang_qil()

class shifokor(Odam):
    dorilar=["Trimol", "suv"]
    def davola(self):
        if len(self.dorilar)>0:
            dori=self.dorilar.pop()
            print(f"{dori}  orqali davolandi")
        else:
            print("Dori tugadi!")
Doniyor=shifokor()
# Doniyor.davola()
# Doniyor.davola()
# Doniyor.davola()

# #1
# "Texnika"parent klass.Konstruktorida esa(brand, model, type) parametrlari bor.
# info() - (brand, model, type) ni print qilib beradi.
#
#

class Texnika:
    def __init__(self,brand,model,type):
        self.brand=brand
        self.model=model
        self.type=type
    def info(self):
        print(f"Brend {self.brand}\nModel {self.model}\nTuri {self.type}")




Traxtor=Texnika("Case",model="Magnum 340" ,type="Agro texnika  ")
Bmw=Texnika(brand="BMW",model="BMW X5M Competition",type="Yengil avtomobil")
# Texnika.info(Bmw)



# "Notebooks" child klassi bor. Unda konstruktirida qo'shimcha (video_card, ram, display).
#     more_info() - (brand, model, type, video_card, ram, display) ni print qilib beradi.

class Texnika:
    def __init__(self, brand,model,type ):
        self.brand=brand
        self.model=model
        self.type=type
class Notebooks(Texnika):
    def __init__(self,brand, model,type,video_card, ram,displey ):
        super().__init__(brand,model,type)
        self.video_card=video_card
        self.ram=ram
        self.displey=displey
    def more_info(self):
        print(f"Brendi:{self.brand}\nModeli:{self.model}\nTuri:{self.type}\nVidio karta:{self.video_card}\nRam:{self.ram}\nDispley:{self.displey}")


Hp=Notebooks(brand="HP",model="corei5", type="IT",   video_card="Rtx",ram="8G",displey="NV156FHM-N48")
# # Notebooks.more_info(Hp)


# Hp.more_info()
# "Televisions" child klassi bor. Unda konstruktirida (size, display) parametrlari bor.
#     more_info() - (brand, model, type, size, display) ni print qilib beradi.
class Texnika:
    def __init__(self,brand,model,type,size):
        self.brand=brand
        self.model=model
        self.type=type
        self.size=size
    def info(self):
        print(f"Brend {self.brand}\nModel {self.model}\nTuri {self.type}")
class Televisions(Texnika):
    def __init__(self,displey,brand,model,type,size):
        super().__init__(brand,model,type,size)
        self.displey=displey
        self.brand=brand
        self.model=model
        self.type=type
        self.size=size
    def more_info(self):
        print(f"{self.displey}\n{self.brand}\n{self.model}\n{self.type}\n{self.size}")
BMW=Televisions( displey=23, brand="BMW",model="X5", type="M",size=23,)
# BMW.more_info()


# "Smartphones"child klassi bor.Unda konstruktirida(size, sim_count) parametrlari
# bor. more_info() - (brand, model, type, size, sim_count) ni print qilib beradi.

class Phones():
    def __init__(self,brand,model,type,size):
        self.brand=brand
        self.model=model
        self.type=type
        self.size=size
class Smarthones(Phones):
    def __init__(self,brand,model,type,size,sim_count):
        super().__init__(brand,model,type,size)
        self.brand=brand
        self.model=model
        self.type=type
        self.size=size
        self.sim_count=sim_count
    def more_info(self):
        print(f"{self.brand}\n {self.model}\n {self.type}\n {self.size}\n{self.sim_count}")
Samsung=Smarthones(brand="Samsung",model="S26",type="S",size="26",sim_count=2)
# Samsung.more_info()
##2
# "Transport" parent klass. Konstruktorida esa (brand, model, type) parametrlari bor.
#     info() - (brand, model, type) ni print qilib beradi.


class Transport:
    def __init__(self,brand,model,type):
        self.brand=brand
        self.model=model
        self.type=type

    def info(self):
        return f"{self.brand}\n{self.model}\n{self.type}"
Malibu=Transport(brand="Chevrolet",model="Malibu",type="Sedan")
# Malibu.info()

# "ElentroCars" - child klassi bor. Unda konstruktirida qo'shimcha (battery_life, chargin_time).
#     more_info() - (brand, model, type, battery_life, chargin_time) ni print qilib beradi.


class ElectronCars(Transport):
    def __init__(self,brand,model,type,battary_life,chargin_time):
        super().__init__(brand,model,type)
        self.battary_life=battary_life
        self.chargin_time=chargin_time
    def more_info(self):
        print(f"{self.info()}\n{self.battary_life}\n{self.chargin_time}")
L9=ElectronCars(brand="Li",
                model="L9",
                type="Yo'ltanlamas",
                battary_life="52.3 kVt/soat" ,
                chargin_time="To'liq quvvatlanish uchun taxminan 6.5 — 8 soat"
                )
# L9.more_info()

#
# "SportCars" - child klassi bor.Unda konstruktirida qo'shimcha (motor, color).
# more_info() - (brand, model, type, motor, color)) ni print qilib beradi.


class SportCars(Transport):
    def __init__(self, brand, model, type, motor, color):
        super().__init__(brand, model, type)
        self.motor = motor
        self.color = color

    def more_info(self):
        print(f"{self.info()}\n{self.motor}\n{self.color}")


Bugatti_chiron = SportCars(brand="Bugatti", model="Chiron", type="Sport kar", motor="8 l W16 ", color="Qora")
# Bugatti_chiron.more_info()


# "Truck" - child klassi bor.Unda konstruktirida qo'shimcha (motor, height, long, wieght).
# more_info() - (brand, model, type, height, long, wieght)ni print qilib beradi.

class Truck(Transport):
    def __init__(self, brand, model, type, motor, height, long, wieght):
        super().__init__(brand, model, type)
        self.motor = motor
        self.height = height
        self.long = long
        self.wieght = wieght

    def more_info(self):
        print(f"{self.info()}\n{self.motor}\n{self.height}\n{self.long}\n{self.wieght}")


Volvo = Truck(brand="Volvo Trucks", model="FH16 750 ot kuchi", type="Heavy-Duty Truck", motor="Volvo D16K Dvigateli",
              height="3,400 mm – 3,900 mm ",
              long="5,890 mm – 6,900 mm", wieght="9,500 kg – 10,500 kg")
# Volvo.more_info()




# "University" - parent klass.Konstruktorida esa(university) parametrlari bor.
# info() - (university) ni print qilib beradi

class University:
    def __init__(self, university):
        self.university = university

    def info(self):
        return f"Universitet nomi:{self.university}"


Unversitet = University(university="Fargo'ona davlat texnika unversiteti")

# print(Talaba.info())






# "Staff" - child klass .Unda konstruktorida qo'shimcha(first_name, last_name,age) parametri bor
# staff_info() - (university, first_name, last_name, age) ni print qilib bersin




class Staff(University):
    def __init__(self, university, first_name, last_name, age):
        super().__init__(university)
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def staff_info(self):
        print(f"{self.info()}\n{self.first_name}\n{self.last_name}\n{self.age} yosh")


Talaba = Staff(university="Farg'ona davlat texnika unversiteti", first_name="Qudrat", last_name="Aliyev", age=20)
# Talaba.staff_info()

#






# "Student" - child klass.U "Staff" dan vorislik oladi.Unda konstruktirida qo'shimcha (group) parametrlari bor.
# more_info() - (university, first_name, last_name, age, group) ni print qilib beradi.




class Student(Staff):
    def __init__(self, university, first_name, last_name, age, group):
        super().__init__(university, first_name, last_name, age)
        self.group = group

    def more_info(self):
        return f"{self.staff_info()}\n{self.group}"


student = Student(university=" Farg'ona davlat texnika unversiteti", first_name="Muhammadsodiq", last_name="Farhodov",
                  age=20, group="653-24")
# student.more_info()






# "Teacher" - child klass.U "Staff" dan vorislik oladi.Unda konstruktirida qo'shimcha (position, subject) parametrlari bor.
# more_info() - () ni print qilib beradi.




class Teacher(Staff):
    def __init__(self, university, first_name, last_name, age, position, subject):
        super().__init__(university, first_name, last_name, age)
        self.position = position
        self.subject = subject

    def more_info(self):
        return f"{self.staff_info()}\n{self.position}\n{self.subject}"


oqtuvchi = Teacher(university="Farg'ona davlat texnika unversiteti", first_name="Ali ", last_name="Aliye", age=46,
                   position="Fan Doktori", subject="Sun'iy intellekt")
# oqtuvchi.more_info()






# "OtherStaff" - child klass.U"Staff"dan vorislik oladi.Unda konstruktirida qo'shimcha (position) parametrlari bor.
# more_info() - (,) niprint qilib beradi.








class OtherStaff(Staff):
    def __init__(self, university, first_name, last_name, age, position):
        super().__init__(university, first_name, last_name, age)
        self.position = position

    def more_info(self):
        return f"{self.staff_info()}\n{self.position}"


Xodim = OtherStaff(university="Farg'ona davlat texnika unversiteti", first_name="Mashhura  ", last_name="O'ktamova",
                   age=26, position="Magistr")
# Xodim.more_info()



# "Object" - child klass. U "University" dan vorislik oladi. Unda konstruktirida qo'shimcha (name) parametrlari bor.
#     object_info() - (university, name) ni print qilib beradi.


class Obyekt(University):
    def __init__(self, university, name):
        super().__init__(university)
        self.name = name

    def obyekt_info(self):
        return f"{self.university}\n{self.name}"


obyekt = Obyekt(university="Farg'ona davlat unversiteti", name="Fizika matematika")


# obyekt.obyekt_info()


# "Computer" - child klass.U "Object" dan vorislik oladi.Unda
# konstruktirida qo'shimcha (soni, tizimi, holati) parametrlari bor.
# object_more_info() - (university, name, soni, tizimi, holati) ni print qilib beradi.


class Compyuter(Obyekt):
    def __init__(self, university, name, soni, tizimi, holati):
        super().__init__(university, name)
        self.soni = soni
        self.tizimi = tizimi
        self.holati = holati

    def obyekt_more_info(self):
        print(f"{self.obyekt_info()}\n{self.soni}\n{self.tizimi}\n{self.holati}")


compyuter = Compyuter(university="TATU ", name="Hp", soni=500, tizimi="Windows", holati="Yangi")
# compyuter.obyekt_more_info()



#
#
# "Mebel" - child klass. U "Object" dan vorislik oladi. Unda konstruktirida qo'shimcha (soni, turi, holati) parametrlari bor.
#     o - (university, name, soni, turi, holati) ni print qilib beradi.


class Mebel(Obyekt):
    def __init__(self, university, name, soni, turi, holati):
        super().__init__(university, name)
        self.soni = soni
        self.turi = turi
        self.holati = holati

    def obyekt_more_info(self):
        print(f"{self.obyekt_info()}\n{self.soni} ta\n{self.turi}\n{self.holati}")


mebel = Mebel(university="Farg'ona davlat texnika unversiteti", name="Kompyuter xonasi uchun ", turi="kompyuter uchun",
              soni=500, holati="Yangi")
# mebel.obyekt_more_info()
