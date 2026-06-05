# def son_genrator():
#     def is_son(sonlar):
#         if sonlar < 2  :
#             return False
#         for i in range (2, int(sonlar ** 0.5)+1):
#             if sonlar % i == 0:
#                 return False
#         return True
#     sonlar = 2
#     while True:
#         if is_son(sonlar):
#             yield sonlar
#         sonlar += 1
# sonlar = son_genrator()
# for _ in range(9):
#     print(next(sonlar))


# string = ['a', 'b', 'c']
# import itertools
# def parol_generator(input_string):
#     for i in itertools.permutations(input_string):
#         yield '' .join(i)
# input_string = "abs"
# passwords = parol_generator(input_string)
# for _ in range(6):
#     print(next(passwords))


# def fibonachi(n):
#      if n == 0:
#          return 0
#      elif n  == 1:
#          return 1
#
#      else:
#          return fibonachi(n-1) + fibonachi(n-2)
# print(fibonachi(10))



import itertools
my_list=[1,2,3,4,5,6,7,8,9]
n=3
def birlashtirish(my_list, n):
    for juf in itertools.combinations(my_list, n):
        yield juf
for i in birlashtirish(my_list,n):
    print(i)

