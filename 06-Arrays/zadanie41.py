arr = [[7,3,7,9,0],[2,9,0,1,5],[3,8,6,4,7]]
arr1 = [[7,3,7,9,0],[2,9,0,1,5],[3,8,6,4,7]]
for i in range(len(arr)):
    pomocnicza = arr[i][0]
    arr[i][0] = arr[i][-1]
    arr[i][-1] = pomocnicza
for i in arr1:
    print(i)
print("")
for i in arr:
    print(i)