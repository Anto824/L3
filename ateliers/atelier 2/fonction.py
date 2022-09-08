from iteration_utilities import duplicates
from iteration_utilities import unique_everseen




def est_surjective(X,Y):
    return len(X) == len(Y)






L = [1,2,3,4,5,1,2]
M = [1,4,3,8,9,1,0]
n = []


def unique(L):
	return list(unique_everseen(duplicates(L)))



def test(L,i):
    m = []
    for index, elem in enumerate(L):
        if elem == i:
            m.append(index)
    return m

def est_injective(X,Y):
    a = unique(X)
    for i in a:
        n.append(test(X,i))

    z = []
    for k in range(len(n)):
        f = []
        for t in n[k]:
            f.append(Y[t])
    
        if(len(set(f))==1):
            z.append(True)
        else:
            z.append(False)

    if False in z:
        return False
    else:
        return True

L = [1,2,3,4,5,1,2]
M = [1,4,3,8,9,1,4]

print(est_injective(L,M))


def est_bijective(X,Y):
    return est_injective(X,Y) and est_surjective(X,Y)
        





def listehisto(X):
    a = max(X)
    h = []
    for i in range(a+1):
        h.append(X.count(i))
    return h







def histo(h):
    print("")
    H = max(h)
    while True:
        if H == 0:
            break
        for i in h:
            if i>=H:
                print("#    ",end="")
            else:
                print("     ",end="")
        H-=1
        print('')
    for i in range (len(h)):
        print("i    ", end="")



