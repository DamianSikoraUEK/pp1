import random
def rand_elem(array):
    return array[random.randint(0,len(array)-1)]
arr = [5,4,3,2,6,7,8,12]
print(rand_elem(arr))
print(rand_elem(arr))
print(rand_elem(arr))