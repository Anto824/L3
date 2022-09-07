DENUTRITION = 16.5
MAIGREUR = 18.5
NORMALE = 25
SURPOIDS = 30
OBESITE_MOD = 35
OBESITE_SEV = 40




def message_imc(imc:float)->str:
    """donne une signification de l'imc d'une personne

    Args:
        imc (float): indice de masse corporelle d'une personne

    Returns:
        msg (String): message correspondant à la signification trouvée
    """
    if imc<DENUTRITION:
        msg = 'dénutrition ou famine'
    elif imc<MAIGREUR:
        msg = 'maigreur'
    elif imc<NORMALE:
        msg = 'corpulence normale'
    elif imc<SURPOIDS:
        msg = 'surpoids'
    elif imc<OBESITE_MOD:
        msg = 'obésité modérée'
    elif imc<OBESITE_SEV:
        msg = 'obésité sévère'
    else:
        msg = 'obésité morbide'
    return msg

def test_imc(tab:list)->None:
    """teste plusieurs valeurs d'imc pour la fonction message_imc

    Args:
        tab (list): tableau d'entiers  contenant les imc à tester
    """
    for i in tab:
        print(message_imc(i))


tab = [12,45,32,29,25,23]
test_imc(tab)