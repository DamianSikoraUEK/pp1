arr = [[3,9,2],[2,4,5],[7,1,6],[0,4,8]]
even = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] % 2 == 0:
            even = even + arr[i][j]
print(even)
