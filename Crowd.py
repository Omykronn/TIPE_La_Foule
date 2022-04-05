import matplotlib.axes

from Person import Person


class Crowd:
    def __init__(self, N: int, depart_list: list, arrive_list: list, speed_list: list):
        assert len(depart_list) == len(arrive_list) == len(speed_list) == N

        self.size = N
        self.subjects = [Person(depart_list[i], arrive_list[i], speed_list[i]) for i in range(N)]

    def update(self, axes: matplotlib.axes.Axes):
        i = 0

        while i < self.size:
            self.subjects[i].move()
            axes.add_patch(self.subjects[i])

            if self.subjects[i].has_reach_goal():
                print(self.subjects[i].name + " has reached his goal")
                self.subjects.pop(i)  # Si on retire la personne en question, la taille de la liste va changer, et la
                self.size -= 1        # la personne suivant sera alors d'indice i, d'où la non-incrémentation de i
            else:
                i += 1

    def get_artists(self):
        return self.subjects