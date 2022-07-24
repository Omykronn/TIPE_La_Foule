import matplotlib.axes
from tools import read_csv

from Person import Person


class Crowd:
    def __init__(self, csv_dir: str, move_resol: int = 10):
        """
        Définition des attributs des instances, selon un fichier CSV externe (pour plus de simplicité dans le cas d'une
        réitération avec les mêmes conditions

        :param str csv_dir: Chemin du fichier CSV (contenant les informations sur les Agents) à ouvrir
        :param int move_resol: Indice de qualité de la transition
        """
        self.subjects = []
        self.move_resol = move_resol

        # Lecture du fichier CSV
        data = read_csv(csv_dir)

        for info in data:
            # On crée chaque agent en fonction des informations données, ligne par ligne
            self.subjects.append(Person(name=info[0],
                                        depart=(int(info[4]), int(info[5])),
                                        destination=(int(info[6]), int(info[7])),
                                        priority=int(info[1]),
                                        speed=int(info[2]),
                                        color=info[3]))

        self.size = len(self.subjects)  # On définit la taille de la foule (nombre d'agents)

    def update(self, axes: matplotlib.axes.Axes, f):
        """
        Mise à jour de la foule, en faisant avancer personne par personne

        :param matplotlib.axes.Axes axes: Axe sur lequel les disques doivent être ajoutés
        """
        i = 0

        while i < self.size:
            if f % self.move_resol == 0 and f > 0:
                # Dans le cas où le numéro de frame f est multiple de self.move_resol, on fait avancer l'Agent à la case
                # suivante (et ceux uniquement pour f > 0 à cause d'un problème avec f = 0 dans l'animation)
                self.subjects[i].move()
            else:
                # Autrement, on effectue la transition case à case, dont les étapes sont indicées par le modulo de f par
                # self.move_resol
                self.subjects[i].half_move((f % self.move_resol) / self.move_resol)

            # On ajoute le disque représentant de l'Agent à l'objet axes de matplotlib
            axes.add_patch(self.subjects[i])

            if self.subjects[i].has_reached_goal():
                print("GOAL : " + self.subjects[i].name)  # Petit message lors de l'arrivée
                self.subjects.pop(i)  # Si on retire la personne en question, la taille de la liste va changer, et la
                self.size -= 1  # la personne suivant sera alors d'indice i, d'où la non-incrémentation de i
            else:
                i += 1

    def get_artists(self):
        """
        Renvoie la liste des Agents (nécessaire pour l'animation)
        """

        return self.subjects
