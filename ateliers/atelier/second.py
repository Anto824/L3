import math

def discriminant(a,b,c):
    d = b**2
    e = 4*a*c
    d-=e
    return d


def racine_unique(a,b):
    d = -b/(2*a)
    return d

def racine_double(a,b,delta,num):
    if num == 1:
        rac = -b-math.sqrt(delta)
        rac = rac/2*a
    else:
        rac = -b+math.sqrt(delta)
        rac = rac/2*a
    return rac

def str_equation(a,b,c):
    equ = ''
    if a == -1:
        a = '-'
    elif a == 1:
        a = ''
    if a!=0:
        equ = equ+str(a)
        equ = equ+'x2'
    if b == -1:
        b = str('-')
    elif b<0:
        equ = equ+str(b)
        equ = equ+'x'
    elif b>0:
        if equ!='':
            equ = equ+'+'
            equ = equ+str(b)
            equ = equ+'x'
        else:
            equ = equ+str(b)
            equ = equ+'x'
    if c<0:
        equ = equ+str(c)
    elif c>0:
        equ = equ+'+'
        equ = equ+str(c)
    equ = equ+'=0'
    return equ


def solution_equation(a,b,c):
    delta = discriminant(a,b,c)
    if delta==0:
        return "solution unique de l'equation" +str_equation(a,b,c) + ": " + str(racine_unique(a,b))
    elif delta>0:
        return "deux solutions pour l'equation  " + str_equation(a,b,c) + "\n x=" + str(racine_double(a,b,delta,1)) + "\n x=" + str(racine_double(a,b,delta,2))
    else:
        return "aucune solution pour l'equation " + str_equation(a,b,c)
def test_sec(tab:list):
    for i in tab:
        print(solution_equation(i[0],i[1],i[2]))




