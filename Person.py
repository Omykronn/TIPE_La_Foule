from matplotlib.patches import Circle
from collections import deque

from AStar import a_star


colors = ["crimson", "orangered", "orange", "gold", "chartreuse", "royalblue"]


class Person(Circle):
    def __init__(self, depart: tuple, destination: tuple, size=0.5, priority=1, speed=2):
        """
        Initialisation des attributs de Person

        :param tuple depart: Coordonnées du point de départ
        :param tuple destination: Coordonnées du point d'arrivée visé
        :param float new_vitesse: Vitesse maximale
        """

        super().__init__(depart, radius=size)  # On utilise l'initialisation de la classe-parent

        # Départ et Arrivée
        self._center = depart
        self.destination = destination

        # Déplacement
        self.speed = speed
        self.path = a_star(self._center, self.destination)
        self.path.append(self.destination)  # Pour avoir une frame où la personne est sur sa destination

        # Attribut
        self.priority = priority

        # Apparences
        self.size = size
        self.name = colors[0]  # Le nom de la couleur est aussi le nom de la personne
        self.set_color(self.name)

        colors.pop(0)  # On retire la couleur de la liste afin de ne pas avoir de doublon de couleur/nom

    def move(self):
        """
        Définie la position selon self.path

        :return None:
        """

        self._center = self.path[0]
        self.path.popleft()

    def has_reached_goal(self):
        """
        Fonction vérifiant si l'objet a atteint son objectif ; le critère étant le nombre d'éléments dans self.path

        :return bool: Test d'arrivée à destination
        """
        return len(self.path) == 0
