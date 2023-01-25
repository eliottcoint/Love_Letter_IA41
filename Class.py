# Définition de la class Carte
class Carte():
    def __init__(self, nom="name", nb_carte=0, valeur=0, pourcentage=0) :
        self.nom = nom
        self.nb_carte = nb_carte
        self.valeur = valeur
        self.pourcentage = pourcentage

# Définition de la class Joueur
class Joueur():
    def __init__(self, main=[], nb_faveur=0, defausse=[], elimine = False, immune = False) :
        self.main = []
        self.nb_faveur = nb_faveur
        self.defausse = []
        self.elimine = False
        self.immune = False