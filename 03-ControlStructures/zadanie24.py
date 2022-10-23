wiersz = int(input("Wpisz ile wierszy ma zostac zapelnione gwiazdkami: "))
if wiersz % 2 == 0:
    srodek = int(wiersz/2)
else:
    srodek = int(wiersz/2)+1
for i in range(1,srodek+1):
    gwiazdki = ""
    iterator = i
    while iterator != 0:
        gwiazdki = gwiazdki + "*"
        iterator = iterator - 1
    print(gwiazdki)
if wiersz % 2 == 0:
    print(gwiazdki)
for i in range(1,srodek):
    print(gwiazdki[:-i])
