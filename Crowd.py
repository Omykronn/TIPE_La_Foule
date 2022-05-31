import matplotlib.axes

from Person import Person


class Crowd:
    def __init__(self, N: int, depart_list: list, arrive_list: list):
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
