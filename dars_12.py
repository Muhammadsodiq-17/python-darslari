#
# #1
def user_data():
    first_name = input("Ism:")
    last_name = input("Familya:")
    age = input("Yosh:")
    return f"Foydalanuvchi: {first_name} {last_name}, Yosh: {age}"


print(user_data())



##2
# a = int(input("A sonni kiriting:"))
# b = int(input("B sonni kiriting:"))
# c = int(input("C sonni kiriting:"))
#
#
# def find_max():
#     if a > b and a > c:
#         print(f"Eng katta son-A={a}")
#     elif a == b and b > c:
#         print(f"Eng katta son-A va B={a}")
#     elif a == c and a > b:
#         print(f"Eng katta son-A va C={a}")
#     elif b > a and b > c:
#         print(f"Eng katta son-B={b}")
#     elif b == c and b > a:
#         print(f"Eng katta son-B va C={b}")
#     elif c > a and c > b:
#         print(f"Eng katta son-C={c}")
#     elif a == b == c:
#         print(f"Hamma sonlar bir xil={a}")
#
#     return
#
#
# print(find_max())



##3
# word = input("Matnni  kiriting:")
# letter = input("Qaysi harfni sanaysiz:")
#
#
# def find_letter_count(word, letter):
#     return word.count(letter)
#
#
# print(find_letter_count(word, letter))



##4
# mylist = [1, 2, 3, 4, 5]
#
#
# def list_sum(mylist):
#     print(f"List elementlari yig'indisi=    {sum(mylist)}")
#     return sum(mylist)
#
#
# print(list_sum(mylist))



##5
# a = int(input("a sonini kiriting:"))
# b = int(input("b sonini kiriting:"))
#
#
# def daraja(a, b):
#     return a**b
#
#
# print(daraja(a,b))



##6
# a = int(input("a sonini kiriting:"))
# b = int(input("b sonini kiriting:"))
# c = int(input("c sonini kiriting:"))
# d = int(input("d sonini kiriting:"))
#
#
# def daraja(a, b, c, d):
#     return a ** b, c ** d
#
#
# print(daraja(a, b, c, d))




##7
# def digit_count_and_sum(word):
#     count = 0
#     sum = 0
#
#     for harf in word:
#         if harf.isdigit():
#             count += 1
#             sum+= int(harf)
#
#     print(f"Raqamlar soni: {count}")
#     print(f"Raqamlar yig'indisi: {sum}")
# user_input = input("Matn yoki so'zni kiriting: ")
# result = digit_count_and_sum(user_input)
# print(result)




##8
# a=input("a sonni kiriting:")
# b=input("b sonni kiriting:")
# def add_right(a, b):
#     qoshish =str(a)+ str(b)
#     print(qoshish)
# print(add_right(a,b))





##9
# a=input("a sonni kiriting:")
# b=input("b sonni kiriting:")
# def add_left(a, b):
#     qoshish =str(b)+ str(a)
#     print(qoshish)
# print(add_left(a, b))


##10
# def big_sales(sales):
#     max_month = max(sales, key=sales.get)
#     max_sales = sales[max_month]
#
#     return f"{max_month.capitalize()} oyida eng yuqori sotuv amalga oshirilgan: {max_sales}"
#
#
#
# sales = {
#     "yanvar": 12000,
#     "mart": 6000,
#     "aprel": 15000,
#     "sentabr": 9000,
#     "dekabr": 10000,
# }
# print(big_sales(sales))

 ##11
# def expensiveProduct(products):
#
#
#     max_product = max(products, key=lambda x: x['price'])
#     print(f"Eng qimmat mahsulot: {max_product['name']} - {max_product['price']}")
#
# products = [
#     {"name": "Iphone X", "price": 600},
#     {"name": "Iphone 12", "price": 1500},
#     {"name": "Samsung Note 9", "price": 800},
#     {"name": "Samsung S10", "price": 1100},
# ]
# expensiveProduct(products)
