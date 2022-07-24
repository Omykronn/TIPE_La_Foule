import matplotlib.pyplot as plt
import matplotlib.animation as animation

from Crowd import Crowd
from CollisionManager import CollisionManager

from tools import read_csv

# Paramètres
csv_people = "agents_config.csv"  # Chemin jusqu'au fichier CSV contenant les informations sur les Agents
csv_obstacles = "obstacles_config.csv"  # Chemin jusqu'au fichier CSV contenant les coordonnées des obstacles

frame_rate = 30  # Nombre d'image par seconde

x_interval = (-4, 11)  # Limites de l'axe X
y_interval = (-4, 11)  # Limites de l'axe Y

# ~~~~~~~~~~

manager = CollisionManager(Crowd(csv_people, 10))  # On génère l'objet-manager à l'aide du csv

fig = plt.figure()
ax = plt.axes(xlim=x_interval, ylim=y_interval, aspect="equal")  # L'arguement aspect assure un repère orthonormé

# Définition des écarts entre les marques sur les axes
ax.set_xticks([i + 0.5 for i in range(x_interval[0], x_interval[1])])
ax.set_yticks([i + 0.5 for i in range(y_interval[0], y_interval[1])])

# Les Nombres sur les axes sont imprimés en blanc pour ne pas les voir
plt.xticks(color="w")
plt.yticks(color="w")


def draw(j=0):
    """
    Fonction assurant le dessin de chacune des frames, dont l'initialisation grâce à la valeur par défaut de j

    :param int j: Numéro de frame
    :return: None
    """

    # On fait chercher les éventuelles collisions
    manager.collision_prediction()

    manager.crowd.update(ax, j)  # Mise à jour de la foule, dont sa représentation sur l'object Axes
    return manager.crowd.get_artists()  # On retourne tous les disques représentant les Personnes pour permettre le dessin par mpl


# Lancement de l'animation avec la fonction draw et le délai entre chaque frame
anim = animation.FuncAnimation(fig, draw, init_func=draw, frames=200, interval=int(1000 / frame_rate), blit=True)

plt.grid(which="major")  # Affichage d'une grille pour plus de visibilité
# anim.save("test.gif", writer=animation.PillowWriter(fps=frame_rate))  # Dans le cas, d'une exportation en .gif

plt.show()  # Affichage de la fenêtre
