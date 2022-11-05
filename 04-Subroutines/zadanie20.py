def power(x,n):
    if n == 0:
        return 1
    if n >= 1:
        return x * power(x, n - 1)
x = 5
n = 3
print(f"{x} do potęgi {n} to {power(x,n)}")