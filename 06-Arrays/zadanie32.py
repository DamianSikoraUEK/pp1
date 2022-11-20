def arrToString(arr):
    string = ""
    for i in range(len(arr)):
        if i == len(arr)-1:
            string = string+str(arr[i])
        else:
            string = string+str(arr[i])+","
    return string
arr = [5,4,3,2,6,5]
print(arrToString(arr))