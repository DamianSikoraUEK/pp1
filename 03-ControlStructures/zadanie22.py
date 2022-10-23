wynik = ""
for i in range(1,31):
    if i % 3 == 0 and i % 5 != 0:
        wynik = wynik + "THREE "
    if i % 5 == 0 and i % 3 != 0:
        wynik = wynik + "FIVE "
    if i % 3 == 0 and i % 5 == 0:
        wynik = wynik + "BINGO "
    if i % 3 != 0 and i % 5 != 0:
        wynik = wynik + str(i) + " "
print(wynik)
    