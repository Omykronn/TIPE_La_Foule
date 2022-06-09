import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

from astar.algorithm import a_star

""" Paramètres """
x_interval = (-30, 30)  # Limites de l'axe X
y_interval = (-12, 12)  # Limites de l'axe Y

blocked_cell = [(i, 3) for i in range(-5, 0)] + [(i, 3) for i in range(3, 6)] + \
               [(i, 5) for i in range(-5, -2)] + [(i, 5) for i in range(-1, 6)] + \
               [(i, -3) for i in range(-5, 6)] + [(-5, i) for i in range(-2, 2)] + [(5, i) for i in range(-2, 4)] + \
               [(10, i) for i in range(-5, 10)]

data = [((0, 10), (0, 0), "blue"),
        ((-1, -10), (0, 0), "red"),
        ((20, 10), (0, 0), "green")]
""" ---------- """


def unlink(data_list: list):
    x_data, y_data = [], []

    for x, y in data_list:
        x_data.append(x)
        y_data.append(y)

    return x_data, y_data


fig = plt.figure()
ax = plt.axes(xlim=x_interval, ylim=y_interval, aspect="equal")  # L'arguement aspect assure un repère orthonormé

# Définition des écarts entre les marques sur les axes
ax.set_xticks([i + 0.5 for i in range(x_interval[0], x_interval[1])])
ax.set_yticks([i + 0.5 for i in range(y_interval[0], y_interval[1])])

# Les Nombres sur les axes sont imprimés en blanc pour ne pas les voir
plt.xticks(color="w")
plt.yticks(color="w")

canva, = ax.plot([0], [0], 'bo', ms=5, color="silver")  # On place un point gris à l'origine

# Affichage des obstacles
for x, y in blocked_cell:
    ax.add_patch(Rectangle((x - 0.5, y - 0.5), 1, 1, facecolor="silver"))

# Affichage des trajectoires
for start, stop, color in data:
    x_list, y_list = unlink(a_star(start, stop, blocked=blocked_cell))
    plt.plot(x_list, y_list, color=color)

plt.grid(which="major")  # Affichage d'une grille pour plus de visibilité
plt.show()  # Affichage de la fenêtre
