a = int(input("Podaj pierwszy bok (pionowy): "))
b = int(input("Podaj drugi bok (poziomy): "))

for i in range(a):
    if i == 0 or i == a-1:
        for j in range(b):
            if j == b-1:
                print("*")
            else:
                print("*",end="")
    else:
        for j in range(b):
            if j==0:
                print("*",end="")
            elif j == b-1:
                print("*")
            else: print(" ",end="")
