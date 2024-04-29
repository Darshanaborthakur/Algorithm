def binarySearch(x, L, low, high):
    if low == high:
        if x == L(low):
            return low
        else:
            return -1
    
    else:
        mid = (low + high) // 2
        if x == L[mid]:
            return mid
        elif x < L[mid]:
            return binarySearch(x, L, low, mid - 1)
        else:
            return binarySearch(x, L, mid + 1, high)

my_list = [2, 5, 7, 10]
x = 5
print(binarySearch(x, my_list, 0, len(my_list) - 1))
