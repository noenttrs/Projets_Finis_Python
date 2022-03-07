"""
Noé Nottaris - Celia Bistampoey
Jeu du Verger:
Entrée : -
Sortie :    - CSV de la simulation (nb de partie, nb de fois que les joueurs gagnent,
              nb de fois que le corbeau gagne).
            - Graphique Matplotlib
élément : 40 fruits; 6 faces du dé : 4 fruit, 1 panier, 1 corbeau; 9 pieces puzzles corbeau
"""
from matplotlib import pyplot as plt
import random
import operator

nbSimulation = 10000

regles = {'dé': ['jaune', 'bleu', 'violet', 'orange', 'panier', 'corbeau'],
          'arbres': {'jaune': 10,
                     'bleu': 10,
                     'violet': 10,
                     'orange': 10},
          'corbeau': 0}


def simulerParties(a):
    gagne = 0
    perdu = 0
    resultat = [[0], [0], [0]]
    for x in range(a):
        regles['arbres']['jaune'] = 10
        regles['arbres']['bleu'] = 10
        regles['arbres']['violet'] = 10
        regles['arbres']['orange'] = 10
        regles['corbeau'] = 0
        # print(regles)
        partie = True

        # lancement de la partie n.a
        while partie:
            coup = random.choice(regles['dé'])
            nbFruit = regles['arbres']['jaune'] + regles['arbres']['bleu'] + regles['arbres']['violet'] + regles['arbres']['orange']
            tri = sorted(regles['arbres'].items(), key=operator.itemgetter(1))
            #print(tri)
            # décompte des fruit et du puzzle
            if coup == 'panier':
                for k in range(2):
                    regles['arbres'][tri[3][0]] -= 1
                    tri = sorted(regles['arbres'].items(), key=operator.itemgetter(1))

            else:
                if coup == 'jaune':
                    if regles['arbres']['jaune'] >= 1:
                        regles['arbres']['jaune'] -= 1
                if coup == 'bleu':
                    if regles['arbres']['bleu'] >= 1:
                        regles['arbres']['bleu'] -= 1
                if coup == 'violet':
                    if regles['arbres']['violet'] >= 1:
                        regles['arbres']['violet'] -= 1
                if coup == 'orange':
                    if regles['arbres']['orange'] >= 1:
                        regles['arbres']['orange'] -= 1
                if coup == 'corbeau':
                    regles['corbeau'] += 1

            # print(regles['arbres']['jaune'],regles['arbres']['bleu'],regles['arbres']['violet'],regles['arbres']['orange'], regles['corbeau'])

            # vérification fin de la partie
            if nbFruit <= 0:
                gagne += 1
                partie = False
            elif regles['corbeau'] == 9:
                perdu += 1
                partie = False
        #print()

    resultat[0] = a
    resultat[1] = gagne
    resultat[2] = perdu
    return resultat


resultatFini = simulerParties(nbSimulation)

print(resultatFini)

fig = plt.figure()

plt.bar(0, (resultatFini[1] / resultatFini[0]) * 100, width=0.5)
plt.bar(1, (resultatFini[2] / resultatFini[0]) * 100, width=0.5)
plt.plot(0, 100)
plt.title("Graphique du ratio Gagné/Perdu pour " + str(nbSimulation) + " simulations")
plt.xticks([0, 1], ['Gagné', 'Perdu'])
plt.ylabel('Pourcentage (%)')
plt.show()
