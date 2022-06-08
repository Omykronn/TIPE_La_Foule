from matplotlib.patches import Circle
# from collections import deque

from AStar import a_star


colors = ["crimson", "orangered", "orange", "gold", "chartreuse", "royalblue"]


class Person(Circle):
    def __init__(self, depart: tuple, destination: tuple, size: float = 0.5, priority: int = 1, speed: int = 1):
        """
        Initialisation des attributs de Person

        :param tuple depart: Coordonnées du point de départ
        :param tuple destination: Coordonnées du point d'arrivée visé
        :param float size: Rayon de la sphère (et donc taille de la réprésentation)
        :param int priority: Indice de priorité social
        :param float speed: Vitesse de parcours de self.path (et donc de déplacement)
        """

        super().__init__(depart, radius=size)  # On utilise l'initialisation de la classe-parent

        # Départ et Arrivée
        self._center = depart
        self.destination = destination

        # Déplacement
        self.speed = speed
        self.path = a_star(self._center, self.destination)  # self.path devra être de longueur divisible par self.speed

        while len(self.path) % self.speed != 0:  # On compléte alors avec des destinations
            self.path.append(self.destination)

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

        self._center = self.path[self.speed - 1]

        for _ in range(self.speed):  # self.path contient toutes les étapes des déplacements : seul self.vitesse importe
            self.path.popleft()      # dans le parcours des étapes (c'est l'incrémentation)

    def has_reached_goal(self):
        """
        Fonction vérifiant si l'objet a atteint son objectif ; le critère étant le nombre d'éléments dans self.path

        :return bool: Test d'arrivée à destination
        """
        return len(self.path) == 0
