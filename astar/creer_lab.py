from random import randint


def lab(cote, boucle, bat, entree) :
    """Génère un labyrinthe sous forme de tableau selon :
    Entrées :
        <cote> entier naturel >=7 -> Taille du labyrinthe
        <boucle> booléen -> une unique solution (0) / plusieurs (1)
        <bat> booléen -> arrivée aléatoire (0) / au centre (1)
        <entree> Chaine de caractère : "B", "H", "G" ou "D" -> Emplacement du début

    Sortie :
        <laby> tableau -> le labyrinthe
        <coordPJ> tuple d'entiers naturels -> coordonnées initiales du joueur dans le tableau
        <coordcentre> tuple d'entiers naturels -> coordonnées de l'arrivée du labyrinthe


    >>> [len(lab(x*10,boucle,zone,"D")[0]) for x in range (1,6)  for boucle in range(2) for zone in range (2)]
    [10, 10, 10, 10, 20, 20, 20, 20, 30, 30, 30, 30, 40, 40, 40, 40, 50, 50, 50, 50]
    >>> [lab(x*10,0,0,"B")[1][0]>0 and lab(x*10,0,0,"B")[1][0]<(10*x-1) and lab(x*10,0,0,"B")[1][1]==(10*x-2) for x in range (1,6)]
    [True, True, True, True, True]
    >>> [lab(10+x,0,1,"B")[2] for x in range (0,6)]
    [(5, 5), (5, 5), (6, 6), (6, 6), (7, 7), (7, 7)]
    """
    #Génèration d'un tableau de murs.
    laby=[[1]*cote for hauteur in range (cote)]

    #Placement de l'entrée aléatoirement sur le côté correspondant.
    porte=randint(1,cote-2)
    if entree=="G" :
        x=1
        y=porte
        laby[y][x-1]=2
        pointeur=0
        sens="D"
    elif entree=="D" :
        x=cote-2
        y=porte
        laby[y][x+1]=2
        pointeur=2
        sens="G"
    elif entree=="B" :
        x=porte
        y=cote-2
        laby[y+1][x]=2
        pointeur=3
        sens="H"
    elif entree=="H" :
        x=porte
        y=1
        laby[y-1][x]=2
        pointeur=1
        sens="B"

    #Placement de murs infranchissables tout autour du tableau aux autres endroits que la porte.
    for largeur in range(cote):
        for hauteur in range (cote):
            if largeur==0 or largeur==cote-1 or hauteur==0 or hauteur==cote-1 :
                if laby[hauteur][largeur]!=2 :
                    laby[hauteur][largeur]=3

    #Définition des coordonnées de départ du personnage.
    laby[y][x]=4
    coordPJ=(x,y)
    avance=[(1,0),(0,1),(-1,0),(0,-1)]

    #Placement de l'arrivée dans le mode où elle se trouve au milieu.
    if bat==1:
        for hauteur in range (cote//2-1,cote//2+2):
            for largeur in range (cote//2-1,cote//2+2):
                if hauteur==cote//2 and largeur==cote//2 :
                    laby[hauteur][largeur]=-1
                    coordcentre=(largeur,hauteur)
                else :
                    laby[hauteur][largeur]=0

    #Placement de l'arrivée dans le mode où elle est placée aléatoirement.
    else :
        eloignement=randint(cote//2,cote-4)
        perp=randint(2,cote-3)
        if pointeur %2==0 :
            for hauteur in range (perp-1,perp+2) :
                for largeur in range (coordPJ[0]+avance[pointeur][0]*eloignement-1,coordPJ[0]+avance[pointeur][0]*eloignement+2):
                    if hauteur==perp and largeur==coordPJ[0]+avance[pointeur][0]*eloignement :
                        laby[hauteur][largeur]=-1
                        coordcentre=(largeur,hauteur)
                    else :
                        laby[hauteur][largeur]=0
        else:
            for largeur in range (perp-1,perp+2) :
                for hauteur in range (coordPJ[1]+avance[pointeur][1]*eloignement-1,coordPJ[1]+avance[pointeur][1]*eloignement+2):
                    if largeur==perp and hauteur==coordPJ[1]+avance[pointeur][1]*eloignement :
                        laby[hauteur][largeur]=-1
                        coordcentre=(largeur,hauteur)
                    else :
                        laby[hauteur][largeur]=0

    #Traçage un labyrinthe depuis le départ en plaçant cases par cases aléatoirement jusqu'à l'arrivée.
    while 1 :
        pointeur=randint(0,3)
        valid= validation(boucle,laby,x+avance[pointeur][0],y+avance[pointeur][1],pointeur)
        if valid == 2 :
            laby[y+avance[pointeur][1]][x+avance[pointeur][0]]=4
            break
        elif valid :
            x+=avance[pointeur][0]
            y+=avance[pointeur][1]
            laby[y][x]=4
    return laby,coordPJ,coordcentre


def validation(boucle, laby, x, y, pointeur):
    """ Valide ou non une case candidatant en tant que sol :
    Entrées :
        <boucle> booléen -> une unique solution (0) / plusieurs (1)
        <laby> tableau -> l'etat actuel du labyrinthe en construction
        <x> et <y> entiers naturels -> coordonnées de la case
        <pointeur> entier 0<pointeur<4 -> symbolise la direction que prenait le "générateur" pour rentrer dans la case candidate
    Sortie :
        <valid> 1,2 ou 3 -> autorisant (1) ou non (0) la case, et déclarant la fin du labyrinthe(2)

    >>> validation(0,[[3,3,3],[3,3,3],[3,3,3]],1,1,3)
    0
    >>> validation(0,[[3,3,3],[1,0,3],[3,3,3]],0,1,0)
    2
    >>> [validation(0,[[1]*x for hauteur in range(x)],randint(1,x-2),randint(1,x-2),randint(0,3)) for x in range (10,20)]
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    >>> validation(0,[[1,1,1],[4,1,4],[1,1,1]],1,1,0)
    0
    >>> sum([validation(1,[[1,1,1],[4,1,4],[1,1,1]],1,1,0) for x in range (40)]) > 0
    True
    """
    #Maintient une case de sol en tant que sol si le générateur veut repasser dessus.
    if laby[y][x]==4 :
        return 1

    #Empêche de transformer toute autre case qu'un mur classique (soit les murs infranchissable et la porte) en sol.
    if laby[y][x]!=1 :
        return 0

    #Valide la nouvelle case si elle ne forme pas de boucle (ou si elle n'en forme une que en arrivant par en face si l'option boucleest activée)
    avance=[(1,0),(0,1),(-1,0),(0,-1)]
    valid=1
    for deplacement in range (4):
            if deplacement!=(pointeur+2)%4 :
                if laby[y+avance[deplacement][1]][x+avance[deplacement][0]]!=4 :
                    if laby[y+avance[deplacement][1]][x+avance[deplacement][0]]==0 :
                        #Envoie le signal de fin du labyrinthe quand le ring est atteint.
                        valid=2
                elif boucle==0 :
                    return 0
                else :
                    if deplacement!=pointeur or randint(0,2) :
                        return 0
    return valid

    return False


def initgrille(cote, coordPJ, laby, cave=0):
    """Initialise une grille se superposant au labyrinthe et indiquant en particulier l'emplacement du joueur et des coffres.
    Entrées :
        <cote> entier naturel = len(laby) -> Taille de la grille
        <coordPJ> tuple d'entiers naturels -> coordonnées initiales du joueur dans la grille
        <laby> tableau carré -> le labyrinthe
    Sortie :
        <grille> tableau -> la grille carré de côté <cote> se superposant au labyrinthe

    >>> initgrille(3,(1,1),[[4]*3 for hauteur in range(3)])
    [[-100, -100, -100], [-100, -100, -100], [-100, -100, -100]]
    >>> initgrille(10,(1,1),[[3, 3, 3, 3, 3, 3, 3, 3, 3, 3], [3, 4, 4, 3, 3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]])
    [[-100, -100, -100, -100, -100, -100, -100, -100, -100, -100], [-100, -100, 0, -100, -100, -100, -100, -100, -100, -100], [-100, -100, -100, -100, -100, -100, -100, -100, -100, -100], [-100, -100, -100, -100, -100, -100, -100, -100, -100, -100], [-100, -100, -100, -100, -100, -100, -100, -100, -100, -100], [-100, -100, -100, -100, -100, -100, -100, -100, -100, -100], [-100, -100, -100, -100, -100, -100, -100, -100, -100, -100], [-100, -100, -100, -100, -100, -100, -100, -100, -100, -100], [-100, -100, -100, -100, -100, -100, -100, -100, -100, -100], [-100, -100, -100, -100, -100, -100, -100, -100, -100, -100]]
    """
    #Création d'une grille vide.
    grille=[[-100]*cote for hauteur in range (cote)]

    #Placement des coffres.
    infocoffre=placements(cote,coordPJ,laby,cote//10)
    for element in infocoffre :
        grille[element[1]][element[0]]=0
    return grille


def initmonstres(cote, coordPJ, laby, cave=0):
    """Initialise une grille se superposant au labyrinthe et indiquant en particulier l'emplacement des monstres.
    Entrées :
        <cote> entier naturel = len(laby) -> Taille de la grille
        <coordPJ> tuple d'entiers naturels -> coordonnées initiales du joueur dans la grille
        <laby> tableau carré -> le labyrinthe
    Sortie :
        <monstres> tableau -> la grille des monstres de côté <cote>
        <infos> liste de tuples -> information sur les différents monstres : type, coordonnées, direction, PV

    >>> initmonstres(3,(1,1),[[4]*3 for hauteur in range(3)])
    ([[(0, 0), (0, 0), (0, 0)], [(0, 0), (0, 0), (0, 0)], [(0, 0), (0, 0), (0, 0)]], [])
    >>> initmonstres(10,(1,1),[[3, 3, 3, 3, 3, 3, 3, 3, 3, 3], [3, 4, 4, 3, 3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]])
    ([[(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)], [(0, 0), (0, 0), (1, 'H'), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)], [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)], [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)], [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)], [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)], [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)], [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)], [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)], [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]], [(2, 1, 1, 'H', 0, 1)])
    """
    #Création d'un tableau vide.
    monstres=[[(0,0)]*cote for hauteur in range (cote)]

    #Placement des monstres.
    if cave ==0 or len(cave)==0 :
        infos=placements(cote,coordPJ,laby,(cote//10)**2)
        for index in range(len(infos)) :
            monstres[infos[index][1]][infos[index][0]]=("octorok","H")
            infos[index]=(infos[index][0],infos[index][1],"octorok","H",0,2)
        return monstres,infos

    else :
        infotot=[]
        for element in cave :
            infos=placements(cote,coordPJ,laby,cave[element])
            for index in range(len(infos)) :
                monstres[infos[index][1]][infos[index][0]]=(element,"H")
                infotot.append((infos[index][0],infos[index][1],element,"H",0,2))
        return monstres,infotot


def placements(cote, coordPJ, laby, nombre):
    """Détermine l'emplacement des coffres ou d'autres éléméents à placer.
    Entrées :
        <cote> entier naturel = len(laby) -> Taille du labyrinthe
        <coordPJ> tuple d'entiers naturels -> coordonnées initiales du joueur dans la grille
        <laby> tableau carré -> le labyrinthe
        <nombre> entier naturel -> nombre d'éléments à placer
    Sortie :
        <coffre> liste de tuples -> coordonnées des coffres (ou d'autres choses à placer)

    >>> placements(3,(1,1),[[4,0,0],[0,4,0],[0,4,0]],2)
    [(0, 0), (1, 2)]

    >>> len(placements(3,(2,1),[[4,4,4],[4,4,4],[4,4,4]],5))
    5
    """
    #Compte le nombre de cases sol différentes de celle du personnage dans le labyrinthe.
    chemin=-1
    for x in range (cote):
        for y in range (cote):
            if laby[y][x]==4 :
                chemin+=1

    #Décide des emplacements des coffres sur les cases de sols.
    place=[]
    for coffres in range (nombre) :
        position_temp=randint(1,chemin)
        while appartient(position_temp,place):
            position_temp=randint(1,chemin)
        place.append(position_temp)

    #Relève les emplacements.
    coffres=[]
    for x in range (cote):
        for y in range (cote):
            if laby[y][x]==4 and (x!=coordPJ[0] or y!=coordPJ[1]):
                for coffre in range (nombre) :
                    place[coffre]+=-1
                    if place[coffre]==0 :
                        coffres.append((x,y))
    return coffres


def appartient(element, liste) :
    """Détermine si l'élément appartient à la liste.
    Entrées :
        <element> le dit élément
        <liste> la dite liste
    Sortie :
        Booléen -> appartient (1) /  n'appartient pas (0)

    >>> appartient("bob",[])
    0
    >>> appartient(0,[1,0,2])
    1
    >>> appartient("bob",[0,2,3])
    0
    >>> appartient("bob",[0,"bob",3])
    1
    """
    for elem in liste :
        if elem==element :
            return 1
    return 0
