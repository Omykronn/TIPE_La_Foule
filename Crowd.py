import matplotlib.axes
from pandas import read_csv
from backup.tools import string_to_tuple, string_to_deque

from Person import Person


class Crowd:
    def __init__(self, N: int = 0, depart_list: list = [], arrive_list: list = []):
        """
        Définition des attributs des instances

        :param int N: Nombre de personnes dans la foule
        :param list depart_list: Liste des coordonnées des départs de chaque personne
        :param list arrive_list: Liste des coordonnées des arrivées de chaque personne
        :param list speed_list: Liste des vitesses de chacune des personnes
        """
        # On vérifie la concordance de N et des longueurs des listes
        assert len(depart_list) == len(arrive_list) == N

        self.size = N  # Enregistrement de la taille de la foule
        # Création de chacune des personnes
        self.subjects = [Person(depart_list[i], arrive_list[i]) for i in range(N)]

    def add_from_csv(self, csv_dir):
        data = read_csv(csv_dir, sep=";")
        n_person = len(data)

        self.size += n_person

        for i in range(n_person):
            new_person = Person(depart=string_to_tuple(data["depart"][i]),
                                destination=string_to_tuple(data["destination"][i]),
                                size=float(data["size"][i]),
                                priority=int(data["priority"][i]),
                                speed=int(data["speed"][i]))
            new_person.path = string_to_deque(data["path"][i])

            self.subjects.append(new_person)

    def update(self, axes: matplotlib.axes.Axes):
        """
        Mise à jour de la foule, en faisant avancer personne par personne

        :param matplotlib.axes.Axes axes: Axe sur lequel les disques doivent être ajoutés
        """
        i = 0

        while i < self.size:
            self.subjects[i].move()
            axes.add_patch(self.subjects[i])

            if self.subjects[i].has_reached_goal():
                print(self.subjects[i].name + " has reached his goal")  # Petit message lors de l'arrivée
                self.subjects.pop(i)  # Si on retire la personne en question, la taille de la liste va changer, et la
                self.size -= 1        # la personne suivant sera alors d'indice i, d'où la non-incrémentation de i
            else:
                i += 1

    def get_artists(self):
        return self.subjects
