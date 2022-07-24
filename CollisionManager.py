from random import randint

from tools import sub_vector2D, sum_vector2D


class CollisionManager:
    # On définit des constantes identificatrices pour chaque type de collisions
    NOTHING = 0  # Pas de collision détectée
    TOWARD1 = 1  # Les deux agents vont vers la même case
    TOWARD2 = 2  # Les deux agents inversent leurs cases
    AWAY_A = 3  # L'agent A est derrière l'agent B
    AWAY_B = 4  # L'agent B est derrière l'agent A

    # On définit les constantes identificatrices pour les reactions
    FORWARD = 5
    RIGHT = 6
    LEFT = 7
    SLOW = 8
    STOP = 9

    # Table de conversion de l'ordre au vecteur mouvement associé
    order_to_move = {(0, 1): {RIGHT: (1, 1), LEFT: (-1, 1)},
                     (0, -1): {RIGHT: (-1, -1), LEFT: (1, -1)},
                     (1, 0): {RIGHT: (1, -1), LEFT: (1, 1)},
                     (-1, 0): {RIGHT: (-1, 1), LEFT: (-1, -1)},
                     (1, 1): {RIGHT: (0, 1), LEFT: (1, 0)},
                     (-1, -1): {RIGHT: (-1, 0), LEFT: (0, -1)},
                     (-1, 1): {RIGHT: (-1, 0), LEFT: (0, 1)},
                     (1, -1): {RIGHT: (1, 0), LEFT: (1, 0)}}

    def __init__(self, crowd, obstacles: list = []):
        """
        Initialisation d'une Instance de CollisionManager

        :param Crowd crowd: Foule à gérer
        :param list obstacles: Obstacles à prendre en compte
        """

        self.crowd = crowd
        self.obstacles = obstacles

    def collision_prediction(self):
        """
        Détermination du type de collision s'il y a, calcul de la réponse et application de cette dernière.
        Et cela pour tous les agents
        """

        for i in range(self.crowd.size):
            for j in range(i + 1, self.crowd.size):  # On ne traite pas deux fois la même paire d'agent
                collision = self.type_of_collision(i, j)  # On détermine le type de collision, s'il y en a une

                # La réaction dépend du type de collision identifiée
                if collision == CollisionManager.TOWARD1 or collision == CollisionManager.TOWARD2:  # Cas des Towards
                    print("TOWARD COLLISION : {} ↔ {}".format(self.crowd.subjects[i].name, self.crowd.subjects[j].name))

                    # On détermine quel agent est prioritaire : soit par son attribut priority, ou aléatoirement
                    a, b = self.select(i, j)

                    # On détermine l'action à faire pour les deux agents
                    a_res, b_res = self.toward_response(a, b)

                    # On applique l'action respectif des deux agents
                    # Agent A
                    if a_res == CollisionManager.LEFT or a_res == CollisionManager.RIGHT:
                        self.crowd.subjects[a].change_path(a_res)

                    # Agent B
                    if b_res == CollisionManager.LEFT or b_res == CollisionManager.RIGHT:
                        self.crowd.subjects[b].change_path(b_res)

                elif collision == CollisionManager.AWAY_A:  # Cas des Aways où i est le percutant
                    print("AWAY COLLISION : {} → {}".format(self.crowd.subjects[i].name, self.crowd.subjects[j].name))
                elif collision == CollisionManager.AWAY_B:  # Cas des Aways où j est le percutant
                    print("AWAY COLLISION : {} → {}".format(self.crowd.subjects[j].name, self.crowd.subjects[i].name))

    def select(self, i: int, j: int):
        """
        Détermination de quel agent est prioritaire, en fonction de son attribut priority, ou aléatoirement

        :param int i: Index n°1
        :param int j: Index n°2
        :return int * int: Couple dans le même sens ou non, en fonction du tri
        """

        if self.crowd.subjects[i].priority > self.crowd.subjects[j].priority:  # Cas où i est prioritaire
            return i, j
        elif self.crowd.subjects[i].priority < self.crowd.subjects[j].priority:  # Cas où j est prioritaire
            return j, i
        else:  # Cas du tirage aléatoire
            if randint(0, 1) == 0:
                return i, j
            else:
                return j, i

    def type_of_collision(self, a: int, b: int):
        """
        Détermination du type de collision s'il y en a une

        :param int a: Index de l'Agent A
        :param int b: Index de l'Agent B
        :return int: Identifiant du type de collision
        """

        if self.crowd.subjects[a].get_next_position() == self.crowd.subjects[b].get_next_position():
            return CollisionManager.TOWARD1
        elif self.crowd.subjects[a].get_next_position() == self.crowd.subjects[b].get_position() \
                and self.crowd.subjects[b].get_next_position() == self.crowd.subjects[a].get_position():
            return CollisionManager.TOWARD2
        elif self.crowd.subjects[a].get_next_position() == self.crowd.subjects[b].get_position() \
                and self.crowd.subjects[a].speed > self.crowd.subjects[b].speed:
            return CollisionManager.AWAY_A
        elif self.crowd.subjects[b].get_next_position() == self.crowd.subjects[a].get_position() \
                and self.crowd.subjects[b].speed > self.crowd.subjects[a].speed:
            return CollisionManager.AWAY_B
        else:
            return CollisionManager.NOTHING

    def toward_response(self, a, b, rang: int = 1):
        """
        Arbre de réponse dans le cas d'une collision TOWARD

        :param int a: Index de l'Agent A
        :param int b: Index de l'Agent B
        :param int rang: Rang de la réponse à tester
        :return int * int: Couple des deux actions validées à appliquer
        """

        if rang == 1:
            next_move_a = CollisionManager.FORWARD
            next_move_b = CollisionManager.RIGHT
        elif rang == 2:
            next_move_a = CollisionManager.FORWARD
            next_move_b = CollisionManager.LEFT
        elif rang == 3:
            next_move_a = CollisionManager.RIGHT
            next_move_b = CollisionManager.FORWARD
        elif rang == 4:
            next_move_a = CollisionManager.LEFT
            next_move_b = CollisionManager.FORWARD
        elif rang == 5:
            next_move_a = CollisionManager.FORWARD
            next_move_b = CollisionManager.STOP
        else:
            next_move_a = CollisionManager.STOP
            next_move_b = CollisionManager.STOP

        # Vérification si les actions désignées conviennent au deux agents
        if self.check_for_reaction(a, next_move_a) and self.check_for_reaction(b, next_move_b):
            return next_move_a, next_move_b
        else:  # Si la vérification échoue, on teste une autre réaction, de rang inférieur
            return self.toward_response(a, b, rang + 1)

    def away_response(self, a: int, b: int, rang: int = 1):
        """
        Arbre de réponse dans le cas d'une collision AWAY

        :param int a: Index de l'Agent A
        :param int b: Index de l'Agent B
        :param int rang: Rang de la réponse à tester
        :return int * int: Couple des deux actions validées à appliquer
        """

        if rang == 1:
            next_move_a = CollisionManager.FORWARD
            next_move_b = CollisionManager.RIGHT
        elif rang == 2:
            next_move_a = CollisionManager.FORWARD
            next_move_b = CollisionManager.LEFT
        elif rang == 3:
            next_move_a = CollisionManager.RIGHT
            next_move_b = CollisionManager.SLOW  # TODO Ralentir pourrait causer un décalage dans le deque path

        # Vérification si les actions désignées conviennent au deux agents
        if self.check_for_reaction(a, next_move_a) and self.check_for_reaction(b, next_move_b):
            return next_move_a, next_move_b
        else:  # Si la vérification échoue, on teste une autre réaction, de rang inférieur
            return self.away_response(a, b, rang + 1)

    def check_for_reaction(self, i, order):
        """
        Vérification de la possibilitée de la réaction donnée à un agent

        :param int i: Index de l'Agent concerné
        :param int order: Identifiant de l'ordre donné
        :return bool: Validité ou non
        """
        if order == CollisionManager.SLOW or order == CollisionManager.STOP or order == CollisionManager.FORWARD:
            # Les ordres SLOW, STOP, TOWARD sont toujours considérés possible
            return True
        else:
            # On calcule le vecteur mouvement de l'Agent, afin de déterminer quel mouvement est sa droite/gauche
            move = sub_vector2D(self.crowd.subjects[i].get_next_position(), self.crowd.subjects[i].get_position())
            # Position à vérifier si libre, obtenue par la table de conversion order_to_move
            new_position = sum_vector2D(CollisionManager.order_to_move[move][order], self.crowd.subjects[i].get_position())

            # On vérifie si la future position n'est pas obstruée
            # TODO Voir si pas plus de contrainte
            return new_position not in self.obstacles
