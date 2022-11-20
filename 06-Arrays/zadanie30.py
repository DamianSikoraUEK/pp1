def minmax(array):
    min = array[0]
    max = array[0]
    for i in array:
        if i < min:
            min = i
        if i > max:
            max = i
    return [min,max]
array = [4,2,8,4,7,9,5]
print(minmax(array))