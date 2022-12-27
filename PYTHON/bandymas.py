#
# listing = [1, 2, 3, "Hey", 45.5]
# num_list = [55, 44, 1, 18]
# ex_dict = {"car": 2500, "bike": 3000, "truck": 5000}
# sum_of = 0
#
# for i in listing:
#     print(i)
#
# for y in num_list:
#     sum_of += y
# print(sum_of)
# print('---------------')
# for x, z in ex_dict.items():
#     print(x, z)
#
# for sk in range(10, 20, 3):
#     print(sk)
#
# print('---------------')
#
# a = 2
# while a < 50:
#     a += 3
#     print(a)
# print('---------------')
#
# list_1 = range(2, 8, 2)
# for one in list_1:
#     print(one)
#     if one == 8:
#         print('Breaking')
#         break
# else:
#     print('Cycle is finished')
# print('---------------')
# print(len(list_1))
# print('---------------')
# print('---------------')
# for next in range(0, 6):
#     if next == 3:
#         continue
#     print(next)
# print('---------------')
# print('---------------')

#
# x = datetime.datetime.today()
# print(x)
#
# y = datetime.datetime.today().time()
# print(y)
# print('---------------')
# print('---------------')
#
# now = datetime.datetime.now()
# print(now)
# print(now - datetime.timedelta(days=5, hours=10))
# print('---------------')
# print('---------------')
#
# try:
#     skaicius = int(input('Iveskite skaiciu: '))
# except:
#     print('Ne skaicius')
# print('---------------')
# print('---------------')

while True:
    try:
        x = int(input('Iveskite skaiciu: '))
        break
    except ValueError:
        print("Ivedete ne skaiciu. Bandom dar karta")
