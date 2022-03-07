from random import randint
import pprint
from os import system, name
import time
import PySimpleGUI as sg


# Fonction

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def entree():
    b = False
    while not b:
        codeRentre = input('Rentre un code couleur : ')
        if len(codeRentre) != 4:
            sg.popup_ok('Le code rentré est invalide,ton code ne fait pas 4 caractères, recommence.')
        elif not codeRentre.isdigit():
            sg.popup_ok('Le code rentré est invalide, tu a rentré une lettre, recommence.')
        elif len(codeRentre) != len(set(codeRentre)):
            sg.popup_ok('Le code rentré est invalide, tu a fait une répétition, recommence.')
        else:
            b = True
            return codeRentre


def creationCodeCache():  # fonction de choix aléatoire des couleurs
    colors = [t for t in range(8)]
    CouleursChoisies = []
    for u in range(4):
        hasard = randint(0, len(colors) - 1)
        ChoixCouleur = colors.pop(hasard)
        CouleursChoisies.append(ChoixCouleur)
    return CouleursChoisies


def verifCode(a, b):  # fonction de vérification du code entré
    codeCacheList = a
    codeEntreList = b
    c = []
    if codeEntreList == codeCacheList:
        win = 'win'
        return win
    else:
        for q in range(4):
            try:
                test = codeCacheList.index(codeEntreList[q])
                if codeEntreList[q] == codeCacheList[q]:
                    c.append(2)
                else:
                    c.append(1)
            except:
                c.append(0)
        return c

# --- Initialisation ---
sg.theme('White')


# Création du plateau

plateau = [[[0, 0, 0, 0], [0, 0, 0, 0]],
           [[0, 0, 0, 0], [0, 0, 0, 0]],
           [[0, 0, 0, 0], [0, 0, 0, 0]],
           [[0, 0, 0, 0], [0, 0, 0, 0]],
           [[0, 0, 0, 0], [0, 0, 0, 0]],
           [[0, 0, 0, 0], [0, 0, 0, 0]],
           [[0, 0, 0, 0], [0, 0, 0, 0]],
           [[0, 0, 0, 0], [0, 0, 0, 0]],
           [[0, 0, 0, 0], [0, 0, 0, 0]],
           [[0, 0, 0, 0], [0, 0, 0, 0]],
           [[0, 0, 0, 0], [0, 0, 0, 0]],
           [[0, 0, 0, 0], [0, 0, 0, 0]],
           [[0, 0, 0, 0], [0, 0, 0, 0]]]

# --- Lancement de la partie ---
clear()
print('''
 ____               _                __  __  _             _ 
|  _ \  _   _  ___ | |_   ___  _ __ |  \/  |(_) _ __    __| |
| |_) || | | |/ __|| __| / _ \| '__|| |\/| || || '_ \  / _` |
|  __/ | |_| |\__ \| |_ |  __/| |   | |  | || || | | || (_| |
|_|     \__, ||___/ \__| \___||_|   |_|  |_||_||_| |_| \__,_|
        |___/                                                
''')

time.sleep(4)
clear()

codeCache = creationCodeCache()
pprint.pprint(plateau, indent=5, depth=None, width=100)
print("Les couleurs sont : 0, 1, 2, 3, 4, 5, 6, 7. Aucune répétition n'est possible.")

for x in range(12):

    codeEntre = entree()
    listCodeEntre = [int(x) for x in codeEntre]

    indice = verifCode(codeCache, listCodeEntre)

    if indice == 'win':
        print("Bravo tu a gagné, le code était : ", codeCache)
        exit()

    for i in range(4):
        plateau[x][0][i] = listCodeEntre[i]
    for y in range(4):
        plateau[x][1][y] = int(indice[y])

    clear()  # rafraichissement du terminal

    pprint.pprint(plateau, indent=5, depth=None, width=100)
    print("Les couleurs sont : 1, 2, 3, 4, 5, 6, 7, 8. Aucune répétition n'est possible.")

print('Nombre de tour épuisé désolé\n le code était : ', codeCache)
