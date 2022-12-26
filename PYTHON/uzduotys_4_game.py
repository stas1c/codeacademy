# Sukurti programą, kuri:
# Sugeneruotų tris atsitiktinius skaičius nuo 1 iki 6
# Jei vienas iš šių skaičių yra 5, atspausdinti „Pralaimėjai...“
# Kitu atveju atspausdinti „Laimėjai!“
# Patarimas: Naudoti while ciklą, funkciją random.randint (import random), else, break

import random

skaiciai = [random.randint(1, 6) for _ in range(3)]
print(skaiciai)
if 5 in skaiciai:
    print('Loose')
else:
    print('Win')
