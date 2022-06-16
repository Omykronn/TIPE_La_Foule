from collections import deque


def sum_vector2D(v1, v2):
    """
    Somme deux 2-uplets coefficients par coefficients

    :param tuple v1: 2-uplet n°1
    :param tuple v2:  2-uplets n°2
    :return tuple: Somme de v1 et v2
    """

    return v1[0] + v2[0], v1[1] + v2[1]


def unlink(data_list: list):
    """
    Sépare une liste de couples en deux listes dont les coefficients des couples portent le même indice

    :param list data_list: Liste à scinder
    :return list * list: Listes des coefficients des couples
    """
    x_data, y_data = [], []

    for x, y in data_list:
        x_data.append(x)
        y_data.append(y)

    return x_data, y_data


def string_to_tuple(string: str, char: str = ':'):
    """
    Convertie une chaîne de caractères en tuple selon le caractère divisant char

    :param str string: Chaîne de caractères à convertir
    :param char char: Caractère divisant
    :return tuple: Tuple issu de la conversion de string
    """
    coors = string.split(char)
    list_temp = []

    for item in coors:
        list_temp.append(int(item))

    return tuple(list_temp)


def string_to_deque(string: str, char: str = '|'):
    """
    Divise une chaîne de caractères en liste selon le caractère séparant char

    :param str string: Chaîne de caractères à convertir
    :param char char: Caractère séparant
    :return list: Liste issue de la conversion de string
    """
    d = deque()
    str_tuple = string.split(char)

    for item in str_tuple:
        d.append(string_to_tuple(item))

    return d
