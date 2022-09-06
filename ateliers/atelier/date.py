from biss import est_bissextile
import time
from datetime import date

def date_est_valide(jour,mois,année):
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
            if est_bissextile(année):
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

def saisie_date_naissance():
    a = int(input('entrez votre année de naissance: '))
    m = int(input('entrez votre mois de naissance: '))
    j = int(input('entrez votre jour de naissance: '))
    if date_est_valide(j,m,a):
        return date(a,m,j)
    else:
        print('date invalide, veuillez réessayer')
        saisie_date_naissance()

def age(dat):
    age = date.today().year - dat.year
    if date.today().month > dat.month:
        return age
    else:
        return age-1
def est_majeur(dat):
    if age(dat)<18:
        return False
    else:
        return True

def test_acces():
    dat = saisie_date_naissance()
    if est_majeur(dat):
        return 'accès autorisé'
    else: 
        return 'accès refusé'
print(test_acces())
