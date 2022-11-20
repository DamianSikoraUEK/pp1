def create_2d_arr(x,y):
    array = []
    for i in range(y):
        array.append([])
        for j in range(x):
            array[i].append(0)
    return array
    
for i in create_2d_arr(3,5):
    print(i)