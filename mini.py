import time
import random

def search(x,L):
    comparisons = 0

    # Base case: if the list has only one element, return that element
    if len(L) == 1:
        if x==L:
            return 1
        else:
            return -1
        return L[0],0

    # Split the list into two halves
    mid = len(L) // 2
    L1 = L[:mid]
    L2 = L[mid:]
    i=search(x,L1)
    j=search(x,L2)
    if(i!=1):
        return i
    elif(j!=1):
        return j
    else:
        return -1

    o1, comparisons_left = Search(i)
    o2, comparisons_right = Search(j)

    # Combine results and count comparisons
    comparisons += comparisons_left + comparisons_right
    if o1 <= o2:
        return o1, comparisons + 1
    else:
        return o2, comparisons + 1

# Test the function with different values of n
n_values = [10, 100, 1000, 10000, 100000]

# Print headers
print("n\t\e")



for n in n_values:
    
    A = [random.randint(1, 1000) for _ in range(n)]

    comparisons, elapsedtime = search(n,A)

    print(f"{n}\tComparisons:{comparisons}")
    print(f"{n}\tTime Taken: {elapsedtime:5f}")