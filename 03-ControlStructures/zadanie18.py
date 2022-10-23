kwota = int(input("Podaj kwotę w złotówkach: "))

piatka = 0
dwojka = 0
jedynka = 0
kwotapomocnicza = kwota

while kwotapomocnicza - 5 >= 0:
    piatka = piatka + 1
    kwotapomocnicza = kwotapomocnicza - 5
while kwotapomocnicza - 2 >= 0:
    dwojka = dwojka + 1
    kwotapomocnicza = kwotapomocnicza - 2
while kwotapomocnicza - 1 >= 0:
    jedynka = jedynka + 1
    kwotapomocnicza = kwotapomocnicza - 1
print(f"{kwota}zł w monetach to:")
print(f"5zł - {piatka} ")
print(f"2zł - {dwojka} ")
print(f"1zł - {jedynka} ")