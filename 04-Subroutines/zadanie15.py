from mymath import read_number
from mymath import generate_number

cyfraUzytkownika = read_number()
cyfraKomputera = generate_number()

if cyfraKomputera == cyfraUzytkownika:
    print("Gratuluję, wygrałeś")
else:
    print("Przegrałeś")