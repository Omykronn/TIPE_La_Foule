from math import sqrt
from astar.Node import Node


def euclidean_distance(current_cell: tuple, goal: tuple):
    return sqrt((current_cell[0] - goal[0])**2 + (current_cell[1] - goal[1])**2)


def minimum(node_dict: dict):
    """
    Retourne l'indice du Node au coût minimal

    :param Node dict node_dict: dictionnaire de Node
    :return Float * Float: Clef de l'élément au coût minimal
    """

    min_tag = None
    min_value = float("inf")

    for tag in node_dict:
        if node_dict[tag].f() < min_value:
            min_tag = tag
            min_value = node_dict[tag].f()

    return min_tag


def a_star(begin, end, heuristic=euclidean_distance, blocked: list = []):
    open_dict = {begin: Node(begin, forbidden=blocked, h=0)}
    closed_dict = {}

    while end not in closed_dict:
        q_tag = minimum(open_dict)
        q = open_dict[q_tag]

        closed_dict[q_tag] = q
        del open_dict[q_tag]

        for subnode in q.generate_successors():
            subnode.h = heuristic(subnode.value, end)

            """if subnode.value in open_dict and open_dict[subnode.value].f() > subnode.f():
                # Si subnode existe déjà dans open_list, mais avec une f plus faible : on le remplace
                open_dict[subnode.value] = subnode
            elif not (subnode.value in closed_dict and closed_dict[subnode.value].f() > subnode.f()):
                # Si on a pas "subnode existe déjà dans closed_list et sa f est inférieur", alors on le rajoute
                # dans open_list
                open_dict[subnode.value] = subnode"""

            if subnode.value in open_dict:
                if open_dict[subnode.value].f() > subnode.f():
                    open_dict[subnode.value] = subnode
            else:
                open_dict[subnode.value] = subnode

    return closed_dict
