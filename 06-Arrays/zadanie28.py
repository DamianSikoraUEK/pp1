def median(array):
    posortowana = []
    length = len(array)
    while len(posortowana) != length:
        smallest = 10000000000000000000000000000
        index = 0
        for i in range(len(array)):
            if array[i] <= smallest:
                index = i
                smallest = array[i]
        posortowana.append(smallest)
        array.pop(index)
    if length % 2 != 0:
        mediana = posortowana[length//2]
    else:
        mediana = (posortowana[length//2]+posortowana[(length//2)-1])/2
    return mediana
array = [1,0,9,4,6]
array1 = [6,8,3,1,0,5,7]
print(median(array))
print(median(array1))
