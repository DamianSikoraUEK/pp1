arr = [15,8,31,47,2,19]
sum = 0
arithmetic = 0
i = 0
while i <= (len(arr)-1):
    sum = sum + arr[i]
    i = i+1
arithmetic = sum /len(arr)
print (sum, arithmetic)