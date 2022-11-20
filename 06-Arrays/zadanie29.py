array = [1,2,3,4,5,6,7,8,9,10]
elementsGreater = 0
numberToCheck = int(input("Wpisz liczbę, którą chcesz sprawdzić: "))
for i in array:
    if i > numberToCheck:
        elementsGreater += 1
print(elementsGreater)