arr = [4,2,8,4,7,9,5]
even = []
odd = []
for i in arr:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
arr.clear()
for i in even:
    arr.append(i)
for i in odd:
    arr.append(i)
print(arr)