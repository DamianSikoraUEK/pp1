arr = [[-38, 19], [5,40],[-7,11],[29,16]]
smallest = arr[0][0]
smallestRowAndColumn = [0,0]
largest = arr[0][0]
largestRowAndColumn =[]
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] < smallest:
            smallest = arr[i][j]
            smallestRowAndColumn = [i,j]
        if arr[i][j] > largest:
            largest = arr[i][j]
            largestRowAndColumn = [i,j]
print(smallest)
print(smallestRowAndColumn)
print(largest)
print(largestRowAndColumn)
