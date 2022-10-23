iloscLiczb = int(input("Wpisz ile chcesz poznac liczb pierwszych: "))
tablica = []
poczatkowa = 2
while len(tablica) != iloscLiczb:
    liczbaDzielnikow = 0
    for i in range(1,poczatkowa+1):
        if poczatkowa % i == 0:
            liczbaDzielnikow = liczbaDzielnikow + 1
    if liczbaDzielnikow == 2:
        tablica.append(poczatkowa)
    poczatkowa = poczatkowa + 1
liczbaDzielnikow = 0
czyIloscLiczbToDwa = ''
for i in range(1,poczatkowa+1):
    if poczatkowa % i == 0:
        liczbaDzielnikow = liczbaDzielnikow +1
if liczbaDzielnikow == 2:
    czyIloscLiczbToDwa = f"{iloscLiczb} jest pierwsza"
else:
    czyIloscLiczbToDwa = f"{iloscLiczb} nie jest pierwsza"
print(f"{iloscLiczb} liczb pierwszych to: {tablica}, a liczba {czyIloscLiczbToDwa}")