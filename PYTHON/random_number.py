import random

# sukuriam sarasa is atsitiktiniu skaiciu tarp 1 iki 50 , 20 skaiciu ilgio

big_list = [random.randint(1, 50) for _ in range(20)]

# ivedam ieskoma skaiciu

des_number = int(input('Enter your number: \n'))
for x in big_list:
    print(x)
    if x == des_number:
        print('Desired number found!')
        break
else:
    print('Number not found')
