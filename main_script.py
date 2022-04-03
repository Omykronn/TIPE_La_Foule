import matplotlib.pyplot as plt
import matplotlib.animation as animation

from Crowd import Crowd


frame_rate = 30   # Nombre d'image par seconde
speed_convert = lambda v: v / frame_rate  # Traduit la vitesse réelle en une valeur en fonction de frame_rate

fig = plt.figure()
ax = plt.axes(xlim=(-10, 10), ylim=(-10, 10))
people, = ax.plot([0], [0], 'bo', ms=5)

N = 1

depart = [(5, 9)]
goal = [(0, 0)] * N
vitesse = [2.1]

crowd = Crowd(N, depart, goal, [speed_convert(v) for v in vitesse])


def init():
    """
    Initialisation de l'environnement avec le début de l'animation

    :return: None
    """

    x, y = crowd.print()

    people.set_data(x, y)

    return people,


def animate(j):
    """
    Redessine l'environnement pour chaque image

    :param int j: Numéro de l'image dessinée
    :return: None
    """

    crowd.update()
    x, y = crowd.print()

    people.set_data(x, y)

    return people,


anim = animation.FuncAnimation(fig, animate, init_func=init, frames=360, interval=int(1000 / frame_rate), blit=True)

plt.show()
