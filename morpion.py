#!/usr/bin/python
# -*- coding: utf-8 -*-

# Le Morpion, aussi appelé “tic-tac-toe” ou “oxo” en Belgique, est un jeu
# très courant et facile à jouer. Le principe du jeu est simple. C’est un
# jeu au tour par tour, où le but est d’aligner un trio de cercles ou de croix
# en diagonale, horizontalement ou verticalement sur une grille de 3×3 carrés
# pour obtenir la victoire.

# Le défi de la création de ce jeu consiste principalement à se familiariser
# avec l’indexation des tableaux en 2D et à comprendre comment vérifier les
# alignements en diagonale. Une fois ces problèmes résolus, le codage devrait
# être simplifié.

# Création du plateau et remplissage par des espaces
plateau = []
for _ in range(0, 9):
    plateau.append(" ")


def afficherPlateau(plateau, joueur=None):
    """
    Affiche le plateau de jeu en utilisant les symboles contenus dans la liste 'plateau'.
    Si le paramètre 'joueur' est fourni, affiche un message indiquant que ce joueur a gagné.
    """
    print(" " + plateau[0] + " | " + plateau[1] + " | " + plateau[2] + " ")
    print("---|---|---")
    print(" " + plateau[3] + " | " + plateau[4] + " | " + plateau[5] + " ")
    print("---|---|---")
    print(" " + plateau[6] + " | " + plateau[7] + " | " + plateau[8] + " ")

    if joueur:
        print("Le joueur {} a gagné !".format(joueur))


def main():
    joueur = "X"
    tour = 0

    while True:
        afficherPlateau(plateau)
        mouvement = int(input("Tour du joueur {}. Entrez un nombre de 1 à 9 :"
                              .format(joueur)))

        # On soustraie 1 au mouvement car le tableau est indexé de 0 à 8
        mouvement -= 1

        # On vérifie qu'on peut jouer dans la case demandée
        if plateau[mouvement] == " ":
            plateau[mouvement] = joueur
            tour += 1
        else:
            print("Le case est déjà occupée !")
            continue

        # Vérification si les case sont pleines et du même symbole
        if plateau[0] == plateau[1] == plateau[2] != " " \
                or plateau[3] == plateau[4] == plateau[5] != " " \
                or plateau[6] == plateau[7] == plateau[8] != " " \
                or plateau[0] == plateau[3] == plateau[6] != " " \
                or plateau[1] == plateau[4] == plateau[7] != " " \
                or plateau[2] == plateau[5] == plateau[8] != " " \
                or plateau[0] == plateau[4] == plateau[8] != " " \
                or plateau[2] == plateau[4] == plateau[6] != " ":
            afficherPlateau(plateau, joueur)
            break

        # Si on arrive au tour 9, ça signifie que tout est rempli et qu'il n'y
        # a pas de gagnant.
        if tour == 9:
            print("Egalité")
            break

        if joueur == "X":
            joueur = "O"
        else:
            joueur = "X"

main()
