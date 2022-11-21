file = open(input("Wpisz nazwę pliku z rozszerzeniem: "),"r")
licznikLini = 0
for line in file:
    licznikLini = licznikLini+1
print(licznikLini)
file.close()