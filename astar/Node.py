from collections import deque
from tools import sum_vector2D


class Node:
    def __init__(self, value, parent=None, forbidden: list = [], g: float = 0, h: float = float("inf")):
        """
        Initialisation de l'instance

        :param value: Value de l'instance
        :param Node parent: Node parent de l'instance
        :param float * float List forbidden: Liste des valeurs interdites
        :param float g: Coût Accumulé
        :param float h: Estimation Heuristique
        """

        self.value = value
        self.parent = parent
        self.forbidden = forbidden
        self.g = g
        self.h = h

    def __eq__(self, other):
        """
        Test d'égalite (choisi) sur la valeur de self.value

        :param Node other: Node à comparer avec l'instance
        :return Bool: Résultat du test
        """
        return self.value == other.value

    def __str__(self):
        """
        Gère la conversion en chaîne de caractères : ici, on affiche la valeur

        :return String: Représentation
        """

        return str(self.value)

    def f(self):
        """
        Calcul de la Fitness Function du Node en vue du self.g et self.h

        :return Float: Fitness Function
        """
        return self.g + self.h

    def generate_successors(self):
        """
        Génère les 8 successeurs autour de l'instance

        :return Node list: Liste des successeurs
        """

        move = [-1, 0, 1]
        successors = []

        for i in move:
            for j in move:
                new_value = sum_vector2D(self.value, (i, j))

                if i != 0 and j != 0:  # Mouvement en diagonale
                    cost = float("inf")  # Racine de 2
                else:
                    cost = 1

                if new_value != self.value and new_value not in self.forbidden:
                    successors.append(Node(value=new_value,
                                           parent=self,
                                           forbidden=self.forbidden,
                                           g=self.g + cost))

        return successors

    def get_path(self):
        if self.parent is None:
            return [self.value]
        else:
            return self.parent.get_path() + [self.value]  # On utilise l'opération + afin de créer un nouvel objet
