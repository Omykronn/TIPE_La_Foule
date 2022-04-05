import matplotlib.pyplot as plt
import matplotlib.animation as animation

from Crowd import Crowd


frame_rate = 30   # Nombre d'image par seconde
N = 5

depart = [(25, 5), (25, -5), (25, 0), (25, 10), (25, -10)]
goal = [(0, 0)] * N
vitesse = [2.1, 1.7, 1.3, 2.5, 1.5]


# ~~~~~~~~~~


def speed_convert(v):
    return v / frame_rate  # Traduit la vitesse réelle en une valeur en fonction de frame_rate


crowd = Crowd(N, depart, goal, [speed_convert(v) for v in vitesse])

fig = plt.figure()
ax = plt.axes(xlim=(-1, 30), ylim=(-10, 10), aspect="equal")
canva, = ax.plot([0], [0], 'bo', ms=5, color="silver")


def draw(j=0):
    crowd.update(ax)
    return crowd.get_artists()


anim = animation.FuncAnimation(fig, draw, init_func=draw, frames=360, interval=int(1000 / frame_rate), blit=True)

plt.grid()
plt.show()
