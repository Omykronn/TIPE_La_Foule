from math import sqrt
from matplotlib.patches import Polygon

from tools import sum_vector2D


colors = ["crimson", "orangered", "orange", "gold", "chartreuse", "royalblue"]


class Person(Polygon):
    def __init__(self, depart: tuple, new_destination: tuple, new_vitesse: float = 1.2, new_size=1):
        """
        Initialisation des attributs de Person

        :param tuple depart: Coordonnées du point de départ
        :param tuple new_destination: Coordonnées du point d'arrivée visé
        :param float new_vitesse: Vitesse maximale
        """

        super().__init__([(0, 0), (0, 0)])  # On utilise l'initialisation de la classe-parent

        self.position = depart
        self.destination = new_destination
        self.vitesse = new_vitesse
        self.size = new_size

        self.recalcul_vecteur()

        self.name = colors[0]  # Le nom de la couleur est aussi le nom de la personne
        self.set_color(self.name)

        colors.pop(0)  # On retire la couleur de la liste afin de ne pas avoir de doublon de couleur/nom

    def recalcul_vecteur(self):
        """
        Calcul le nouveau vecteur vitesse de la position lors de l'appel vers le point d'arrivée

        :return: None
        """

        adj = self.destination[0] - self.position[0]
        opp = self.destination[1] - self.position[1]  # Noms de variable liés à la trigonométrie : projections
        hyp = sqrt(opp ** 2 + adj ** 2)

        if hyp == 0:  # Cas pour éviter la division par zéro
            coord_x = 0  # Arbitrairement, on choisit que le vecteur vitesse soit (0, 0)
            coord_y = 0
        else:
            coord_x = adj / hyp
            coord_y = opp / hyp

        self.vecteur = (coord_x * self.vitesse, coord_y * self.vitesse)

    def move(self):
        """
        Incrémente chacune des coordonées positions par les coordonnées respectives du vecteur vitesse

        :return: None
        """
        self.position = sum_vector2D(self.position, self.vecteur)
        self.recalcul_vecteur()

        self.draw_me()

    def draw_me(self):
        """
        Fonction assurant le calcul des coordonnées des sommets du triangle

        :return: None
        """

        norm_speed = sqrt(self.vecteur[0] ** 2 + self.vecteur[1] ** 2)  # Norme du vecteur vitesse

        if self.vecteur == (0, 0):  # Cas pour éviter la division par zéro
            x, y = - self.size, 0  # Dans le cas d'un vecteur vitesse nul, on choisit arbitrairement que la direction
                                   # soit plein-Ouest
        else:
            x, y = self.vecteur[0] * (self.size / norm_speed), self.vecteur[1] * (self.size / norm_speed)

        norm_side = sqrt((x + y) ** 2 + (x - y) ** 2)  # Norme des vecteurs temporaires d'ajout

        # Definit les coordonnées des sommets du triangle de repésentation
        top_point = sum_vector2D(self.position, (x, y))
        # On cherche a faire en sorte que self.position soit le centre de gravité du triangle : pour cela, on fait en
        # sorte que la norme de vecteurs d'ajout soit bien self.size
        right_point = sum_vector2D(self.position, ((-y - x) * (self.size / norm_side), (x - y) * (self.size / norm_side)))
        left_point = sum_vector2D(self.position, ((y - x) * (self.size / norm_side), (-x - y) * (self.size / norm_side)))

        self.set_xy([top_point, right_point, left_point])

    def has_reach_goal(self):
        """
        Fonction vérifiant si l'objet a atteint son objectif ; le critère étant la distance entre sa position et son
        objectif par rapport à la norme de son vecteur vitesse

        :return bool: Test d'arrivée à destination
        """
        return sqrt((self.position[0] - self.destination[0]) ** 2 + (self.position[1] - self.destination[1]) ** 2) \
               < self.vitesse
