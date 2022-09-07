from biss import est_bissextile
from datetime import date

def date_est_valide(jour:int,mois:int,annee:int)->bool:
    """determine si une date est valide ou non

    Args:
        jour (int): numero du jour
        mois (int): numero du mois
        annee (int): numero de l'année

    Returns:
        (booleen): validité de la date
    """
    if jour > 31 or mois >12 or jour <= 0 or mois <= 0:
        return False
    elif mois == 4 or mois == 6 or mois == 9 or mois == 11:
        if jour>30:
            return False
        else:
            return True
    elif mois == 2:
        if jour>29:
            return False
        elif jour == 29:
            if est_bissextile(annee):
                return True
            else:
                return False
        else:
            return True
    elif jour>31:
        return False
    else:
        return True

#print(date_est_valide(29,2,2001))

def saisie_date_naissance()->date:
    """saisie de la date de naissance de l'utilisateur

    Returns:
        (date): date de naissance
    """
    a = int(input('entrez votre annee de naissance: '))
    m = int(input('entrez votre mois de naissance: '))
    j = int(input('entrez votre jour de naissance: '))
    if date_est_valide(j,m,a):
        return date(a,m,j)
    else:
        print('date invalide, veuillez réessayer')
        saisie_date_naissance()



def age(dat:date)->int:
    """retourne l'age de la personne, en fonction de sa date de naissance

    Args:
        dat (date): date de naissance

    Returns:
        age (int) : age de la personne
    """
    age = date.today().year - dat.year
    if date.today().month > dat.month:
        return age
    else:
        return age-1


def est_majeur(dat:date)->bool:
    """determine si une personne est majeure ou non

    Args:
        dat (date): date de naissance

    Returns:
        (booléen): True si majeur, False si mineur
    """
    if age(dat)<18:
        return False
    else:
        return True
        
def test_acces()->str:
    """autorise ou non un accès selon si la personne est majeure ou non

    Returns:
        (string): accès accepté ou refusé
    """
    dat = saisie_date_naissance()
    if est_majeur(dat):
        return 'accès autorisé'
    else: 
        return 'accès refusé'
print(test_acces())
