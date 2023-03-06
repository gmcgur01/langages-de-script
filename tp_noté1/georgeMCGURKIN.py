#! /usr/bin/env python3

import random

def main():
    # print(Chaine("toto", "O"))
    # print(afficheListe(["a", "b", "c"]))
    # print(sous_liste([56, 7, 4, 8, 23, 89, 101, 78], 3))
    # print(minP([78, 101, 89, 23, 8, 4, 7, 56]))
    # print(TriLong(["bip", "toto", "azerty", "blablabla", "a", "allo"]))
    # print(LireCompter())
    # print(NbLignes("toto.txt"))
    Cartes(4)

def Chaine(s, c):
    return c.lower() in s.lower()

def afficheListe(L):
    return L[::-1]

def sous_liste(L, k):
    return L[::k]

def minP(L):
    return min(L[::2])

def TriLong(L):
    return sorted(L, key=len, reverse=True)

def LireCompter():
    freq = {}
    while True:
        for word in input().split():
            word = word.lower()
            if word == "fin":
                return freq
            elif word in freq:
                freq[word] += 1
            else:
                freq[word] = 1
        
def NbLignes(nom):
    count = 0
    with open(nom) as file:
        for line in file:
            if line.startswith("bip"):
                count += 1
    return count

def Cartes(n):
    cartes = newListe(n)

    gauche = 0
    droit = len(cartes) - 1

    joueur1 = []
    joueur2 = []

    tour_de_joueur1 = True

    while True:
        try:
            choix = input("Voulez-vous jouer contre l'ordinateur? [o/n] ")
            if choix == "o":
                j2_est_ordinateur = True
                break
            elif choix == "n":
                j2_est_ordinateur = False
                break
        except KeyboardInterrupt:
            return

    turns = []

    while gauche <= droit:
        afficheCartes(cartes, gauche, droit)

        if tour_de_joueur1:
            nom = "Joueur 1"
            liste_de_joueur = joueur1
        else:
            nom = "Joueur 2"
            liste_de_joueur = joueur2

        if not tour_de_joueur1 and j2_est_ordinateur:
            choix = ChoixOrdi(cartes, gauche, droit)
            print(f"L'ordinateur a choisi {choix}!")
        else:
            choix = ChoixUtil(nom)

        if isinstance(choix, int):
            while choix > 0 and len(turns) != 0:
                curr_turn = turns.pop()
                if curr_turn[0]:
                    joueur1.pop()
                else:
                    joueur2.pop()

                if curr_turn[1]:
                    droit += 1
                else:
                    gauche -= 1
                tour_de_joueur1 = not tour_de_joueur1

        elif choix == "droit":

            liste_de_joueur.append(cartes[droit])
            droit -= 1
            turns.append((tour_de_joueur1, True))
            tour_de_joueur1 = not tour_de_joueur1

        elif choix == "gauche":

            liste_de_joueur.append(cartes[gauche])
            gauche += 1
            turns.append((tour_de_joueur1, False))
            tour_de_joueur1 = not tour_de_joueur1
            
        else:
            break
    QuiGagne(joueur1, joueur2)

def newListe(n):
    return [random.randint(-50, 100) for _ in range(n)]

def QuiGagne(L1, L2):

    score_du_j1 = sum(L1)
    score_du_j2 = sum(L2)

    if score_du_j1 > score_du_j2:
        print("Félicitations au joueur 1, vous avez gagné!")
    elif score_du_j1 < score_du_j2:
        print("Félicitations au joueur 2, vous avez gagné!")
    else:
        print("C'est un match nul, personne n'a gagné!")

def ChoixOrdi(L, gauche, droit):
    if L[gauche] > L[droit]:
        return "gauche"
    else:
        return "droit"

def afficheCartes(L, g, d):
    print("Cartes: ", end="" )
    for i in range(g, d + 1):
        print(L[i], end=" ")
    print("")

def ChoixUtil(joueur):
    while True:
        try:
            choix = input(f"{joueur}, qu'est-ce que vous choisissez, droit ou gauche? [d/g] ").lower()
        except KeyboardInterrupt:
            return None

        if choix in ["droit", "d", "right", "r"]:
            return "droit"
        elif choix in ["gauche", "g", "left", "l"]:
            return "gauche"
        elif choix.startswith("revenir en arrière"):
            try:
                comps = choix.split()
                return int(comps[3])
            except IndexError:
                return 1
            except ValueError:
                pass
        print("Ce n'est pas un choix possible!")

if __name__ == "__main__":
    main()
