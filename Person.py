from matplotlib.patches import Circle
from collections import deque

from astar.algorithm import a_star
from tools import sub_vector2D, sum_vector2D
from CollisionManager import CollisionManager


class Person(Circle):
    def __init__(self, name: str, depart: tuple, destination: tuple, color: str, size: float = 0.15, priority: int = 1,
                 speed: int = 1):
        """
        Initialisation des attributs de Person

        :param str name: Nom de l'agent
        :param tuple depart: Coordonnées du point de départ
        :param tuple destination: Coordonnées du point d'arrivée visé
        :param str color: Couleur du disque
        :param float size: Rayon de la sphère (et donc taille de la réprésentation)
        :param int priority: Indice de priorité social
        :param float speed: Vitesse de parcours de self.path (et donc de déplacement)
        """

        super().__init__(depart, radius=size)  # On utilise l'initialisation de la classe-parent

        # Départ et Arrivée
        self.position = depart  # On considère deux variables pour la position : position se référant à la case
        self._center = depart   # et _center qui est la véritable position, même pendant les transitions de cases
        self.destination = destination  # Case objectif

        # Déplacement
        self.speed = speed  # Vitesse de parcours du deque path
        # Deque contenant toutes les étapes du parcours, sans prendre en compte les collisions (juste obstacles)
        self.path = deque(a_star(self._center, self.destination))
        self.path.append(self.destination)  # On ajoute une fois en plus la dernière case, pour voir le personnage dessus
        # TODO self.path devra être de longueur divisible par self.speed

        # Attribut
        self.priority = priority  # Indice de priorité de l'Agent

        # Apparences
        self.size = size  # Rayon du disque
        self.name = name  # Nom, notamment utilisé dans les messages
        self.set_color(color)  # Couleur du disque

    def move(self):
        """
        Méthode faisant évoluer la position de case en case
        """

        self._center = self.get_next_position()  # On obtient la position suivante
        self.position = self._center             # que l'on défini aussi comme la position du disque

        for _ in range(self.speed):  # On supprime assez d'étapes intermédiaires pour être cohérent avec self.speed
            self.path.popleft()

    def half_move(self, coeff):
        """
        Méthode utilisée pendant les transitions de case en case : self.position de bouge pas, mais la position du
        disque oui

        :param float coeff: Coéfficient d'avancé entre les deux cases
        """

        (x, y) = self.position  # On récupère les coordonnées de la case actuelle
        (z, t) = self.get_next_position()  # On récupère les coordonnées de la case suivante

        self._center = (x + coeff * (z - x), y + coeff * (t - y))  # On calcule la position du disque pendant la transition

    def change_path(self, order):
        """
        Méthode appliquant l'ordre donné par le Collision Manager

        :param int order: Identifiant de l'ordre à appliquer (cf. CollisionManager.py)
        """

        # On détermine le vecteur mouvement afin de déterminer la droite et la gauche de l'Agent
        move = sub_vector2D(self.get_next_position(), self.get_position())

        # On détermine le mouvement à effectuer avec la table de conversion
        new_move = CollisionManager.order_to_move[move][order]
        # Calcul de la position suivant (et donc du nouveau départ pour A*)
        new_start = sum_vector2D(self.position, new_move)

        # L'algorithme A* détermine un nouveau chemin, après modification
        self.path = deque(a_star(new_start, self.destination))

    def has_reached_goal(self):
        """
        Fonction vérifiant si l'objet a atteint son objectif ; le critère étant le nombre d'éléments dans self.path

        :return bool: Test d'arrivée à destination
        """

        return len(self.path) == 0

    def get_position(self):
        """
        Renvoie la position (case) actuelle

        :return int * int: Coordonnées de la case actuelle
        """

        return self.position

    def get_next_position(self):
        """
        Renvoie la position de la case suivante (dépendante de self.speed)

        :return int * int: Coordonnées de la case suivante
        """

        return self.path[self.speed - 1]
