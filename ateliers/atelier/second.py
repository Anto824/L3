import math

def discriminant(a:int,b:int,c:int)->int:
    """calcule le determinant d'un polynome du second degré

    Args:
        a (int): coefficient a
        b (int): coefficient b
        c (int): coefficient c

    Returns:
        d (int): determinant du polynome
    """
    d = b**2
    e = 4*a*c
    d-=e
    return d

def racine_unique(a:int,b:int)->int:
    """donne la solution de l'equation y=0 du polynome du second degré, dans le cas où le determinant est egal à 0

    Args:
        a (int): coefficient a
        b (int): coefficient b

    Returns:
        d (int): absisse solution
    """
    d = -b/(2*a)
    return d

def racine_double(a:int,b:int,delta:float,num:int)->float:
    """donne une des deux solutions de l'equation y=0

    Args:
        a (int): coefficient a
        b (int): coefficient b
        delta (float)): determinant
        num (int): 1ere ou 2e solution à trouver

    Returns:
        rac (float): solution de y=0
    """
    if delta<0:
        print('delta negatif, aucune solution réelle')
    elif num == 1:
        rac = -b-math.sqrt(delta)
        rac = rac/2*a
    else:
        rac = -b+math.sqrt(delta)
        rac = rac/2*a
    return rac

def str_equation(a:int,b:int,c:int)->str:
    """donne l'equation du second degre complete en fonction des coefficients

    Args:
        a (int): coefficient a
        b (int): coefficient b
        c (int): coefficient c

    Returns:
        equ (string): equation
    """
    equ = ''
    if a == -1:
        a = '-'
    elif a == 1:
        a = ''
    if a!=0:
        equ = equ+str(a)
        equ = equ+'x2'
    if b == -1:
        b = str('-')                    #on ajoute a la chainne de caractères tous les elements en faisant attention aux cas particuliers.
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


def solution_equation(a:int,b:int,c:int)->str:
    """donne toutes les solutions réelles d'une equation du second degré

    Args:
        a (int): coefficient a
        b (int): coefficient b
        c (int): coefficient c

    Returns:
        (string) : solutions de l'equation y=0
    """
    delta = discriminant(a,b,c)
    if delta==0:
        return "solution unique de l'equation" +str_equation(a,b,c) + ": " + str(racine_unique(a,b))
    elif delta>0:
        return "deux solutions pour l'equation  " + str_equation(a,b,c) + "\n x=" + str(racine_double(a,b,delta,1)) + "\n x=" + str(racine_double(a,b,delta,2))
    else:
        return "aucune solution pour l'equation " + str_equation(a,b,c)


def test_sec(tab:list)->None:
    """teste plusieurs equations

    Args:
        tab (list): tableau de tableaux d'entiers
    """
    for i in tab:
        print(solution_equation(i[0],i[1],i[2]))




