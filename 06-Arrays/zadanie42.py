arr = [[7,3,7,9,0],[2,9,0,1,5],[3,8,6,4,7]]
arr1 = [[7,3,7,9,0],[2,9,0,1,5],[3,8,6,4,7]]
for i in range(len(arr[0])):
    pomocnicza = arr[0][i]
    print(arr[0][i])
    arr[0][i] = arr[-1][i]
    print(arr[-1][i])
    arr[-1][i] = pomocnicza
for i in arr1:
    print(i)
print("")
for i in arr:
    print(i)