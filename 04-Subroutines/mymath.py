import random

def read_number():
    numer = int(input("Wpisz cyfrę: "))
    return numer

def generate_number():
    losowy = random.randint(1,9)
    return losowy