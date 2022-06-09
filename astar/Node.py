from collections import deque
from tools import sum_vector2D


class Node:
    def __init__(self, value, parent=None, g: float = 0, h: float = float("inf")):
        """
        Initialisation de l'instance

        :param value: Value de l'instance
        :param Node parent: Node parent de l'instance
        :param float g: Coût Accumulé
        :param float h: Estimation Heuristique
        """

        self.value = value
        self.parent = parent
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
                if not(i == 0 and j == 0):
                    successors.append(Node(value=sum_vector2D(self.value, (i, j)),
                                           parent=self,
                                           g=self.g + 1))

        return successors

    def get_path(self):
        if self.parent is None:
            return [self.value]
        else:
            return self.parent.get_path() + [self.value]  # On utilise l'opération + afin de créer un nouvel objet
