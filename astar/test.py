import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

from astar.algorithm import a_star
from tools import unlink


x_interval = (-1, 11)  # Limites de l'axe X
y_interval = (-1, 11)  # Limites de l'axe Y

data = [((9, 10), (0, 0), "crimson"),
        ((10, 3), (0, 0), "royalblue")]
blocked_cell = [(2, 6), (3, 6), (3, 5), (7, 8), (8, 8), (8, 7), (3, 1), (6, 4), (6, 3), (5, 7)]

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

print("OBSTACLES : OKAY")

# Affichage des trajectoires
for start, goal, color in data:
    x_list, y_list = unlink(a_star(start, goal, blocked=blocked_cell))
    plt.plot(x_list, y_list, color=color)

plt.grid(which="major")  # Affichage d'une grille pour plus de visibilité
plt.show()  # Affichage de la fenêtre
