# Yra masyvas: data = ['Mes mokinames programuoti', [2, 2, 3], (True, True, True), (True, False, True),
# {'one':1, 'two':2, 'three':3, 'four': 4}]
# Jei string tipas - suskaičiuoti kiek raidžių iš visu ir kiek yra unikalių raidių. Išvesti sakinyje;
# Jei listas - suskaičiuoti kiek narių, sudėti ir sudauginti visus.
# Jei tuple - patikrinti ar visos reikšmės yra True
# Jei dict - išspausdinti du listus, viename liste raktai (keywords), kitame - reikšmės (values)

# Jei string tipas - suskaičiuoti kiek raidžių iš visu ir kiek yra unikalių raidių. Išvesti sakinyje;

data = ['Mes mokinames programuoti', [2, 2, 3], (True, True, True), (True, False, True),
        {'one': 1, 'two': 2, 'three': 3, 'four': 4}]

for value in data:
    result = ''
    if isinstance(value, str):
        # Jei string tipas - suskaičiuoti kiek raidžių iš visu ir kiek yra unikalių raidių. Išvesti sakinyje;
        number_of_letters = len(value)
        unique_value = len(set(value))
        result = f"Str value: '{value}' contains {number_of_letters} values, unique values: {unique_value}"
    elif isinstance(value, list):
        # Jei listas - suskaičiuoti kiek narių, sudėti ir sudauginti visus.
        number_of_values = len(value)
        sum_of_values = sum(value)
        multiply_values = 1
        for v in value:
            multiply_values *= v
        result = f'List {value} contains {number_of_values} elements,' \
                 f' suma of elements {sum_of_values}, multiply {multiply_values}'
    elif isinstance(value, tuple):
        # Jei tuple - patikrinti ar visos reikšmės yra True
        result = f'Tuple {value} all is True' if all(value) else f'Tuple {value} all is False'
    elif isinstance(value, dict):
        # Jei dict - išspausdinti du listus, viename liste raktai (keywords), kitame - reikšmės (values)
        keys = list(value.keys())
        values = list(value.values())
        result = f"""
        Keys: {keys},
        Values: {values}
        """
    print(result)
