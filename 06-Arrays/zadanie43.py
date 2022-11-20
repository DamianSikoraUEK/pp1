def identity_matrix(n):
    array = []
    for i in range(n):
        array.append([])
        for j in range(n):
            if i == j:
                array[i].append(1)
            else:
                array[i].append(0)
    return array
print(identity_matrix(3))
print(identity_matrix(5))
print(identity_matrix(8))
