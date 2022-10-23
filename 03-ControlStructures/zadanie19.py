wiek = int(input("Wpisz wiek psa w ludzkich latach: "))
wiekpsa = 0
for i in range(1,wiek+1):
    if i <= 2:
        wiekpsa = wiekpsa + 10.5
    else:
        wiekpsa = wiekpsa + 4
wiekpsa = int(wiekpsa)
print(f"Wiek tego psa w psich latach to {wiekpsa}")
