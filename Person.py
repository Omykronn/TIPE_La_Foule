from math import sqrt
from random import choice


names = {"Bob": 0}


class Person:
    def __init__(self, depart: tuple, new_destination: tuple, new_vitesse: float = 1.2):
        """
        Initialisation des attributs de Person

        :param tuple depart: Coordonnées du point de départ
        :param tuple new_destination: Coordonnées du point d'arrivée visé
        :param float new_vitesse: Vitesse maximale
        """

        self.destination = new_destination
        self.position = depart
        self.vitesse = new_vitesse

        self.recalcul_vecteur()

        self.name = choice(list(names.keys()))
        self.name = self.name + " n°" + str(names[self.name] + 1)

    def recalcul_vecteur(self):
        """
        Calcul le nouveau vecteur vitesse de la position lors de l'appel vers le point d'arrivée

        :return: None
        """

        adj = self.destination[0] - self.position[0]
        opp = self.destination[1] - self.position[1]  # Noms de variable liés à la trigonométrie : projections
        hyp = sqrt(opp ** 2 + adj ** 2)

        coord_x = adj / hyp
        coord_y = opp / hyp

        self.vecteur = (coord_x * self.vitesse, coord_y * self.vitesse)

    def move(self):
        """
        Incrémente chacune des coordonées positions par les coordonnées respectives du vecteur vitesse

        :return: None
        """
        self.position = (self.position[0] + self.vecteur[0], self.position[1] + self.vecteur[1])
        self.recalcul_vecteur()

    def has_reach_goal(self):
        return sqrt((self.position[0] - self.destination[0]) ** 2 + (self.position[1] - self.destination[1]) ** 2) < self.vitesse


