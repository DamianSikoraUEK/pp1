def calculate(x):
    suma = 0
    for i in str(x):
        suma = suma + int(i)
    return suma
liczba = 7182
print(f"Suma cyfr w liczbie {liczba} wynosi {calculate(liczba)}")