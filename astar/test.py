import matplotlib.pyplot as plt
from astar.algorithm import a_star

""" Paramètres """
x_interval = (-30, 30)  # Limites de l'axe X
y_interval = (-12, 12)  # Limites de l'axe Y
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

# Affichage des trajectoires
x_list, y_list = unlink(a_star((10, 10), (0, 0)))
plt.plot(x_list, y_list)

plt.grid(which="major")  # Affichage d'une grille pour plus de visibilité
plt.show()  # Affichage de la fenêtre
