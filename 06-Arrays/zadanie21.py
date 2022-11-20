def compare(array1,array2):
    if len(array1) != len(array2):
        return False
    else:
        for i in range(len(array1)):
            if array1[i] != array2[i]:
                return False
    return True
print(f'Array1: water book sky\nArray2: water book sky\n{compare(["water","book","sky"],["water","book","sky"])}')
print(f'Array1: True False \nArray2: True False True\n{compare(["True","False"],["True","False","True"])}')
print(f'Array1: 5 3 1\nArray2: 5 3 1\n{compare([5,3,1],[5,3,1])}')
print(f'Array1: 3 2 1\nArray2: 3 2 \n{compare([3,2,1],[3,2])}')