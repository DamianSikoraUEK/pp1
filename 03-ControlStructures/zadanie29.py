print("Kalkulator sumy i średniej arytmetycznej, by przerwać, naciśnij 0")
numer = 1
tablica = []

while numer != 0:
    numer = int(input("Podaj liczbę: "))
    if numer != 0:
        tablica.append(numer)
suma = 0
for i in tablica:
    suma = suma + i

print(f"Wynik: Ilość liczb={len(tablica)}, Suma={suma}, Średnia arytmetyczna={suma/len(tablica)}")
