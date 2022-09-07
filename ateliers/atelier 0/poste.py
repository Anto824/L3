


def typ()->int:
    """demande l'entrée du type de lettre, et verifie sa validité

    Returns:
        ind (int): emplacement du type de lettre dans le tableau
    """
    lst = ['verte','prioritaire','eco']
    t=input("entrez votre type de lettre (verte, prioritaire ou eco)")
    if t not in lst: #si la reponse n'est pas dans la liste, on entre dans un boucle jusqu'a ce que l'entrée soit correcte.
        c = True
        while c:
            t = input("erreur, veuillez entrer votre type de lettre (verte, prioritaire ou eco)")
            if t in lst: #stoppe la boucle quand l'entrée est correcte.
                c = False
    ind=lst.index(t) #renvoie l'emplacement du type entré dans la liste lst. l'emplacement sera utilisé plus tard pour parcourir le tableau des prix au bon endroit.
    return ind




def prix()->None:
    """affiche le prix à payer
    """
    p = [[[20,1.16],[100,2.32],[250,4],[500,6],[1000,7.5],[3000,10.5]] #tableau des prix en fonction du poids max lettre verte
,[[20,1.43],[100,2.86],[250,5.26],[500,7.89],[3000,11.44]],            #pareil pour lettre prioritaire
[[20,1.14],[100,2.28],[250,3.92]],                                     #lettre eco-pli
[3000,3000,250]]                                                       #poids maximum des differents type de lettre
    t = typ()
    poids = float(input('entrez le poids de votre lettre'))
    if poids>p[3][t]: #verifie dans le dernier tableau du tableau p
        print("votre lettre est trop lourde pour ce type d'envoi, veuillez reessayer")
    else:
        print("votre lettre n'est pas trop lourde pour le type d'envoi selectionné.")
        for n in p[t]:      #parcours le tableau correspondant au type d'envoi
            if poids<n[0]:
                pri = n[1]
                break       #arrete dès que le poids de la lettre est inferieur à celui d'un pallier de prix.
        print('prix à regler: ',pri,'€')



prix()

