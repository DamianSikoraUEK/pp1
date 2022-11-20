def occurs(number,array):
    for i in array:
        if number == i:
            return f"Number {number} appears in the array"
    return f"Number {number} does not appear in the array"
array = [15,38,7,23,14]
print(occurs(int(input("Podaj numer który chcesz sprawdzić: ")),array))