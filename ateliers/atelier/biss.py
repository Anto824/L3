def est_bissextile(an:int)->bool:
    """verifie si l'année en entrée est bissextile

    Args:
        an (int): année à tester

    Returns:
        booleen: bissextile ou non 
    """
    if(an%4==0 and an%100!=0 or an%400==0):
        return True
    else:
        return False


def test_biss(tab:list)->None:
    """teste differentes année

    Args:
        tab (list): tableau d'entiers
    """
    for i in tab: #parcours le tableau d'entrée
        print(est_bissextile(i))


#tab = [2003,2009,2004,1997,2000]
#test_biss(tab)
#print(est_bissextile(2000))

