liczba = int(input("Wpisz liczbe: "))
for i in range(1,liczba+1):
    cyfry = ""
    iterator = i
    while iterator != 0:
        cyfry = cyfry + str(i)
        iterator = iterator - 1
    print(cyfry)