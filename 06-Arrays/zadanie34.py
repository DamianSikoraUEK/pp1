arr1 = [5,4,3,2,6]
arr2 = [5,4,3,2,6,7,8,12]
for i in arr1:
    appear = False
    for j in arr2:
        if i==j:
            appear = True
    if appear == False:
        print("It is not a subset")
        break
if appear == True:
    print("It is a subset")