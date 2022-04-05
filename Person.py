from math import sqrt
from random import shuffle
from matplotlib.patches import Circle


colors = ["gold", "royalblue", "orange", "orangered", "crimson", "chartreuse"]
shuffle(colors)


class Person(Circle):
    def __init__(self, depart: tuple, new_destination: tuple, new_vitesse: float = 1.2, new_size=0.5):
        """
        Initialisation des attributs de Person

        :param tuple depart: Coordonnées du point de départ
        :param tuple new_destination: Coordonnées du point d'arrivée visé
        :param float new_vitesse: Vitesse maximale
        """

        super().__init__(depart, radius=new_size)

        self.destination = new_destination
        self.vitesse = new_vitesse
        self.size = new_size

        self.recalcul_vecteur()

        self.name = colors[0]
        self.set_color(self.name)

        colors.pop(0)

    def recalcul_vecteur(self):
        """
        Calcul le nouveau vecteur vitesse de la position lors de l'appel vers le point d'arrivée

        :return: None
        """

        position = self.get_center()

        adj = self.destination[0] - position[0]
        opp = self.destination[1] - position[1]  # Noms de variable liés à la trigonométrie : projections
        hyp = sqrt(opp ** 2 + adj ** 2)

        coord_x = adj / hyp
        coord_y = opp / hyp

        self.vecteur = (coord_x * self.vitesse, coord_y * self.vitesse)

    def move(self):
        """
        Incrémente chacune des coordonées positions par les coordonnées respectives du vecteur vitesse

        :return: None
        """
        position = self.get_center()

        self.set_center((position[0] + self.vecteur[0], position[1] + self.vecteur[1]))
        self.recalcul_vecteur()

    def has_reach_goal(self):
        position = self.get_center()

        return sqrt((position[0] - self.destination[0]) ** 2 + (position[1] - self.destination[1]) ** 2) \
               < self.vitesse
