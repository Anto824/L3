import random


listeChoix = ['papier','pierre','ciseaux','puit']

def infosJoueurs()->list: #retourne le nombre de joueurs ainsi que leurs noms.
    """recupere les informations de/des joueur(s)

    Returns:
        (list) : tableau contenant les infos necessaires (solo ou multi, nom du joueur 1, nom du joueur 2)
    """
    solomulti=''
    while solomulti != 'O' and solomulti != 'N':
        if solomulti != '':
            print("Je n'ai pas compris votre réponse")
        solomulti = input("Voulez-vous jouer contre l'ordinateur (Max 5 parties) O/N ? " )
    if solomulti == 'O':
        nom1 = input("Quel est votre nom ? ")
        print("Bienvenu ",nom1, " nous allons jouer ensemble \n")
        nom2 = 'Machine'
    elif solomulti == 'N':
        nom1 = input("Quel est votre nom ? ")
        print("Bienvenue ",nom1, " nous allons jouer ensemble")
        nom2 = input("Quel est le nom du deuxième joueur ?")
        print("Bienvenue ",nom2, " nous allons jouer ensemble \n")
    return solomulti,nom1,nom2



def verif(nom:str)->str:
    """verifie le choix du joueur

    Args:
        nom (string): choix du joueur pour la manche

    Returns:
        choix (string): choix verifie du joueur
    """
    while True:
        choix = input('{nom} faîtes votre choix parmi (pierre, papier, ciseaux, puit): '.format(nom=nom))
        if choix not in listeChoix:
            print('nom incorrect')
        else:
            return choix



def partie()->None:
    """lance la partie
    """
    tableauInfos = infosJoueurs() #recuperation infos joueurs.
    solomulti = tableauInfos[0]
    nom1 = tableauInfos[1]
    nom2 = tableauInfos[2]
    jouer = True
    score1 = 0
    nbParties = 0
    score2 = 0
    while jouer == True:
        choix = []
        nbParties += 1 
        choixJ1 = verif(nom1)
        if solomulti == 'O': #choisit aléatoirement un choix si il n'y a qu'un joueur.
            choixJ2 = random.choice(listeChoix)
        else: #sinon verifie l'entrée comme pour le joueur 1.
            choixJ2 = verif(nom2)
        print("Si on récapitule :",nom1, choixJ1, "et", nom2, choixJ2,"\n") #On affiche les choix de chacun
        choix.append(choixJ1)
        choix.append(choixJ2)
        if choixJ1 == choixJ2:
            gagnantManche = 2
            ggManche = 'aucun de vous deux, vous etes ex aequo'
        elif 'ciseaux' in choix:
            if 'puit' in choix:
                gagnantManche = choix.index('puit')
            elif 'pierre' in choix:
                gagnantManche = choix.index('pierre')
            else:
                gagnantManche = choix.index('ciseaux')
        elif 'papier' in choix:
            if 'pierre' in choix or 'puit' in choix:
                gagnantManche = choix.index('papier')
        else:
            gagnantManche = choix.index('puit')
        if gagnantManche == 0:
            score1+=1
            ggManche = nom1
        elif gagnantManche == 1:
            score2+=1
            ggManche = nom2
        print("le gagnant est",ggManche)
        print("Les scores à l'issue de cette manche sont donc",nom1, score1, "et", nom2, score2, "\n")
        if nbParties==5: 
            continuer = input("Souhaitez vous refaire une partie {} contre {} ? (O/N) ".format(nom1,nom2))#On propose de continuer ou de s'arrêter
            if continuer == 'O':
                nbParties = 0
            elif continuer == 'N':
                jouer = False
            else:
                jouer = True
                print("Vous ne répondez pas à la question, on continue ")
                nbParties = 0
    if jouer == False : #arret de la boucle infinie du jeu. 
        print("Merci d'avoir joué ! A bientôt")



partie() #lancement partie.