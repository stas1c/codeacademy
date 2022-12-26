# Sukurti programą, kuri:
# Leistų vartotojui įvesti 5 žodžius
# Pridėtų įvestus žodžius į sąrašą
# Atspausdintų kiekvieną žodį, jo ilgį ir eilės numerį sąraše (nuo 1)
# Sudėtingiau: kad programa leistų įvesti norimą žodžių kiekį
# Patarimas: Naudoti sąrašą (list), ciklą for, funkcijas len ir index


words_list = []

for i in range(5):
    word = input('Enter a word: ')
    words_list.append(word)

for i, word in enumerate(words_list, start=1):
    print(f'Word {i}: {word} ({len(word)} characters)')
