# def xabar(f):
#     def g(*args, **kwargs):
#         result = f(*args, **kwargs)
#         return result.upper()
#
#     return g
#
#
# @xabar
# def func(x):
#     return f"ismingiz: {x}"
#
#
# print(func("akmal"))
#




# def print_salom(func):
#     def x(*args, **kwargs):
#         print("Boshladi...")
#         result = func(*args, **kwargs)
#         print("Tugadi!")
#         return result
#
#     return x
#
#
# @print_salom
# def xabar():
#     print("Salom!")
#
#
# xabar()




# def parol_tekshir(func):
#     def son(*args, **kwargs):
#         parol = input("Parolni kiriting: ")
#         if parol == "1234":
#             return func(*args, **kwargs)
#         else:
#             print("Noto‘g‘ri parol!")
#
#     return son
#
#
# @parol_tekshir
# def maxfiy_funk():
#     print("Bu maxfiy ma'lumot!")
#
#
# maxfiy_funk()


# def ism_bilan(func):
#     def ism(*args, **kwargs):
#         ism = input("Ismingizni kiriting: ")
#         print(f"Salom, {ism}!")
#         return func(*args, **kwargs)
#
#     return ism
#
#
# @ism_bilan
# def boshlash():
#     print("Dastur ishga tushdi.")
#
#
# boshlash()
