#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mbenm
#
# Created:     07/02/2021
# Copyright:   (c) mbenm 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os

liste_mots = []
curPath = os.path.abspath(os.path.split(_file_)[0])
with open(curPath + os.sep + 'dictionnaireMotsFrTriPython,txt','r', encoding="UTF-8") as inFile:
    for ligne in inFile.readline():
        while ligne != "":
            T.append(ligne.rstrip('\n'))
            inFile.readline()
print(liste_mot())

""""#système de vie (et début score)
def score():
    score = 0
    print("Tu as 6 vies")
    print("\n")
    vie = 6

####################### programme principal #########################

prénom=input("Bienvenue dans le jeu du Pendu. Quel est ton prénom ?")
play=int(input("Tape 1 si tu veux trouver le mot et 2 si tu veux que l'ordinateur trouve le mot auquel tu pense ! \n "))

#l'ordinateur trouve le mot

while play ==2:
    int(input("Quel mot veut tu que l'ordinateur")

#affichage des mots
while play == 1 :
    vie = 6
    mot=(lire_mots[random.randint(0,)])
    longueur=len(mot)
    barre=["_ "]
    barre=barre*longueur
    grandeur=longueur
    print(longueur*"_ ")

#si une lettre est dans un mot, alors...

        while vie!=0 and grandeur!=0 :
            lettre_choisi = input("Choisi une lettre  ")
            print("\n")
            if lettre_choisi in mot :
                print("Bravo!")
                if lettre_choisi in barre:
                    print ("Tu l'as déja dit !")
                else:
                    position=int(mot.index(lettre_choisi))
                    barre.pop(position)
                    barre.insert(position,lettre_choisi)

                resultat = ' '.join(barre)

                print(resultat)
                grandeur=grandeur-1


            else:
                print("Raté")
                if grandeur==longueur :
                    print(longueur*"_ ")
                else:
                    print (resultat)
                vie=vie-1
                print("Il te reste",vie,"vies")
                print("\n")
        if vie==0 :
            print("Tu as perdu")"""

