# Parašyti programą, kuri:
# Leistų vartotojui įvesti norimą datą ir laiką
# (pvz. gimtadienį)
# Paskaičiuotų ir atspausdintų,
# kiek nuo įvestos datos ir laiko praėjo:
# Metų
# Mėnesių
# Dienų
# Valandų
# Minučių
# Sekundžių
# Kadangi tiksliai galima paskaičiuoti tik
# dienas ir sekundes, metus, mėnesius ir t.t.
# paskaičiuokite apytiksliai.
# Patarimas: naudoti datetime, .days, .total_seconds()
# Skaičių suapvalinimo pavyzdys (kurio gali prireikti
# šioje užduotyje):
import datetime

ivesta_data = input('Iveskite savo gimimo data, formatu MMMM mm dd HH:mm:ss ')
data_istraukta = datetime.datetime.strptime(ivesta_data, '%Y %m %d %I:%M:%S')

date_now = datetime.datetime.now()
difference = date_now - data_istraukta

years_passed = difference.days // 365
months_passed = (difference.days % 365) // 30
days_passed = difference.days % 365 % 30
hours_passed = difference.seconds // 3600
seconds_passed = difference.seconds % 3600

print("Praejo", years_passed, "metu,", months_passed,
      "menesiu,", days_passed, "dienu,", hours_passed, "vanaldu, ir",
      seconds_passed, "sekundziu nuo Jusu gimimo.")
