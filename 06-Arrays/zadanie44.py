def transpose_matrix(m):
    for i in range(len(m)):
        for j in range(i+1, len(m)):
            m[i][j], m[j][i] = m[j][i], m[i][j]

arr1  = [[1,2,3],[4,5,6],[7,8,9]]
arr2 = [[1,2,3,4,5],[6,7,8,9,0]]
arr3 = [[5,6,7,8]]

transpose_matrix(arr1)
transpose_matrix(arr2)
transpose_matrix(arr3)
for i in arr1:
    print(i)
print("")
for i in arr2:
    print(i)
print("")
for i in arr3:
    print(i)
print("")