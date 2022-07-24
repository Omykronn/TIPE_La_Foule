def sum_vector2D(v1, v2):
    """
    Somme deux 2-uplets coefficients par coefficients

    :param tuple v1: 2-uplet n°1
    :param tuple v2:  2-uplets n°2
    :return tuple: Somme de v1 et v2
    """

    return v1[0] + v2[0], v1[1] + v2[1]


def sub_vector2D(v1, v2):
    """
    Différence deux 2-uplets coefficients par coefficients

    :param tuple v1: 2-uplet n°1
    :param tuple v2: 2-uplets n°2
    :return tuple: Différence de v1 et v2
    """

    return v1[0] - v2[0], v1[1] - v2[1]


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


def read_csv(dir: str, titled_rows: bool = True):
    """
    Lecture d'un fichier CSV

    :param str dir: Chemin du fichier CSV à ouvrir
    :param bool titled_rows: Si le fichier contient des intitulés
    :return list data: Données du fichier CSV stockées dans une matrice Python
    """
    data = []

    with open(dir) as file:
        raw_data = file.readlines()

        for line in raw_data[titled_rows:]:  # Booléen équivalent à 0 ou 1
            temp = line.replace('\n', '').split(';')

            if len(temp) == 1:
                # Dans le cas où chaque ligne de contient qu'un élément, on ne l'ajoute pas comme une liste
                data.append(temp[0])
            elif len(temp) > 1:
                data.append(temp)

    return data
