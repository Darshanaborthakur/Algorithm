def Linear(A,x,n):
    if n == 0:
        return None
    for i in range(n):
        if x == A[i]:
            return i
        else:
            return -1

list=[1, 2 , 3, 4]
x=5
print(Linear(list,x,len(list)-1))