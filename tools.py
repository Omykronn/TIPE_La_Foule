from collections import deque


def sum_vector2D(v1, v2):
    """
    Somme deux 2-uplets coefficients par coefficients

    :param tuple v1: 2-uplet n°1
    :param tuple v2:  2-uplets n°2
    :return tuple: Somme de v1 et v2
    """

    return v1[0] + v2[0], v1[1] + v2[1]


def string_to_tuple(string: str, char: str = ':'):
    coors = string.split(char)
    list_temp = []

    for item in coors:
        list_temp.append(int(item))

    return tuple(list_temp)


def string_to_deque(string: str, char: str = '|'):
    d = deque()
    str_tuple = string.split(char)

    for item in str_tuple:
        d.append(string_to_tuple(item))

    return d
