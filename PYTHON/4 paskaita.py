#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Mes praėjome:
    - Duomentų tipus: int, float, str, bool, list, dict {keyword: value}, set {}, tuple ()
    - salygas if
    - ciklą while
    - ciklą for


# all()/any()/enumerate()/len()/max()/min()/range()/sorted()/sum()

# In[ ]:


numbers_list = [a for a in range(3, 10)]

print(numbers_list)


# In[ ]:


numbers_list = [a for a in range(10)]

all(numbers_list)


# In[ ]:


numbers_list = [a for a in range(1)]

print(numbers_list)
print(any(numbers_list))


# In[ ]:


{
    1: 'Dalinti', 
    2: 'Dauginti'
}

for number, value in enumerate([10, 22, 33]):
    print(number, value)


# In[ ]:


print(max([3, 4, 5, 6, 7, 8, 9]))
print(min([3, 4, 5, 6, 7, 8, 9]))


# In[ ]:


masyvas = [5, 3, 4]

print(sorted(masyvas))

print(masyvas)
masyvas.sort()
print(masyvas)


# In[ ]:


masyvas = [5, 3, 4]

print(sum(masyvas))


# DRY - don't repeat yourself

# value = 15
# 
# if (value % 3 == 0) and (value % 5 == 0):
#     print("dalyba")

# In[ ]:


value = 9

if (value % 3 == 0) and (value % 5 == 0): 
    result = "3 ir 5"
elif value % 5 == 0:
    result = "5"
elif value % 3 == 0:
    result = "3"
    
print(f'Result is {result}')


# In[3]:


if 10 == int('10'):
    result = 'a'
elif 'bag' < 'bapple':
    result = 'b'
else:
    result = 'c'
    
print(result)


# In[8]:


sarasas = [5, 8, 'Lietuva']


suma = 0

for x in sarasas:
    if type(x) is int:
        suma += x
        
print(suma)


# In[9]:


sarasas = [5, 8, 'Lietuva']


suma = 0

for x in sarasas:
    if isinstance(x, int):
        suma += x
        
print(suma)


# Sugeneruoti random pagalba 100 skaičiaus listą intervale 0-100, jį atspausdinti, tada patikrinti ar jame yra 0
# 
# Naudoti For ciklą, random biblioteką, if sąlyga.

# In[25]:


import random

print(random.randint(0, 100))


# In[1]:


for i in range(5):
    print(i)


# Yra masyvas:
# data = ['Mes mokinames programuoti', [2, 2, 3], (True, True, True), (True, False, True), {'one':1, 'two':2, 'three':3, 'four': 4}]
# 
# Jei string tipas - suskaičiuoti kiek raidžių iš visu ir kiek yra unikalių raidių. Išvesti sakinyje;
# Jei listas - suskaičiuoti kiek narių, sudėti ir sudauginti visus.
# Jei tuple - patikrinti ar visos reikšmės yra True
# Jei dict - išspausdinti du listus, viename liste raktai (keywords), kitame - reikšmės (values)

# In[28]:


masyvas = (0, 1, 2)

print(isinstance(masyvas, list))


# Parašyti programą, kuri:
# Leistų vartotojui įvesti skaičių.
# Jei įvestas skaičius yra teigiamas, paprašyti įvesti dar vieną skaičių
# Jei įvestas skaičius neigiamas, nutraukti programą ir atspausdinti visų įvestų teigiamų skaičių sumą
# Patarimas: Naudoti ciklą while, sąlygą if, break
# 

# In[ ]:


Sukurti programą, kuri:
Leistų vartotojui įvesti 5 žodžius
Pridėtų įvestus žodžius į sąrašą
Atspausdintų kiekvieną žodį, jo ilgį ir eilės numerį sąraše (nuo 1)
Sudėtingiau: kad programa leistų įvesti norimą žodžių kiekį
Patarimas: Naudoti sąrašą (list), ciklą for, funkcijas len ir index


# In[ ]:


Sukurti programą, kuri:
Sugeneruotų tris atsitiktinius skaičius nuo 1 iki 6
Jei vienas iš šių skaičių yra 5, atspausdinti „Pralaimėjai...“
Kitu atveju atspausdinti „Laimėjai!“
Patarimas: Naudoti while ciklą, funkciją random.randint (import random), else, break


# In[ ]:


Sukurti programą, kuri:
Leistų vartotojui įvesti metus
Atspausdintų „Keliamieji metai“, jei taip yra
Atspausdintų „Nekeliamieji metai“, jei taip yra

Keliamieji metai yra kas 4 metus, išskyrus paskutinius amžiaus metus, kurie keliamieji yra tik kas 400 metų


# Bibliotekos: kaip importuoti
