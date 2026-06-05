# def str_counter(strs):
#     royxat = {}
#     for x in strs:
#         uzunlik = len(x)
#         royxat[uzunlik] = x
#     return royxat
#
#
# print(str_counter(["olma", "nok", "shaftoli", "gilos ", "bir ", "dekabr"]))




#
# def merge_list(l1, l2):
#     kalit = {}
#     for i in range(len(l1)):
#         kalit[l1[i]] = l2[i]
#     return kalit
#
#
# print(merge_list(["a", "b", "c"], [1, 2, 3]))




# kontakt = {"Nodir": "+998918602711", "Laziz": "+998908002534"}
#
# while True:
#     print(" 1. Qo‘shish\n 2. Yangilash \n 3. O‘chirish \n 4. Qidirish \n 5. Ko‘rish \n 0. Chiqish")
#     tanlov = input(" Tanlov: ")
#     if tanlov == "1":
#         ism = input("Ism: ")
#         raqam = input("Raqam: ")
#         kontakt[ism] = raqam
#         print("Qo‘shildi.")
#
#     elif tanlov == "2":
#         ism = input("Ism: ")
#         if ism in kontakt:
#             yangi = input("Yangi raqam: ")
#             kontakt[ism] = yangi
#             print("Yangilandi.")
#         else:
#             print("Topilmadi.")
#
#     elif tanlov == "3":
#         ism = input("Ism: ")
#         if ism in kontakt:
#             del kontakt[ism]
#             print("O‘chirildi.")
#         else:
#             print("Topilmadi.")
#
#     elif tanlov == "4":
#         ism = input("Ism: ")
#         print(f"{ism}: {kontakt.get(ism, 'Topilmadi')}")
#
#     elif tanlov == "5":
#         for ism, raqam in kontakt.items():
#             print(f"{ism}: {raqam}")
#
#     elif tanlov == "0":
#         print("Chiqildi.")
#         break
#
#     else:
#         print("Noto‘g‘ri tanlov.")





#
# def counter_dict(raqamlar):
#     result = {}
#     for raqam in raqamlar:
#         if raqam in result:
#             result[raqam] += 1
#         else:
#             result[raqam] = 1
#     return result
#
#
# print(counter_dict([1,2,1,1]))





#
# def max_ball_students(talabalar):
#     saralangan = sorted(talabalar.items(), key=lambda item: item[1], reverse=True)
#
#     eng_yaxshilar = dict(saralangan[:2])
#
#     return eng_yaxshilar
#
#
# print(max_ball_students({"Akmal": 64, "Tohir": 55, "Nodir": 76, "Zafar": 80}))
