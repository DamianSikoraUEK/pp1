height = float(input("Podaj wzrost w cm: "))
weight = float(input("Podaj wage w kg: "))
bmi = (weight/height**2)*10000

print(f"BMI index: {bmi}")
if bmi < 16:
    print("wyglodzenie")
if bmi >=16 and bmi < 17:
    print("wychudzenie")
if bmi >=17 and bmi < 18.5:
    print("niedowaga")
if bmi >=18.5 and bmi < 25:
    print("waga prawidlowa")
if bmi >=25 and bmi < 30:
    print("nadwaga")
if bmi >=30 and bmi < 35:
    print("I stopien otylosci")
if bmi >= 35 and bmi < 40:
    print("II stopien otylosci")
if bmi >=40:
    print("Otylosc skrajna")