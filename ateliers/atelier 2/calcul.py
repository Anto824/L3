


def sommefor(L:list)->int: #version plus adaptée.
    x = 0
    for i in L:
        x+=i
    return x


def sommefor2(L):
    x = 0
    for i in range (len(L)):
        x+=L[i]
    return x


def sommewhile(L):
    x = 0
    n = 0
    while n<len(L):
        x+=L[n]
        n+=1
    return x


def test_exercice1 (): 
    print("TEST SOMME")
    #test liste vide
    print("Test liste vide : ", sommefor([])) #test somme 11111
    S=[1,10,100, 1000,10000]
    print("Test somme 1111 : ", sommefor(S))

#test_exercice1()
#L = [2,2,4,1,1]

#print(sommefor(L))
#print(sommefor2(L))
#print(sommewhile(L))


def moyenne(L):
    x = 0
    for i in L:
        x+=i
    x = x/len(L)
    return x


#L = [10,10,15,20,20]
#print(moyenne(L))

def nb_sup(L,e):
    x = 0
    for i in L:
        if i > e:
            x+=1
    return x

def nb_sup1(L,e):
    x = 0
    for i in range(len(L)):
        if L[i]>e:
            x+=1
    return x


def moy_sup(L,e):
    x = 0
    n = 0
    for i in L:
        x+=i
        n+=1
    x = x/n
    return x


def val_max(L):
    x = -99999999999999
    for i in L:
        if i>x:
            x = i
    return x



def ind_max(L):
    x=-9999999999999
    for i in range (len(L)):
        if L[i]>x:
            x = L[i]
            n = i
    return n




