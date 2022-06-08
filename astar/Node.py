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

    def f(self):
        """
        Calcul de la Fitness Function du Node en vue du self.g et self.h

        :return Float: Fitness Function
        """
        return self.g + self.h
