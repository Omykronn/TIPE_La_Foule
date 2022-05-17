from math import sqrt, acos, asin, pi
from matplotlib.patches import Circle

from tools import sum_vector2D


colors = ["crimson", "orangered", "orange", "gold", "chartreuse", "royalblue"]


class Person(Circle):
    def __init__(self, depart: tuple, new_destination: tuple, new_size=0.5):
        """
        Initialisation des attributs de Person

        :param tuple depart: Coordonnées du point de départ
        :param tuple new_destination: Coordonnées du point d'arrivée visé
        :param float new_vitesse: Vitesse maximale
        """

        super().__init__(depart, radius=new_size)  # On utilise l'initialisation de la classe-parent

        self._center = depart
        self.destination = new_destination
        self.size = new_size

        self.name = colors[0]  # Le nom de la couleur est aussi le nom de la personne
        self.set_color(self.name)

        colors.pop(0)  # On retire la couleur de la liste afin de ne pas avoir de doublon de couleur/nom

    def move(self):
        """
        Incrémente chacune des coordonées positions par les coordonnées respectives du vecteur vitesse

        :return: None
        """
        adj = self.destination[0] - self._center[0]
        opp = self.destination[1] - self._center[1]  # Noms de variable liés à la trigonométrie : projections
        hyp = sqrt(opp ** 2 + adj ** 2)

        arccos = acos(adj / hyp)
        arcsin = asin(opp / hyp)

        if arcsin == 0:
            arcsin_sign = 1
        else:
            arcsin_sign = arcsin / abs(arcsin)

        vector = ()

        if 0 <= arccos < pi / 8:
            vector = (1, 0)
        elif pi * 7/8 < arccos <= pi:
            vector = (-1, 0)
        elif pi / 8 <= arccos < pi * 3 / 8:
            vector = (arcsin_sign, arcsin_sign)
        elif pi * 3 / 8 <= arccos < pi * 5 / 8:
            vector = (0, arcsin_sign)
        else:
            vector = (-arcsin_sign, -arcsin_sign)

        self._center = sum_vector2D(self._center, vector)

    def has_reached_goal(self):
        """
        Fonction vérifiant si l'objet a atteint son objectif ; le critère étant la distance entre sa position et son
        objectif par rapport à la norme de son vecteur vitesse

        :return bool: Test d'arrivée à destination
        """
        return self._center == self.destination
