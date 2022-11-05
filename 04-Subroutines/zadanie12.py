def sum(N):
    if N == 1:
        return N
    else:
        return N + sum(N-1)
N = 6
print(f"suma liczb od 1 do {N} to {sum(N)}")

