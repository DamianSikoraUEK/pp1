pierwsza = 0
druga = 1
ilosc = 50
print(pierwsza,druga,end=" ")
while ilosc - 2>0:
    trzecia = pierwsza + druga
    pierwsza = druga
    druga = trzecia
    print(trzecia,end=" ")
    ilosc = ilosc - 1