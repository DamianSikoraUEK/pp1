def calculations(tekst,litera):
    ileRazy = 0
    for i in tekst:
        if i.lower() == litera.lower():
            ileRazy = ileRazy + 1
    return ileRazy

tekst = "You never get a second chance to make a first impression"
litera = input("Wpisz, ilość której litery chcesz policzyć w tekście: ")
print(f"Litera {litera} występuje w tekście {calculations(tekst,litera)} raz(y)")

print(f"Litera e występuje w tekście {calculations(tekst,'e')} raz(y)")
