kodPin = '0805'
for i in range(3):
    wpisaniePinu = str(input("Podaj kod pin: "))
    if wpisaniePinu != kodPin and i == 2:
        print("Kod niepoprawny")
        print("Przepraszamy, twoja karta płatnicza została zablokowana")
    elif wpisaniePinu != kodPin:
        print("Kod niepoprawny")
    else:
        print("Kod poprawny")
        break