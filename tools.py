def speed_convert(v, frame_rate):
    return v / frame_rate  # Traduit la vitesse réelle en une valeur en fonction de frame_rate


def sum_vector2D(v1, v2):
    """
    Somme deux 2-uplets coefficients par coefficients

    :param tuple v1: 2-uplet n°1
    :param tuple v2:  2-uplets n°2
    :return tuple: Somme de v1 et v2
    """

    return v1[0] + v2[0], v1[1] + v2[1]
