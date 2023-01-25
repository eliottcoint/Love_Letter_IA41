import pygame
import time
from pygame.locals import *
from main import *
from pathlib import Path
from Class import *

pygame.init()
pygame.font.init()

# Initialise screen
screen = pygame.display.set_mode((800, 565))
pygame.display.set_caption('LOVE LETTER - MENU')

# Initialise  icone
pygame_icon = pygame.image.load("Projet/Images/icone.png")
pygame.display.set_icon(pygame_icon)

# Fill background
background = pygame.image.load("Projet/Images/background.jpg").convert()
background = pygame.transform.scale(background, screen.get_size())

# Font
font_titre = pygame.font.SysFont("algerian", 52)
font_text = pygame.font.SysFont("algerian", 36)

# Text
titre = font_titre.render("LOVE LETTER", 1, (0, 0, 0))
t1 = font_text.render("JOUER", 1, (0, 0, 0))
t2 = font_text.render("REGLES", 1, (0, 0, 0))

# Mettre ces boutons dans la classe
# Display bouton's image on each text
bouton = pygame.image.load("Projet/Images/bouton.png").convert_alpha()
bouton = pygame.transform.scale(bouton, (180,76))
b1 = bouton.get_rect()
b1.centerx = background.get_rect().centerx
b1.centery = 300
b2 = bouton.get_rect()
b2.centerx = background.get_rect().centerx
b2.centery = 400

chemin_face_cachee = Path().cwd() / 'Projet/Images/images_cartes/face_cachee.png'
carte_face_cachee = pygame.image.load(chemin_face_cachee)
carte_face_cachee = pygame.transform.scale(carte_face_cachee, (600, 800)) #redimensionner l'image pour avoir la même taille que les autres

# Placement du titre
titrepos = titre.get_rect()
titrepos.centerx = background.get_rect().centerx
titrepos.centery = 150

# Placement du textes pour les boutons
t1pos = t1.get_rect()
t1pos.centerx = b1.centerx
t1pos.centery = b1.centery
t2pos = t2.get_rect()
t2pos.centerx = b2.centerx
t2pos.centery = b2.centery

continuer = 1

# Vérification du bouton "X"
def game_event():
        global continuer
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

# Lancement du Jeu
def game():
        main()

# Création de l'affichage des règles
def regles():
    screen = pygame.display.set_mode((1067, 753))
    pygame.display.set_caption('LOVE LETTER - GAME')

    background = pygame.image.load("Projet/Images/background.jpg").convert()
    background = pygame.transform.scale(background, screen.get_size())

    font_effet = pygame.font.SysFont("Calibri", 20, True)

    t3 = font_text.render("JOUER", 1, (0, 0, 0))

    b3 = bouton.get_rect()
    b3.centerx = background.get_rect().centerx
    b3.centery = 700

    t3pos = t3.get_rect()
    t3pos.centerx = b3.centerx
    t3pos.centery = b3.centery

    i = 0
    while i < 10:
        a, b ,c = desc_effet(i)
        effet1_l1 = font_effet.render(str(deck[i].nom) + " : " + str(a) + " " + str(b), 1, (255, 255, 255))
        effet1_l1pos = effet1_l1.get_rect()
        effet1_l1pos.centerx = background.get_rect().centerx
        effet1_l1pos.centery = 80 + i * 60
        background.blit(effet1_l1, effet1_l1pos) 

        effet1_l2 = font_effet.render(str(c), 1, (255, 255, 255))
        effet1_l2pos = effet1_l2.get_rect()
        effet1_l2pos.centerx = background.get_rect().centerx
        effet1_l2pos.centery = 100 + i * 60
        background.blit(effet1_l2, effet1_l2pos)
        i += 1

    background.blit(bouton, b3)
    background.blit(t3, t3pos)
    screen.blit(background, (0, 0))

    global continuer
    while continuer:
        x, y = pygame.mouse.get_pos()
        pressed = pygame.mouse.get_pressed()
        collide_b3 = b3.collidepoint(x, y)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                continuer = 0
                exit()
            
        if pygame.mouse.get_focused():
            if collide_b3 and pressed[0]:
                game()
        pygame.display.flip()

# Vérification des appuis de la sourie
def menu_event():
    global continuer
    x, y = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed()
    collide_b1 = b1.collidepoint(x, y)
    collide_b2 = b2.collidepoint(x, y)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            continuer = 0
            exit()
        
    if pygame.mouse.get_focused():
        if collide_b1 and pressed[0]:
            game()
            
        elif collide_b2 and pressed[0]:
            regles()

# Création du menu
def home():
    background.blit(bouton, b1)
    background.blit(bouton, b2)
    background.blit(titre, titrepos)
    background.blit(t1, t1pos)
    background.blit(t2, t2pos)
    screen.blit(background, (0, 0))

    # Event loop
    while continuer:
        menu_event()
        pygame.display.flip()

# Mettre l'extension ".png"
def carte_en_png(carte):
    carte_png = carte + '.png'
    return carte_png

# Définition des "Boutons"
class Bouton():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False #initialisé l'état clicked

    def draw(self):
        action = False
        #position de la souris dans la fenetre
        pos = pygame.mouse.get_pos()

        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False: #0 est le click gauche
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        #draw button on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action

# Afficher la main du joueur 1
def afficher_mainJ1():
    x = 0
    y = 0
    z = 0

    # Chercher quels sont les cartes du joueur 1
    carte_J1_1 = J1.main[0].nom.lower()
    # Ajouter l'extension png
    carte_png_J1_1 = carte_en_png(carte_J1_1)
    # dDfinir le chemin en fonction de la carte
    chemin_J1carte1 = Path().cwd() / 'Projet' / 'Images' / 'images_cartes' / carte_png_J1_1 
    # Charger l'image
    J1_carte1 = pygame.image.load(chemin_J1carte1)
    # Transformer les images des cartes en bouton et les positionner dans la fenetre tout en les redimensionnant 0.95 x leur taille originale
    B_J1_carte1 = Bouton(355, 500, J1_carte1, 0.95)
    # La dessiner
    x = B_J1_carte1

    if len(J1.main) > 1:
        carte_J1_2 = J1.main[1].nom.lower()                 
        carte_png_J1_2 = carte_en_png(carte_J1_2)
        chemin_J1carte2 = Path().cwd() / 'Projet' / 'Images' / 'images_cartes' / carte_png_J1_2                  
        J1_carte2 = pygame.image.load(chemin_J1carte2)
        B_J1_carte2 = Bouton(545,500, J1_carte2, 0.95)
        y = B_J1_carte2

        if len(J1.main) > 2:
            carte_J1_3 = J1.main[2].nom.lower()                 
            carte_png_J1_3 = carte_en_png(carte_J1_3)
            chemin_J1carte3 = Path().cwd() / 'Projet' / 'Images' / 'images_cartes' / carte_png_J1_3                 
            J1_carte3 = pygame.image.load(chemin_J1carte3)
            B_J1_carte3 = Bouton(735,500, J1_carte3, 0.95)
            z = B_J1_carte3

    return x, y, z

# Afficher la main du joueur 2
def afficher_mainJ2():
    x = 0
    y = 0

    # Si on connait la carte de l'adversaire ou non
    if len(main_IA) == 0:
        B_IA_carte1 = Bouton(425, 10, carte_face_cachee, 0.3)
    elif len(main_IA) > 0 or J1.defausse[-1] == carte4 or IA.defausse[-1] == carte4:
        carte_IA_1 = IA.main[0].nom.lower()                 
        carte_png_IA_1 = carte_en_png(carte_IA_1)
        chemin_IAcarte1 = Path().cwd() / 'Projet' / 'Images' / 'images_cartes' / carte_png_IA_1                  
        IA_carte1 = pygame.image.load(chemin_IAcarte1)
        B_IA_carte1 = Bouton(390,10, IA_carte1, 0.90)

    x = B_IA_carte1

    if len(IA.main) > 1:
        B_J2_carte2 = Bouton(475, 10, carte_face_cachee, 0.3)
        y = B_J2_carte2
    
    return x, y

# Création du du plateau de jeu
def plateau_jeu(m,t):
    screen = pygame.display.set_mode((1067, 753))
    pygame.display.set_caption('LOVE LETTER - GAME')

    background = pygame.image.load("Projet/Images/background.jpg").convert()
    background = pygame.transform.scale(background, screen.get_size())

    font_text = pygame.font.SysFont("Calibri", 34, True)
    font_effet = pygame.font.SysFont("Calibri", 20, True)

    manche = font_text.render("Manche : " + str(m), 1, (0, 0, 0))
    manchepos = manche.get_rect()
    manchepos.centerx = 170
    manchepos.centery = 80

    tour = font_text.render("Tour : " + str(t), 1, (0, 0, 0))
    tourpos = tour.get_rect()
    tourpos.centerx = 170
    tourpos.centery = 120

    s1 = font_text.render("Score J1 : " + str(J1.nb_faveur), 1, (0, 0, 0))
    s1pos = s1.get_rect()
    s1pos.centerx = 880
    s1pos.centery = 80

    s2 = font_text.render("Score IA : " + str(IA.nb_faveur), 1, (0, 0, 0))
    s2pos = s2.get_rect()
    s2pos.centerx = 880
    s2pos.centery = 120

    p = font_text.render("Pioche", 1, (0, 0, 0))
    ppos = p.get_rect()
    ppos.centerx = 170
    ppos.centery = 240

    if J1.immune == True:
        immun1 = font_effet.render("Vous êtes immunisé !", 1, (255, 255, 255))
        immun1pos = immun1.get_rect()
        immun1pos.centerx = 180
        immun1pos.centery = 660
        background.blit(immun1, immun1pos)

    if IA.immune == True:
        immun2 = font_effet.render("L'IA est immunisé !", 1, (255, 255, 255))
        immun2pos = immun2.get_rect()
        immun2pos.centerx = 800
        immun2pos.centery = 30
        background.blit(immun2, immun2pos)
    
    # Affichage des effets de cartes
    if t > 1 and len(J1.main) > 0:
        a, b ,c = desc_effet(J1.main[0].valeur)
        effet1_l1 = font_effet.render(str(J1.main[0].nom) + " : " + str(a), 1, (255, 255, 255))
        effet1_l1pos = effet1_l1.get_rect()
        effet1_l1pos.centerx = background.get_rect().centerx
        effet1_l1pos.centery = 320
        background.blit(effet1_l1, effet1_l1pos) 

        effet1_l2 = font_effet.render(str(b), 1, (255, 255, 255))
        effet1_l2pos = effet1_l2.get_rect()
        effet1_l2pos.centerx = background.get_rect().centerx
        effet1_l2pos.centery = 340
        background.blit(effet1_l2, effet1_l2pos)

        effet1_l3 = font_effet.render(str(c), 1, (255, 255, 255))
        effet1_l3pos = effet1_l3.get_rect()
        effet1_l3pos.centerx = background.get_rect().centerx
        effet1_l3pos.centery = 360
        background.blit(effet1_l3, effet1_l3pos) 

        if len(J1.main) > 1:
            d, e ,f = desc_effet(J1.main[1].valeur)
            effet2_l1 = font_effet.render(str(J1.main[1].nom) + " : " + str(d), 1, (255, 255, 255))
            effet2_l1pos = effet2_l1.get_rect()
            effet2_l1pos.centerx = background.get_rect().centerx
            effet2_l1pos.centery = 400
            background.blit(effet2_l1, effet2_l1pos) 

            effet2_l2 = font_effet.render(str(e), 1, (255, 255, 255))
            effet2_l2pos = effet2_l2.get_rect()
            effet2_l2pos.centerx = background.get_rect().centerx
            effet2_l2pos.centery = 420
            background.blit(effet2_l2, effet2_l2pos)

            effet2_l3 = font_effet.render(str(f), 1, (255, 255, 255))
            effet2_l3pos = effet2_l3.get_rect()
            effet2_l3pos.centerx = background.get_rect().centerx
            effet2_l3pos.centery = 440
            background.blit(effet2_l3, effet2_l3pos) 
       
    background.blit(p, ppos)
    background.blit(s2, s2pos)
    background.blit(s1, s1pos)
    background.blit(manche, manchepos)
    background.blit(tour, tourpos)
    screen.blit(background, (0, 0))
    maj_screen()

# Mise à jour du screen
def maj_screen():
    pygame.display.flip()
    game_event()

# Afficher la pioche
def afficher_pioche():

    #Charger l'image de la carte face cachée
    B_pioche_jpg = Bouton(80, 255, carte_face_cachee, 0.3)

    return B_pioche_jpg

# Afficher les 3 cartes brulées connues
def afficher_cartes_b():
    carte_B_1 = cartes_retirees[1].nom.lower()              
    carte_png_B_1 = carte_en_png(carte_B_1)
    chemin_Bcarte1 = Path().cwd() / 'Projet' / 'Images' / 'images_cartes' / carte_png_B_1                  
    B_carte1 = pygame.image.load(chemin_Bcarte1)
    B_B_carte1 = Bouton(825,235, B_carte1, 0.95)
    B_B_carte1.draw()

    carte_B_2 = cartes_retirees[2].nom.lower()                  
    carte_png_B_2 = carte_en_png(carte_B_2)
    chemin_Bcarte2 = Path().cwd() / 'Projet' / 'Images' / 'images_cartes' / carte_png_B_2                 
    B_carte2 = pygame.image.load(chemin_Bcarte2)
    B_B_carte2 = Bouton(825,295, B_carte2, 0.95)
    B_B_carte2.draw()

    carte_B_3 = cartes_retirees[3].nom.lower()                   
    carte_png_B_3 = carte_en_png(carte_B_3)
    chemin_Bcarte3 = Path().cwd() / 'Projet' / 'Images' / 'images_cartes' / carte_png_B_3              
    B_carte3 = pygame.image.load(chemin_Bcarte3)
    B_B_carte3 = Bouton(825,355, B_carte3, 0.95)
    B_B_carte3.draw()

# "if" statement pour savoir quelle carte à activer son effet
def Effet(x, i):
    if J1.immune == False and IA.immune == False:
        if x == 1:
            Garde(i)
        elif x ==2:
            Pretre(i)
        elif x == 3:
            Baron(i)
        elif x == 7:
            Roi()

    if x == 0:
        Espionne()
    elif x == 4:
        Servante(i)
    elif x == 5:
        Prince(i)
    elif x == 6:
        Chancelier(i)
    elif x == 9:
        Princesse(i)

# Permet d'essayer de deviner la carte de l'adversaire
def Garde(i):
    # Si c'est au tour du joueur 1 de deviner
    if i == 0:
        # Affichage de toutes les cartes selectionnables
        choix = 1
        C1,C3,C4,C5,C6,C7,C8,C9,C10 = afficher_effet_garde()
        C1.draw()
        C3.draw()
        C4.draw()
        C5.draw()
        C6.draw()
        C7.draw()
        C8.draw()
        C9.draw()
        C10.draw()
        maj_screen()
        while choix != 0 and choix != 2 and choix != 3 and choix != 4 and choix != 5 and choix != 6 and choix != 7 and choix != 8 and choix != 9:
            maj_screen()
            if C1.draw():
                choix = 0
            if C3.draw():
                choix = 2
            if C4.draw():
                choix = 3
            if C5.draw():
                choix = 4
            if C6.draw():
                choix = 5
            if C7.draw():
                choix = 6
            if C8.draw():
                choix = 7
            if C9.draw():
                choix = 8
            if C10.draw():
                choix = 9
        if IA.main[0].valeur == choix:
            IA.elimine = True
            print("Le joueur 2 est éliminé !")
        else:
            print("Vous n'avez pas trouvé.")
    # Si c'est à l'IA
    else:
        # Si grâce à un prètre nous connaissons sa carte
        if len(main_adversaire) > 0:
            choix = main_adversaire[0].valeur
        else :
            # Determine le meilleur choix grâce au tableau de cartes avec les meilleurs proba
            choix = carte_probable(meilleures_cartes)
        if J1.main[0].valeur == choix:
            J1.elimine = True
            print("Le joueur 1 est éliminé !")
        else:
            print("Vous n'avez pas trouvé.")

# Permet de choisir un joueur et il doit se débarasser de sa carte pour en piocher une autre
def Prince(i):
    choix = -1
    if J1.immune == False and IA.immune == False:
        if i == 0:
            J1_1, J1_2, J1_3 = afficher_mainJ1()
            IA_1, IA_2 = afficher_mainJ2()
            while choix != 0 and choix!= 1:
                maj_screen()
                if J1_1.draw():
                    choix = 0
                if IA_1.draw():
                    choix = 1
        # Si c'est l'IA qui joue, permet de déterminer le meilleur coup grâce à soit le pourcentage (correspondant à la meilleur carte à avoir en main) si l'on connait la carte de l'adversaire soit de voir si la seconde carte de l'IA à une valeur supérieur ou égale à 5
        else :
            if len(main_adversaire) > 0:
                if main_adversaire[0].pourcentage <= IA.main[0].pourcentage:
                    choix = 0
                else:
                    choix = 1
            else:
                if IA.main[0].valeur >= 5:
                    choix = 0
                else:
                    choix = 1
    # Si l'adversaire est immunisé le joueur ayant posé cette carte doit obligatoirement se choisir 
    else:
        choix = i

    # La carte choie est defaussé et il en pioche une nouvelle
    joueur_restant[choix].defausse.append(joueur_restant[choix].main[0])
    del joueur_restant[choix].main[0]
    joueur_restant[choix].main.append(Pioche(deck))

    # Si c'est le joueur 1 qui se defausse, supprime la possiblité de la carte défaussée dans le deckIA 
    if choix == 1:
        deckIA[IA.main[0].valeur] -= 1
    elif choix == 0 and len(main_adversaire)>0:
        del(main_adversaire[-1])
    else:
        print("J1 se defausse " + str(J1.defausse[-1].nom))
    Main_Joueur(choix)

# Pioche 2 cartes et en repose 2 dans à la fin de la pioche
def Chancelier(i):
    # Si l'IA connaissait la carte de l'adversaire, del cette dernière car on n'est plus sûr à 100% qu'il à gardé la carte dans sa main
    if i == 0 and len(main_adversaire)>0:
        deckIA[main_adversaire[-1].valeur] += 1
        del(main_adversaire[-1])

    # Pioche des 2 nouvelles cartes
    joueur_restant[i].main.append(Pioche(deck))
    joueur_restant[i].main.append(Pioche(deck))

    Main_Joueur(i)

    jeter = -1
    jeter2 = -1
    if i == 0:
        J1_1, J1_2, J1_3 = afficher_mainJ1()
        J1_1.draw()
        J1_2.draw()
        J1_3.draw()
        maj_screen()
        # Choix pour le joueur 1 des cartes dont il veut ce défausser
        while jeter != 0 and jeter != 1 and jeter != 2:
            maj_screen()
            if J1_1.draw():
                jeter = 0
            if J1_2.draw():
                jeter = 1
            if J1_3.draw():
                jeter = 2
        while jeter2 != 0 and jeter2 != 1 and jeter2 != 2:
            maj_screen()
            if jeter == 0:
                if J1_2.draw():
                    jeter2 = 0
                if J1_3.draw():
                    jeter2 = 1
            if jeter == 1:
                if J1_1.draw():
                    jeter2 = 0
                if J1_3.draw():
                    jeter2 = 1
            if jeter == 2:
                if J1_1.draw():
                    jeter2 = 0
                if J1_2.draw():
                    jeter2 = 1
    else :
        # Si c'est l'IA qui pioche supprime les possiblités dans deckIA 
        deckIA[IA.main[-1].valeur] -= 1
        deckIA[IA.main[-2].valeur] -= 1
        l = 0
        j = 0
        p1 = 100
        p2 = 100
        # Défausse de l'IA par les poucentages des cartes qu'il à en main, ne garde que la carte avec le plus haut pourcentage
        while l < 3:
            if p1 > IA.main[l].pourcentage:
                p1 = IA.main[l].pourcentage
                jeter = l
            l += 1
            while j < 2:
                if p2 > IA.main[j].pourcentage:
                    p2 = IA.main[j].pourcentage
                    jeter2 = j
                j += 1
    # Remet la première carte dans le deck
    print("Les cartes remisent dans le deck sont : " + str(joueur_restant[i].main[jeter].nom))
    deck.append(joueur_restant[i].main[jeter])
    deck[joueur_restant[i].main[jeter].valeur].nb_carte += 1
    if i == 1:
        deckIA[IA.main[jeter].valeur] += 1
    del joueur_restant[i].main[jeter]
    # Remet la seconde
    print("Et " + str(joueur_restant[i].main[jeter2].nom))
    deck.append(joueur_restant[i].main[jeter2])
    deck[joueur_restant[i].main[jeter2].valeur].nb_carte += 1
    if i == 1:
        deckIA[IA.main[jeter2].valeur] += 1
    del joueur_restant[i].main[jeter2]

# Permet de créer toutes les cartes de l'effet du garde en bouton
def afficher_effet_garde():
    carte_1 = carte1.nom.lower()
    carte_3 = carte3.nom.lower()
    carte_4 = carte4.nom.lower()
    carte_5 = carte5.nom.lower()
    carte_6 = carte6.nom.lower()
    carte_7 = carte7.nom.lower()
    carte_8 = carte8.nom.lower()
    carte_9 = carte9.nom.lower()
    carte_10 = carte10.nom.lower()

    carte_png_1 = carte_en_png(carte_1)
    carte_png_3 = carte_en_png(carte_3)
    carte_png_4 = carte_en_png(carte_4)
    carte_png_5 = carte_en_png(carte_5)
    carte_png_6 = carte_en_png(carte_6)
    carte_png_7 = carte_en_png(carte_7)
    carte_png_8 = carte_en_png(carte_8)
    carte_png_9 = carte_en_png(carte_9)
    carte_png_10 = carte_en_png(carte_10)

    chemin_carte1 = Path().cwd() / 'Projet' / 'Images' / 'images_cartes' / carte_png_1
    chemin_carte3 = Path().cwd() / 'Projet' / 'Images' / 'images_cartes' / carte_png_3
    chemin_carte4 = Path().cwd() / 'Projet' / 'Images' / 'images_cartes' / carte_png_4
    chemin_carte5 = Path().cwd() / 'Projet' / 'Images' / 'images_cartes' / carte_png_5
    chemin_carte6 = Path().cwd() / 'Projet' / 'Images' / 'images_cartes' / carte_png_6
    chemin_carte7 = Path().cwd() / 'Projet' / 'Images' / 'images_cartes' / carte_png_7
    chemin_carte8 = Path().cwd() / 'Projet' / 'Images' / 'images_cartes' / carte_png_8
    chemin_carte9 = Path().cwd() / 'Projet' / 'Images' / 'images_cartes' / carte_png_9
    chemin_carte10 = Path().cwd() / 'Projet' / 'Images' / 'images_cartes' / carte_png_10

    C_carte1 = pygame.image.load(chemin_carte1)
    C_carte3 = pygame.image.load(chemin_carte3)
    C_carte4 = pygame.image.load(chemin_carte4)
    C_carte5 = pygame.image.load(chemin_carte5)
    C_carte6 = pygame.image.load(chemin_carte6)
    C_carte7 = pygame.image.load(chemin_carte7)
    C_carte8 = pygame.image.load(chemin_carte8)
    C_carte9 = pygame.image.load(chemin_carte9)
    C_carte10 = pygame.image.load(chemin_carte10)

    C1_carte = Bouton(250,70, C_carte1, 0.95)
    C3_carte = Bouton(450,70, C_carte3, 0.95)
    C4_carte = Bouton(650,70, C_carte4, 0.95)
    C5_carte = Bouton(250,270, C_carte5, 0.95)
    C6_carte = Bouton(450,270, C_carte6, 0.95)
    C7_carte = Bouton(650,270, C_carte7, 0.95)
    C8_carte = Bouton(250,470, C_carte8, 0.95)
    C9_carte = Bouton(450,470, C_carte9, 0.95)
    C10_carte = Bouton(650,470, C_carte10, 0.95)
        
    return C1_carte, C3_carte, C4_carte, C5_carte, C6_carte, C7_carte, C8_carte, C9_carte, C10_carte

# Jeu principale
def main():
    continuer = 1

    while continuer:
        # Commencement de la partie
        print("La partie va commencer...\n")

        # Game
        m = 1
        t = 1 
        while J1.nb_faveur < 6 and IA.nb_faveur < 6:
            # Détérminer le nombre de manche
            print("Manche " + str(m) + " :\n" )

            # Bruler une carte du deck face verso
            cartes_retirees.append(Pioche(deck))
            print("La carte brulée est : " + str(cartes_retirees[-1].nom) + "\n")

            # Retirer 3 cartes du jeu face recto
            print("Les cartes suivantes seront retirés du jeu : ")
            i = 0
            while i < 3 :
                c = Pioche(deck)
                cartes_retirees.append(c)
                print("- " + str(cartes_retirees[-1].nom))
                deckIA[c.valeur] -= 1
                i += 1
            print("\n")

            la_pioche = afficher_pioche()

            # Fontion tour par tour, joueur 1 puis l'IA
            t = 1
            while Compter_carte(deck) > 0 and J1.elimine == False and IA.elimine == False:
                i = 0
                print("Tour " + str(t) + " :\n" )
                while i < len(joueur_restant) and Compter_carte(deck) > 0 and J1.elimine == False and IA.elimine == False:

                    # Distribution des cartes aux joueurs
                    print("Le joueur " + str(i+1) + " pioche...")
                    afficher_cartes_b()
                    if i == 0 and t > 1:
                        while len(J1.main) < 2:
                            maj_screen()
                            if la_pioche.draw():
                                print('Vous avez pioché')
                                c = Pioche(deck)
                                J1.main.append(c)
                    else:
                        c = Pioche(deck)
                        joueur_restant[i].main.append(c)

                    if joueur_restant[i].immune == True:
                        joueur_restant[i].immune = False
                        print("Le joueur " + str(i + 1) + " n'est plus immunisé !")
                        
                    plateau_jeu(m, t)
                    afficher_cartes_b()
                    la_pioche.draw()

                    # Afficher les cartes du joueur 1
                    J1_1, J1_2, J1_3 = afficher_mainJ1()
                    J1_1.draw()
                    if len(J1.main) > 1:
                        J1_2.draw()

                    # Afficher les cartes de l'IA (face cachée)
                    IA_1, IA_2 = afficher_mainJ2()
                    IA_1.draw()
                    if len(IA.main) > 1:
                        IA_2.draw()

                    maj_screen()

                    Main_Joueur(i)  

                    if i == 1:
                        deckIA[c.valeur] -= 1
                    stats()

                    # Choix de la carte à poser
                    if t > 1 and Nb_carte_main(i) > 0:
                        if i == 0:
                            print("Choisisez une carte à jeter !")
                            while len(J1.main) > 1:
                                maj_screen()
                                if J1.main[0] == carte9 and (carte6 in J1.main or carte8 in J1.main):
                                    if J1_1.draw():
                                        Comtesse(i)
                                        Jeter(0)
                                elif J1.main[1] == carte9 and (carte6 in J1.main or carte8 in J1.main):
                                    if J1_2.draw():
                                        Comtesse(i)
                                        Jeter(1)
                                else:
                                    if J1_1.draw():
                                        Jeter(0)
                                    if J1_2.draw():
                                        Jeter(1)
                        else:
                            Jeter_IA()

                        Effet(joueur_restant[i].defausse[-1].valeur, i)

                    plateau_jeu(m,t)
                    afficher_cartes_b()
                    la_pioche.draw()

                    J1_1, J1_2, J1_3 = afficher_mainJ1()
                    J1_1.draw()
                    IA_1, IA_2 = afficher_mainJ2()
                    IA_1.draw()

                    maj_screen()
                    if t > 1:
                        time.sleep(0.8)

                    print("\n")
                    i += 1
                t += 1
                
            if Compter_carte(deck) == 0:
                plateau_jeu(m, t)
                afficher_cartes_b()
                maj_screen()

            QuiGagne()
            print("Récapilutaf des faveurs :\n- Joueur 1 : " + str(J1.nb_faveur) + "\n- IA : " + str(IA.nb_faveur) + "\n")
            Reset()
            print("\n")
            m += 1

        #continuer = 0
        Reset()

    # continuer = 1
    # if J1.nb_faveur >= 6:
    #     v1 = font_text.render("LE JOUEUR 1 A GAGNE", 1, (0, 0, 0))
    # elif IA.nb_faveur >= 6:
    #     v1 = font_text.render("L'IA' A GAGNE", 1, (0, 0, 0))

    # bv1 = bouton.get_rect()
    # bv1.centerx = background.get_rect().centerx
    # bv1.centery = background.get_rect().centery
    # v1pos = v1.get_rect()
    # v1pos.centerx = bv1.centerx
    # v1pos.centery = bv1.centery
        
    # screen.blit(bouton, bv1)
    # screen.blit(v1, v1pos)

    # while continuer == 1:
    #     sx, sy = pygame.mouse.get_pos()
    #     pressed = pygame.mouse.get_pressed()
    #     collide_bv1 = bv1.collidepoint(sx, sy)
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             pygame.quit()
    #             continuer = 0
    #             exit()
                
    #     if pygame.mouse.get_focused():
    #         if collide_bv1 and pressed[0]:
    #             game()
    #     pygame.display.flip()


home()