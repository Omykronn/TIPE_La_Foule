import matplotlib.pyplot as plt
import matplotlib.animation as animation

from Crowd import Crowd
from tools import speed_convert

""" Paramètres d'affichage """
frame_rate = 5   # Nombre d'image par seconde
x_interval = (-30, 30)  # Limites de l'axe X
y_interval = (-12, 12)  # Limites de l'axe Y


""" Parammètres de la simulation """
N = 1  # Nombre de personnes à simuler

depart = [(-30, 12)]  # Position de départ des N personnes
goal = [(0, 0)]  # But des N personnes (en l'occurence, l'origine du repère)
vitesse = [1]  # Vitesse en m/s de chacune des N personnes

# ~~~~~~~~~~

crowd = Crowd(N, depart, goal)  # On génère l'objet-conteneur des N personnes

fig = plt.figure()
ax = plt.axes(xlim=x_interval, ylim=y_interval, aspect="equal")  # L'arguement aspect assure un repère orthonormé
plt.plot([depart[0][0], goal[0][0]], [depart[0][1], goal[0][1]])

# Définition des écarts entre les marques sur les axes
ax.set_xticks([i + 0.5 for i in range(x_interval[0], x_interval[1])])
ax.set_yticks([i + 0.5 for i in range(y_interval[0], y_interval[1])])

# Les Nombres sur les axes sont imprimés en blanc pour ne pas les voir
plt.xticks(color="w")
plt.yticks(color="w")

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

plt.grid(which="major")  # Affichage d'une grille pour plus de visibilité
plt.show()  # Affichage de la fenêtre
