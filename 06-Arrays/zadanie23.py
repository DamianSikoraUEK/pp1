def bubbleSort(arr):
    swapped = False
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if swapped == False:
            return

arr = [64, 34, 25, 12, 22, 11, 90]
arr1 = [0,12,5,123,128,43]
arr2 = [56,43,3,43,5]
 
bubbleSort(arr)
bubbleSort(arr1)
bubbleSort(arr2)
for i in range(len(arr)):
    print(arr[i], end=" ")
print("")
for i in range(len(arr1)):
    print(arr1[i], end=" ")
print("")
for i in range(len(arr2)):
    print(arr2[i], end=" ")