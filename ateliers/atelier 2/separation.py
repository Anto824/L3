

def separation(L):
    LSEP = []
    A = []
    B = []
    C = []
    for i in L:
        if i < 0:
            A.append(i)
        elif i == 0:
            B.append(i)
        else:
            C.append(i)
    
    LSEP = A + B + C
    return LSEP


L = [12,-3,4,0,-3,0,8,32,-12]
print(separation(L))