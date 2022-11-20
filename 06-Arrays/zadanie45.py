def convert_2d_to_1d(arr):
    pomocnicza = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            pomocnicza.append(arr[i][j])
    arr = pomocnicza
    return arr

arr1 = [[2,3],[1,5]]
arr2 = [[5,0,3,7,5],[9,0,9,1,2]]
arr3 = [[2,1],[3,5],[7,4],[2,6]]

print(convert_2d_to_1d(arr1))
print(convert_2d_to_1d(arr2))
print(convert_2d_to_1d(arr3))