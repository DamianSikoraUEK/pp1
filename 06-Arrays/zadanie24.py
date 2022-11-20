arr = [2,3,2,5,8,1,9,8]
uniqueElements = []
for i in range(len(arr)):
    unique = arr[i]
    isUnique = True
    for j in range(len(arr)):
        if i == j:
            continue
        if arr[i] == arr[j]:
            isUnique = False
    if isUnique == True:
        uniqueElements.append(arr[i])
print(uniqueElements)
