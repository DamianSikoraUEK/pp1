def factorial(n):
    if n==0 or n==1:
        return 1
    if n > 1:                           # n! = n * (n-1)!
        return n * factorial(n-1)
x = 5
print( f"{x}! = {factorial(x)}" )