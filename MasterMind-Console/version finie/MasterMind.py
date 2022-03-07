import PySimpleGUI as sg
from random import randint

from PySimpleGUI.PySimpleGUI import Col

sg.theme('Default1')

couleurs = ['B', 'R', 'M', 'J', 'O', 'V', 'G', 'N']
couleurs1 = ['B', 'R', 'M', 'J', 'O', 'V', 'G', 'N']

"""LigneCachee = []

for x in range(4):
    b = randint(0,len(couleurs)-1)
    a = couleurs.pop(b)
    LigneCachee.append(a)
    lignemistere = ''.join(LigneCachee)
    coucou = list(lignemistere)

print(LigneCachee, lignemistere, coucou)"""

layout = [[sg.Text('Ceci est un mastermind, quatre couleurs sont choisies au hasard')],
          [sg.Text('Il y a 8 couleurs : Bleu, Rouge, Marron, Jaune, Orange, Vert, Gris et Noir')],
          [sg.Text('Vous noterais B pour Bleu, R pour Rouge, etc')],
          [sg.Text('Entrez votre ligne sous forme de texte, ex : RBMJ (Rouge, Bleu, Marron, Jaune')],
          [sg.Button('Ok'), sg.Button('Cancel')]]

jeu = []



def verif(ligne):
    pass


window = sg.Window("Page D'entrée", layout)
while True:
    i = 1
    event, values = window.read()
    if event == 'Ok':
        window = sg.Window('Simple data entry window', jeu)
    if event == 'OK':
        window.update()
    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break

window.close()
