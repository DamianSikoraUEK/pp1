number1 = int(input("Wpisz pierwszy numer: "))
number2 = int(input("Wpisz drugi numer: "))
if number1 > 0 or number2 > 0:
    print(f"Przynajmniej jedna z liczb ({number1} lub {number2}) jest dodatnia")
else:
    print(f"Obie liczby ({number1} lub {number2}) są ujemne")