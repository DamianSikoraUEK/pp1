def star(n):
    stars = ''
    for i in range(n):
        stars = stars + "*"
    return stars

arr = [12,6,4,9,10]
for i in arr:
    print(f'{i}: {star(i)}')