x = int(input("Podaj pierwszą współrzędną (x-ową): "))
y = int(input("Podaj drugą współrzędną (y-ową): "))

if x > 0 and y > 0:
    print(f"Punkt P({x},{y}) leży w pierwszej ćwiartce układu współrzędnych ")
elif x < 0 and y > 0:
    print(f"Punkt P({x},{y}) leży w drugiej ćwiartce układu współrzędnych ")
elif x < 0 and y < 0:
    print(f"Punkt P({x},{y}) leży w trzeciej ćwiartce układu współrzędnych ")
elif x > 0 and y < 0:
    print(f"Punkt P({x},{y}) leży w czwartej ćwiartce układu współrzędnych ")
elif x == 0 and y > 0:
    print(f"Punkt P({x},{y}) leży między pierwszą a drugą ćwiartką układu współrzędnych ")
elif x < 0 and y == 0:
    print(f"Punkt P({x},{y}) leży między drugą a trzecią ćwiartką układu współrzędnych ")
elif x == 0 and y < 0:
    print(f"Punkt P({x},{y}) leży między trzecią a czwartą ćwiartką układu współrzędnych ")
elif x > 0 and y == 0:
    print(f"Punkt P({x},{y}) leży między czwartą a pierwszą ćwiartką układu współrzędnych ")
