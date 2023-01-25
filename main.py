# Love Letter #

import random
from Class import *

# Intantiation de toutes les différentes cartes
carte1=Carte("Espionne",2,0,100)
carte2=Carte("Garde",6,1,80)
carte3=Carte("Prêtre",2,2,90)
carte4=Carte("Baron",2,3,50)
carte5=Carte("Servante",2,4,70)
carte6=Carte("Prince",2,5,60)
carte7=Carte("Chancelier",2,6,40)
carte8=Carte("Roi",1,7,30)
carte9=Carte("Comtesse",1,8,20)
carte10=Carte("Princesse",1,9,0) 

# Création des 2 joueurs
J1 = Joueur()
IA = Joueur()

# Joueur restant de la manche
joueur_restant = [J1, IA]

# Deck avec toutes les cartes
deck = [carte1, carte2, carte3, carte4, carte5, carte6, carte7, carte8, carte9, carte10]
# Deck contenant la non connaisance de l'IA (si '1' (ou plus) c'est qu'il sait que la carte est encore en jeu mais ne sais pas où)
deckIA = [x.nb_carte for x in deck]
# Deck de cartes contenant les cartes retirées du jeu en début de partie
cartes_retirees = []
# Tableau de probabilité des cartes que peux avoir le joueur 1 en main
prob_pioche_J1 = [0,0,0,0,0,0,0,0,0,0]
# Si grâce à un prètre l'IA sait la carte de l'adversaire, elle sera ajouté dans ce tableau
main_adversaire = []
# On ne retient que les cartes avec les meilleures proba
meilleures_cartes = [0,0,0,0,0,0,0,0,0,0]
# Si on connait la carte de l'IA grâce à un prêtre
main_IA = [] 

# Reset d'une manche
def Reset():
    carte1.nb_carte = 2
    carte2.nb_carte = 6
    carte3.nb_carte = 2
    carte4.nb_carte = 2
    carte5.nb_carte = 2
    carte6.nb_carte = 2
    carte7.nb_carte = 2
    carte8.nb_carte = 1
    carte9.nb_carte = 1
    carte10.nb_carte = 1
    cartes_retirees[:] = []
    J1.main[:] = []
    IA.main[:] = []
    J1.defausse[:] = []
    IA.defausse[:] = []
    J1.elimine = False
    IA.elimine = False
    J1.immune = False
    IA.immune = False
    deck = [carte1, carte2, carte3, carte4, carte5, carte6, carte7, carte8, carte9, carte10]
    deckIA[:] = [x.nb_carte for x in deck]
    main_adversaire[:] = []
    main_IA[:] = []

# Définition pour piocher une carte
def Pioche(deck):
    x = random.choice(deck)
    while x.nb_carte == 0:
        x = random.choice(deck)
    x.nb_carte -= 1
    return x

# Définition pour compter le nombre de cartes restantes dans le deck
def Compter_carte(deck):
    i = 0
    nb_carte_total = 0
    while i < len(deck):
        nb_carte_total += deck[i].nb_carte
        i += 1
    return nb_carte_total

# Définition pour afficher la main du joueur 'i' en format liste
def Main_Joueur(i):
    main = [x.nom for x in joueur_restant[i].main]
    print("Main du joueur " + str(i + 1) + " : " + str(main))

# Définition pour compter le nombre de carte dans la main du joueur 'i'
def Nb_carte_main(i):
    return len(joueur_restant[i].main) - 1

# Définition pour jeter une carte de la main du joueur 'i'
def Jeter(j):
    # Si c'est au joueur 1 de jeter sa carte
    print("La carte posé est : " + str(J1.main[j].nom))

    # Suppression de la carte de sa main et active son effet
    J1.defausse.append(J1.main[j])
    del J1.main[j]

    # Permet de supprimer un possibilité de carte dans le deckIA si c'est le joueur 1 qui se deffausse avec un cas spécifique si nous savions sa carte auparavent 
    if len(main_adversaire)>0 and J1.defausse[-1] == main_adversaire[-1]:
        deckIA[J1.defausse[-1].valeur] += 1
        del(main_adversaire[-1])
    else:
        deckIA[J1.defausse[-1].valeur] -= 1

# Si c'est à l'IA de jeter une carte
def Jeter_IA():
    # Vérification avec l'effet de la Comtesse
    Comtesse(1)
    if len(IA.main) == 2:
        jeter = choix_meilleur_coup()
        print("La carte posé est : " + str(IA.main[jeter].nom))

        # Suppression de la carte de sa main et active son effet
        IA.defausse.append(IA.main[jeter])
        del IA.main[jeter]

        if len(main_IA) > 0 and IA.defausse[-1] == main_IA[-1]:
            del(main_IA[-1])

# Définition pour savoir qui remporte la manche
def QuiGagne():
    if Compter_carte(deck) == 0:
        print("Il n'y a plus de carte dans le deck !")
        if J1.main[0].valeur > IA.main[0].valeur:
            J1gagne()
        elif IA.main[0].valeur > J1.main[0].valeur:
            IAgagne()
        else:
            valeurJ1 = 0
            valeurIA = 0
            i = 0
            j = 0
            while i < len(J1.defausse) - 1:
                valeurJ1 += J1.defausse[i].valeur
                i += 1
            while j < len(IA.defausse) - 1:
                valeurIA += IA.defausse[j].valeur
                j += 1
            if valeurJ1 > valeurIA:
                J1gagne()
            else:
                IAgagne()
    else:
        if J1.elimine == True:
            IAgagne()
        else:
            J1gagne()

# Définition si le joueur 1 gagne
def J1gagne():
    print("Le joueur 1 gagne 1 point de faveur !")
    J1.nb_faveur += 1

# Définition si l'IA gagne
def IAgagne():
    print("Le joueur 2 gagne 1 point de faveur !")
    IA.nb_faveur += 1

# Définiton des effets pour chaque cartes
# Gagne 1 pt de faveur si il n'y a qu'une seule carte en jeu
def Espionne():
    if carte1 in cartes_retirees:
        if carte1 in J1.defausse:
            J1gagne()
        else:
            IAgagne()

# Permet de savoirla carte del'adversaire
def Pretre(i):
    print("\nVoici la main de votre adversaire :")
    if i == 0:
        Main_Joueur(1)
        if len(main_IA) > 0:
            del(main_IA[0])
        main_IA.append(IA.main[-1])
    else:
        # Attribut la carte de l'adversaire dans 'main_adversaire' pour la sauvegarder
        Main_Joueur(0)
        deckIA[J1.main[-1].valeur] -= 1
        if len(main_adversaire) > 0:
            del(main_adversaire[0])
        main_adversaire.append(J1.main[-1])

# Permet de comparer les cartes des deux joueurs et celui avec la plus haute valeur l'emporte
def Baron(i):
    Main_Joueur(0)
    Main_Joueur(1)
    if J1.main[0].valeur > IA.main[0].valeur:
        IA.elimine = True
        print("Le joueur 2 est éliminé !")
    elif IA.main[0].valeur > J1.main[0].valeur:
        J1.elimine = True
        print("Le joueur 1 est éliminé !")
    else:
        if i == 0:
            if len(main_IA) > 0:
                del(main_IA[0])
            main_IA.append(IA.main[-1])
        else:
            deckIA[J1.main[-1].valeur] -= 1
            if len(main_adversaire) > 0:
                del(main_adversaire[0])
            main_adversaire.append(J1.main[-1])
        print("Egalité ! La partie continue")

# Le joueur la posant est immunisé jusqu'au prochain tour
def Servante(i):
    joueur_restant[i].immune = True
    print("Le joueur " + str(i + 1) + " est immunisé jusqu'à qu'il rejoue !")

# Echange sa carte avec l'adversaire
def Roi():
    if J1.immune == False and IA.immune == False:
        print("\nVous échangez votre carte avec celle de votre adversaire.")
        Main_Joueur(0)
        Main_Joueur(1)
        J1.main.append(IA.main[0])
        IA.main.append(J1.main[0])
        del J1.main[0]
        del IA.main[0]
        print("\nVoici les nouvelles mains :")
        Main_Joueur(0)
        Main_Joueur(1)
        if len(main_adversaire) > 0:
            main_adversaire[0] = J1.main[0]
        else :
            main_adversaire.append(J1.main[0])
        # Supprime et rajoute la possibilité de la carte échangée et celle prise dans deckIA
        deckIA[IA.main[0].valeur] -= 1
        deckIA[J1.main[0].valeur] += 1

# Doit être absolument joué si il y a un Roi ou un Prince dans la main
def Comtesse(i):
    if carte9 in joueur_restant[i].main and (carte6 in joueur_restant[i].main or carte8 in joueur_restant[i].main):
        print("Vous devez jeter la carte 'Comtesse' de votre main !\nLa carte posé est : Comtesse")
        joueur_restant[i].main.remove(carte9)
        joueur_restant[i].defausse.append(carte9)
        if len(main_adversaire) > 0 and i == 0:
            if main_adversaire[0] != carte9:
                deckIA[carte9.valeur] -= 1

# Si posé = perdu
def Princesse(i):
    if i == 0:
        J1.elimine = True
    else:
        IA.elimine = True
    print("Le joueur " + str(i + 1) + " est éliminé de la manche !")

# Mise en place des affichages de l'effet de chaques cartes
def desc_effet(i):
    if i == 0:
        a = "Si une seule des 2 cartes espionne est en jeu,"
        b = "Vous gagnez un point faveur."
        c = ""
    elif i == 1:
        a = "Nommez une carte (sauf Garde)."
        b = "Si c'est la carte que votre adversaire a"
        c = "en main, alors il est éliminé de la manche."
    elif i == 2:
        a = "Vous regardez la carte de l'adversaire."
        b = ""
        c = ""
    elif i == 3:
        a = "Les deux joueurs se montrent leur carte :"
        b = "le joueur ayant la carte de plus haute valeur gagne"
        c = "la manche. Si égales, alors la partie continue."
    elif i == 4:
        a = "Vous ne pouvez pas subir l'effet d'autres"
        b = "cartes pendant un tour, jusqu'à ce que vous rejouez."
        c = ""
    elif i == 5:
        a = "Cliquer sur le joueur qui doit se défausser de sa"
        b = "carte et qui doit en pioche une autre immédiatement."
        c = ""
    elif i == 6:
        a = "Vous piochez 2 cartes supplémentaire en plus de"
        b = "celle que vous avez dans les mains, et vous remetez"
        c = "2 cartes de votre choix dans le bas de la pioche."
    elif i == 7:
        a = "Vous échangez votre carte avec celle de"
        b = "votre adversaire."
        c = ""
    elif i == 8:
        a = "Doit obligatoirement être jouée si vous possèdez"
        b = "aussi en main un Prince ou un Roi."
        c = ""
    else:
        a = "Si vous la défaussée alors vous perdez"
        b = "automatiquement la manche."
        c = ""
    return a, b, c

# Statistique pour determiner la carte la plus probable de J1
def stats():
    i = 0
    total = 0
    cartes_inconnues = 0
    prob_1_carte = 0
    # Compte le nb de cartes inconnues
    while i < 10:
        cartes_inconnues += deckIA[i]
        i += 1
    i = 0
    prob_1_carte = "{0:.3f}".format(1/cartes_inconnues*100)
    # Création du tableau de prob
    while i < 10:
        prob_pioche_J1[i] = deckIA[i] / (cartes_inconnues) * 100
        total += prob_pioche_J1[i]
        if float(prob_pioche_J1[i]) > float(prob_1_carte) + 1:
            meilleures_cartes[i] = 1
        else:
            meilleures_cartes[i] = 0
        i += 1
    mainpossible = ["{0:.3f}".format(x) for x in prob_pioche_J1]
    
# Définition du meilleur coup à faire pour l'IA
def choix_meilleur_coup():
    choix_IA = 0
    # En fonction de si on sait ou non la carte de l'adversaire
    if len(main_adversaire) == 0:
        if J1.defausse[-1] == carte3 and IA.main[0].pourcentage >= IA.main[1].pourcentage:
            choix_IA = 0
        else:
            if IA.main[0].pourcentage > IA.main[1].pourcentage :
                choix_IA = 0
            else:
                choix_IA = 1
    # Si on connait la carte de l'adversaire
    else :
        if carte2 in IA.main and carte2 not in main_adversaire:
            choix_IA = IA.main.index(carte2)
        elif carte10 in main_adversaire and carte4 in IA.main:
            if IA.main[1] == carte4:
                choix_IA = 0
            else:
                choix_IA = 1
        elif carte3 in J1.defausse and carte2 in main_adversaire:
            choix_IA = 0
        elif carte4 in main_adversaire:
            if IA.main[0].valeur < 3:
                choix_IA = 1
            else:
                choix_IA = 0        
        else:
            if IA.main[0].pourcentage > IA.main[1].pourcentage:
                choix_IA = 0
            else:
                choix_IA = 1
    print(choix_IA)
    return choix_IA

# Donne la carte la plus probable aléatoirement parmi les probabilitées réduites
def carte_probable(meilleures_cartes):
    choix = -1
    # Compte le nombre de cartes avec les proba les plus hautes
    choix_possible = tab_cartes_probables(meilleures_cartes)
    print(choix_possible)
    # Choisit une carte aléatoirement parmi le deck de cartes réduit
    if len(choix_possible) > 0:
        choix = random.choice(choix_possible)
    else:
        liste1 = [0,2,3,4,5,6,7,8,9]
        choix = random.choice(liste1)
    print(choix)
    return choix

# Retourner dans un tableau l'index des cartes avec la plus haute probabilitée d'apparition
def tab_cartes_probables(meilleures_cartes):
    choix_possible = []
    i = 0
    while i < 10 :
        if IA.defausse[-1] == carte2:
            if meilleures_cartes[i] == 1 and i != 1:
                # Ajoute l'index des cartes retenues 
                choix_possible.append(i)
        else :
            if meilleures_cartes[i] == 1:
                # Ajoute l'index des cartes retenues 
                choix_possible.append(i)
        i += 1
    return choix_possible