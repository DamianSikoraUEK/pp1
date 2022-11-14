arr =  [1,2,3,4,5]
# arr[0] = arr[0]-1
arr[0] -= 1
print(arr[0])
# arr[-1] = arr[-1]+4
arr[-1] +=4
print(arr[-1])
# arr[len(arr)//2] = arr[len(arr)//2]*2
arr[len(arr)//2] *= 2
print(arr[len(arr)//2])
for i in range(len(arr)):
    # arr[i] = arr[i]+3
    arr[i] +=3
print(arr)
