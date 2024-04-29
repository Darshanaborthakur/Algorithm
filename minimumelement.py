def minimum(L):
    if len(L)==1:
        return L[0]
    else:
        mid=len(L) // 2
        e1=minimum(L[:mid])
        e2=minimum(L[mid:])
        if e1<=e2:
            return e1
        else:
            return e2
        
list=[5, 6, 7, 8, 9, 2]
print( "Minimum in the list:", minimum(list) )

