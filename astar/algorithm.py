from collections import deque
from Node import Node


def heuristic():
    # TODO : Définit le type de fonction heuristique à utiliser
    return None


def minimum(node_list: list):
    """
    Retourne l'indice du Node au coût minimal

    :param Node list node_list: Liste de Node
    :return int: Indice de l'élément au coût minimal
    """

    min_i = 0
    min_value = float("inf")

    for i in range(len(node_list)):
        if node_list[i].f() < min_value:
            min_i = i
            min_value = node_list[i].f()

    return min_i

def a_star(begin, end, h_func=heuristic):
    open_list = [Node(begin, h=0)]  # TODO : Revoir l'initialisation de open_list
    closed_list = []

    while len(open_list) > 0:
        q_index = minimum(open_list)

        del open_list[q_index]

    return deque()

