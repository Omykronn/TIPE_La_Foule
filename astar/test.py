import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

from astar.algorithm import a_star
from creer_lab import lab


a = 32

x_interval = (-1, a)  # Limites de l'axe X
y_interval = (-1, a)  # Limites de l'axe Y

# Génération labyrinthe

start, goal = None, None
blocked_cell = []

raw = lab(a, 1, 1, "H")

print("LAB : OKAY")

raw_lab = raw[0]
start = (raw[1][1], raw[1][0])
goal = raw[2]


for i in range(a):
    for j in range(a):
        if raw_lab[i][j] == 3 or raw_lab[i][j] == 1 or raw_lab[i][j] == 2:
            blocked_cell.append((i, j))


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

print("OBSTACLES : OKAY")

# Affichage des trajectoires
data = a_star(start, goal, blocked=blocked_cell)

print("A* : OKAY")

for tag in data:
    x_list, y_list = unlink(data[tag].get_path())
    plt.plot(x_list, y_list)

plt.grid(which="major")  # Affichage d'une grille pour plus de visibilité
plt.show()  # Affichage de la fenêtre
