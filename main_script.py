import matplotlib.pyplot as plt
import matplotlib.animation as animation

from tools import unlink

from Crowd import Crowd

# Paramètres

N = 2
start_pos = [(0, -10), (-10, 0)]
end_pos = [(0, 10), (10, 0)]

frame_rate = 3   # Nombre d'image par seconde
x_interval = (-12, 12)  # Limites de l'axe X
y_interval = (-12, 12)  # Limites de l'axe Y

csv_location = "/home/saintv/Documents/PycharmProjects/TIPE_La_Foule/resources/param_people.csv"

# ~~~~~~~~~~

crowd = Crowd(N, start_pos, end_pos)  # On génère l'objet-conteneur des N personnes
# crowd.add_from_csv(csv_location)

fig = plt.figure()
ax = plt.axes(xlim=x_interval, ylim=y_interval, aspect="equal")  # L'arguement aspect assure un repère orthonormé

# Définition des écarts entre les marques sur les axes
ax.set_xticks([i + 0.5 for i in range(x_interval[0], x_interval[1])])
ax.set_yticks([i + 0.5 for i in range(y_interval[0], y_interval[1])])

# Les Nombres sur les axes sont imprimés en blanc pour ne pas les voir
plt.xticks(color="w")
plt.yticks(color="w")

# Affichage des trajectoires
for person in crowd.subjects:
    x_list, y_list = unlink(person.path)
    plt.plot(x_list, y_list, color=person.name)


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
