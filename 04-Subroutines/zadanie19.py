def isInRange(x,y,number):
    if number >= x and number <= y:
        return True
    else:
        return False
x = int(input("Podaj pierwszą współrzędną zakresu: "))
y = int(input("Podaj drugą współrzędną zakresu: "))
number = int(input("Wprowadź numer, który chcesz sprawdzić w tym zakresie: "))
print(isInRange(x,y,number))