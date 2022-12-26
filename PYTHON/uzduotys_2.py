# Parašyti programą, kuri:
# Leistų vartotojui įvesti skaičių.
# Jei įvestas skaičius yra teigiamas, paprašyti įvesti dar vieną skaičių
# Jei įvestas skaičius neigiamas, nutraukti programą ir atspausdinti visų įvestų teigiamų skaičių sumą
# Patarimas: Naudoti ciklą while, sąlygą if, break

total = 0
while True:
    user_number = int(input('Input number: \n'))
    if user_number < 0:
        break
    total += user_number

print('Sum of numbers is', total)
