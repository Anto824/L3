import random


listeChoix = ['papier','pierre','ciseaux','puit'] #variable globale car utilisée dans plusieurs fonctions, c'est la seule du fichier

def infosJoueurs()->list: #retourne le nombre de joueurs ainsi que leurs noms.
    """recupere les informations de/des joueur(s)

    Returns:
        (list) : tableau contenant les infos necessaires (solo ou multi, nom du joueur 1, nom du joueur 2)
    """
    solomulti='' #initialisation pour pouvoir entrer dans la boucle while
    while solomulti != 'O' and solomulti != 'N': #tant que l'entrée n'est pas valide, on ne sort pas de la boucle
        if solomulti != '': #pour eviter d'avoir ce message avant d'avoir fait la premiere entrée 
            print("Je n'ai pas compris votre réponse")
        solomulti = input("Voulez-vous jouer contre l'ordinateur (Max 5 parties) O/N ? " ) #recuperation du mode de jeu souhaité
    if solomulti == 'O': #si le mode demandé est solo
        nom1 = input("Quel est votre nom ? ")
        print("Bienvenu ",nom1, " nous allons jouer ensemble \n")
        nom2 = 'Machine'
    elif solomulti == 'N': #sinon, le mode de jeu est multijoueur
        nom1 = input("Quel est votre nom ? ")
        print("Bienvenue ",nom1, " nous allons jouer ensemble")
        nom2 = input("Quel est le nom du deuxième joueur ?")
        print("Bienvenue ",nom2, " nous allons jouer ensemble \n")
    return solomulti,nom1,nom2 #return dans un tableau le mode de jeu et les deux noms



def verif(nom:str)->str:
    """verifie le choix du joueur

    Args:
        nom (string): choix du joueur pour la manche

    Returns:
        choix (string): choix verifie du joueur
    """
    while True: #la boucle s'arretera seule avec le return, donc il n'y a pas besoin d'une condition qui s'arrete à un moment
        choix = input('{nom} faîtes votre choix parmi (pierre, papier, ciseaux, puit): '.format(nom=nom))
        if choix not in listeChoix: #si le choix n'est pas dans la liste des choix possibles, on ne sort pas de la boucle et on redemande au joueur.
            print('nom incorrect')
        else:
            return choix #return le choix et sort de la boucle infinie while True



def partie()->None:
    """lance la partie
    """

    ############ recuperations et initialisations #################
    tableauInfos = infosJoueurs() #recuperation infos joueurs.
    solomulti = tableauInfos[0]
    nom1 = tableauInfos[1]
    nom2 = tableauInfos[2]
    jouer = True
    score1 = 0
    nbParties = 0
    score2 = 0
    while jouer == True: #lancement de la partie, et s'arretera à la fin 
        choix = []       #initialisation du tableau
        nbParties += 1   
        choixJ1 = verif(nom1) #recuperation choix du joueur 1
        if solomulti == 'O': #choisit aléatoirement un choix si il n'y a qu'un joueur.
            choixJ2 = random.choice(listeChoix) #choisit aleatoirement dans la liste de choix possibles dans le cas où le mode de jeu est solo contre l'ordinateur
        else: #sinon verifie l'entrée comme pour le joueur 1.
            choixJ2 = verif(nom2)
        print("Si on récapitule :",nom1, choixJ1, "et", nom2, choixJ2,"\n") #On affiche les choix de chacun
        choix.append(choixJ1) #ajout dans le tableau des deux choix
        choix.append(choixJ2)
        if choixJ1 == choixJ2: #si les choix sont identiques, n'assigne aucun gagnant
            gagnantManche = 2  #0 = joueur 1 gagnant, 1 = joueur 2 gagnant, autre = aucun gagnant
            ggManche = 'aucun de vous deux, vous etes ex aequo'
        elif 'ciseaux' in choix: #on traite les cas où un des deux joueurs a prit les ciseaux 
            if 'puit' in choix:
                gagnantManche = choix.index('puit') #on recupere le gagnant grace a l'emplacement du puit dans le tableau des choix des joueurs 
            elif 'pierre' in choix:
                gagnantManche = choix.index('pierre')
            else:
                gagnantManche = choix.index('ciseaux')
        elif 'papier' in choix:
            if 'pierre' in choix or 'puit' in choix: #la feuille gagne contre les deux donc le resultat est le meme
                gagnantManche = choix.index('papier') #la verification de ces deux cas suffit car nous avons deja verifié si les deux choix sont identiques, ou si l'autre choix est ciseaux.
        else:
            gagnantManche = choix.index('puit') #dernier cas possible, un joueur a prit la pierre, l'autre le puit, le puit gagne donc.
        if gagnantManche == 0: #attribution des scores
            score1+=1
            ggManche = nom1
        elif gagnantManche == 1:
            score2+=1
            ggManche = nom2
        print("le gagnant est",ggManche)
        print("Les scores à l'issue de cette manche sont donc",nom1, score1, "et", nom2, score2, "\n")
        if nbParties==5: #continuer la partie ?
            continuer = input("Souhaitez vous refaire une partie {} contre {} ? (O/N) ".format(nom1,nom2))#On propose de continuer ou de s'arrêter
            if continuer == 'O':
                nbParties = 0 #relance la boucle pour 5 tours minimum.
            elif continuer == 'N':
                jouer = False #arrete la boucle de jeu 
            else:
                jouer = True
                print("Vous ne répondez pas à la question, on continue ")
                nbParties = 0
    if jouer == False : #arret de la boucle infinie du jeu. 
        print("Merci d'avoir joué ! A bientôt")



partie() #lancement partie.