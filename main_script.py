import matplotlib.pyplot as plt
import matplotlib.animation as animation

from Crowd import Crowd


frame_rate = 30   # Nombre d'image par seconde
N = 6  # Nombre de personnes à simuler

depart = [(29, 20 / N * i) for i in range(-(N // 2), N // 2)]  # Position de départ des N personnes
goal = [(0, 20 / N * i) for i in range(-(N // 2), N // 2)]  # But des N personnes (en l'occurence, l'origine du repère)
vitesse = [2.1, 1.7, 1.3, 2.5, 1.5, 2.0]  # Vitesse en m/s de chacune des N personnes


# ~~~~~~~~~~


def speed_convert(v):
    return v / frame_rate  # Traduit la vitesse réelle en une valeur en fonction de frame_rate


crowd = Crowd(N, depart, goal, [speed_convert(v) for v in vitesse])  # On génère l'objet-conteneur des N personnes

fig = plt.figure()
ax = plt.axes(xlim=(-1, 30), ylim=(-12, 12), aspect="equal")  # L'arguement aspect assure un repère orthonormé
canva, = ax.plot([0], [0], 'bo', ms=5, color="silver")  # On place un point gris à l'origine


def draw(j=0):
    """
    Fonction assurant le dessin de chacune des frames, dont l'initialisation grâce à la valeur par défaut de j

    :param int j: Numéro de frame
    :return: None
    """

    crowd.update(ax)  # Mise à jour de la foule, dont sa représentation sur l'object Axes
    return crowd.get_artists()  # On retourne tous les disques représentant les Personnes pour permettre le dessin par mpl


anim = animation.FuncAnimation(fig, draw, init_func=draw, frames=360, interval=int(1000 / frame_rate), blit=True)
# Lancement de l'animation avec la fonction draw et le délai entre chaque frame

plt.grid()  # Affichage d'une grille pour plus de visibilité
plt.show()  # Affichage de la fenêtre
