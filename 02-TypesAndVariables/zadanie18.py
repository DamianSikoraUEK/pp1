a = float(input("Wpisz miare pierwszego boku: "))
b = float(input("Wpisz miare drugiego boku: "))
c = float(input("Wpisz miare trzeciego boku: "))
s = float((a+b+c)/2)
A = float((s*(s-a)*(s-b)*(s-c))**(1/2))
print(f"Dla a={a}, b={b}, c={c} pole trojkata to {A}")

a = 3
b = 4
c = 5
s = float((a+b+c)/2)
A = float((s*(s-a)*(s-b)*(s-c))**(1/2))
print(f"Dla a=3, b=4, c=5 pole trojkata to {A}")
