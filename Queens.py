def nqueens(i, n, x):
    if i > n:
        print(x[1:])
        return
    for j in range(1, n + 1):
        if place(i, j, x):
            x[i] = j
            nqueens(i + 1, n, x)

def place(i, j, x):
    for k in range(1, i):
        if x[k] == j or abs(k - i) == abs(x[k] - j):
            return False
    return True

# Test for n = 4
n = 4
x = [0] * (n + 1)
print(f"Solutions for n = {n}:")
nqueens(1, n, x)

# Test for n = 5
n = 5
x = [0] * (n + 1)
print(f"Solutions for n = {n}:")
nqueens(1, n, x)
