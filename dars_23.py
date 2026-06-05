


class Bankaccaunt:
    def __init__(self, _balans):
        self.balans = _balans

    def deposit(self, qoshish):
        if qoshish > 0:
            self.balans += qoshish

            print(f"Pul qo'shildi:{qoshish}")
        else:
            print("Xato qiymat kiritildi qayta urining ")

    def withdraw(self, ayirish):
        if ayirish > self.balans:
            print(f"Balansda pul yeterli emas ")
        elif ayirish > 0:
            self.balans = self.balans - ayirish

            print(f"Balansdan pul yechildi:{ayirish}\nBalans:{self.balans} so'm ")
        else:
            print("Xato qiymat kiritildi")

    def check_balanse(self):
        print(f"Balans:{self.balans}")


m = Bankaccaunt(_balans=100000)
# m.deposit(100000)
# m.withdraw(10000)
# m.check_balanse()


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        yuza = self.length * self.width
        if self.length == self.width:
            print(f"Kvadratning yuzi:{yuza} metr kvadrat")
        else:
            print(f"To'rtburchakning yuzi:{yuza} metr kvadrat")

    def perimeter(self):
        perimetr = (self.length + self.width) * 2
        if self.length == self.width:
            print(f"Kvadratning perimetri:{perimetr} metr ")
        else:

            print(f"Perimetri:{perimetr} metr")

    def is_sequare(self):
        if self.length == self.width:
            print("Bu shakl kvadrat")
        else:
            print("Bu shakl to'rtburchak")


# tortburchak = Rectangle(length=10, width=30)
# tortburchak.is_sequare()
# tortburchak.area()
# tortburchak.perimeter()


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []

    def add_grade(self, grede):
        if 0 < grede < 100:
            self.grades.append(grede)
            print(f"Ball qo'shildi {grede}")
        else:
            print("Xato qiymat kiritildi")

    def calculate_average(self):
        average = sum(self.grades) / len(self.grades)
        print(f"O'rtacha ball:{average}")

    def print_summary(self):
        print(f"Ismi:{self.name}\nYoshi:{self.age}\n{self.grades}")


talaba = Student(name="Mashhura", age=18)
# talaba.add_grade(20)
# talaba.add_grade(50)
# talaba.calculate_average()
# talaba.print_summary()


p = 3.14


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        s = p * self.radius ** 2
        print(f"Doiraning yuzi:{s} metr kvadrat")

    def circumference(self):
        l = 2 * p * self.radius
        print(f"Aylana uzunligi:{l} metr")

    def diametr(self):
        print(f"Aylan diametri:{self.radius * 2} metr")


# doira = Circle(radius=20)
# doira.area()
# doira.diametr()
# doira.circumference()





class Book:
    def __init__(self,title, author, current_page):
        self.title=title
        self.author=author
        self.current_page=current_page
    def open(self):
        self.current_page+=1
        print(f"Kitobning sahifasi ")
    def turn_page(self,saxifa):
        saxifa=self.current_page+1
        print(f"Kitobning hozirgi saxifasi:{saxifa}")
    def restart(self):

        if self.current_page==100:
            saxifa=self.current_page=0
            print(f"{saxifa}")
        else:
            self.current_page += 1
            print(f"Kitobning saxifasi:{self.current_page}")
kitob=Book(title="Fizika",author="Aliyev Shuxrat",current_page=1)
# kitob.open()
# kitob.turn_page(20)
# kitob.restart()
#
#
#



## Class metodlari


class Dog:
    total_dogs=0
    def __init__(self):

       Dog.total_dogs+=1
    @classmethod
    def get_total_dogs(cls):
        return f"Itlar soni:{cls.total_dogs}"

# dog=Dog()
# dog1=Dog()
# dog2=Dog()
# dog3=Dog()
# print(Dog.get_total_dogs())



class Computer:
    total_computers=0
    computers_list=[]
    def __init__(self,model):
        self.model=model
        Computer.add_computer(self)
    @classmethod
    def add_computer(cls,qoshish):
        cls.computers_list.append(qoshish)
        cls.total_computers+=1
        return f"Kompyuter qo'shildi:{qoshish}"
noutbuk=Computer("Hp")
noutbuk1=Computer("Mac")
noutbuk2=Computer("Lenovo")
noutbuk3=Computer("Acer")
# print(f"Kompyuterlar qoshildi:{Computer.total_computers}")
# print(f"Kompyuter :{Computer.computers_list[0].model}")




class Employee:
    total_employees=0
    employees_list=[]
    def __init__(self,xodim):
        self.xodim=xodim
        Employee.hire_employee(self)
    @classmethod
    def hire_employee(cls,xodim):
        cls.employees_list.append(xodim)
        cls.total_employees+=1
        return f"Yangi xodim qo'shildi:{xodim}"
xodim=Employee("ali")
xodim2=Employee("Rano")
xodim3=Employee("Vali")
# print(f"Xodim :{Employee.total_employees}")
# print(f"Xodimlar:{Employee.employees_list[0].xodim}")
#
# print(f"Xodimlar:{Employee.employees_list[1].xodim}")



class Math:
    @staticmethod
    def multiply(a,b):
        return a*b
# print(Math.multiply(2,3))


class Temperature:
    @staticmethod
    def celsius_to_fahrenheit(C):
        return  (C *1.8) + 32
# print(f"Temperatura:{Temperature.celsius_to_fahrenheit(34)}")




class Distance:
    @staticmethod
    def miles_to_kilometers(x):
        return f"{x} mill \nKilometrga o'tkazildi:{x*1609} km"
# print(Distance.miles_to_kilometers(30))



class Utility:
    @staticmethod
    def is_even(n):
        if n%2==0:
            print(True)
        else:
            print(False)
# Utility.is_even(3)




class Time:
    @staticmethod
    def seconds_to_minutes(n):
        minut = n // 60
        sekund = n % 60
        return (minut, sekund)
# print(Time.seconds_to_minutes(200))















