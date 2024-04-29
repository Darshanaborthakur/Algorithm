# Define the recursive procedures for the 0/1 Knapsack problem

# Procedure for Opt1
def Opt1(i, X, p, w):
    if X < 0:
        return float('-inf')  # return a large negative value
    elif i == 0:
        return 0
    else:
        val1 = Opt1(i - 1, X, p, w)
        val2 = p[i] + Opt1(i - 1, X - w[i], p, w)
        if val2 > val1:
            return val2
        else:
            return val1

# Procedure for Opt2
def Opt2(i, X, p, w):
    if i == 0:
        return 0
    else:
        if X < w[i]:
            val1 = Opt2(i - 1, X, p, w)
            return val1
        else:
            val1 = Opt2(i - 1, X, p, w)
            val2 = p[i] + Opt2(i - 1, X - w[i], p, w)
            if val2 > val1:
                return val2
            else:
                return val1

# Test cases

# Test case 1
n1 = 3
p1 = [0, 1, 2, 5]  # profit array
w1 = [0, 2, 3, 4]  # weight array
M1 = 6  # knapsack capacity

print("Result using Opt1 for Test Case 1:", Opt1(n1, M1, p1, w1))
print("Result using Opt2 for Test Case 1:", Opt2(n1, M1, p1, w1))

# Test case 2
n2 = 4
p2 = [0, 10, 5, 20, 30]  # profit array
w2 = [0, 3, 2, 3, 4]  # weight array
M2 = 9  # knapsack capacity

print("Result using Opt1 for Test Case 2:", Opt1(n2, M2, p2, w2))
print("Result using Opt2 for Test Case 2:", Opt2(n2, M2, p2, w2))
