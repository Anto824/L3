


def position(L,e):
    for i in range(len(L)):
        if L[i]==e:
            return i
    return -1

def position1(L,e):
    n = 0
    while n<len(L):
        if L[n]==e:
            return n
        n+=1
    return -1

def nb_occurences(L,e):
    x = 0
    for i in L:
        if i==e:
            x+=1
    return x

def est_triee(L): #meilleure version
    for i in range(1,len(L)):
        if L[i]<L[i-1]:
            return False
    return True

def est_triee1(L):
    i = 1
    while i<len(L):
        if L[i]<L[i-1]:
            return False
        i+=1
    return True

def position_tri(L,e):
    a = 0
    b = len(L) - 1
    while a <= b:
        m = (a + b) // 2
        if L[m] == e:
            # on a trouvé e
            return m
        elif L[m] < e:
            a = m + 1
        else:
            b = m - 1
    # on a a > b
    return False


def a_repetitions(L):
    T=[]
    for i in L:
        if i in T:
            return True
        else:
            T.append(i)
    return False

        