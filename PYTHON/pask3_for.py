# list  = [45, 126, 7, 'Hey', 45.45]

# for x in list:
#     print(x)
    
digits = [ 2, 4, 6, 7, 8, 5, 4]

sum_of_digits = 0

for x in digits:
    if x == 4:
        continue
    sum_of_digits = sum_of_digits + x
    # if sum_of_digits >= 25:
    #     break

print(f'Suma {sum_of_digits}') 


# for x in 'banana':
#     print(x)
#     if x == 'n':
#         break