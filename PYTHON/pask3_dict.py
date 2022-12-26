age = {'Rokas': 20, 'Andrius': 34, 'Laura': 25}
# print(age)
# print(age['Andrius'])
# age['Kyle'] = 33
# print(age)
# del age['Kyle']
# print(age)
# for x in age:
#     print (x)

# for x in age.values():
#     print(x)

# Atspausdinam zodino elementus
for x in age.items():
    print(x)
print('---------------')
print('---------------')

# Atspausdinam zodino elementus ir reiksmes
for y, x in age.items():
    print(x, y)

print('---------------')
print('---------------')

# Pridedam irasa i zodina
age.update({'Stan': 39})
print(age)

# Istrinam irasa
age.pop('Andrius')
print(age)

# Pakeiciam irasa
age.update({'Stan': 38})
print(age)
