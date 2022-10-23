import random

liczby = ""

liczby = random.randint(1,49),random.randint(1,49),random.randint(1,49),random.randint(1,49),random.randint(1,49),random.randint(1,49),random.randint(1,49)
for j in range(len(liczby)):
    for i in range(len(liczby)):
        if i == j:
            continue
        if liczby[i] == liczby[j]:
            liczby[i] = random.randint(1,49)
            print("jd")
print(liczby)