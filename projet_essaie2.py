#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      HEMMEA
#
# Created:     26/03/2021
# Copyright:   (c) HEMMEA 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os
#tout les mots du dictionnaire


liste_mots = []
curPath = os.path.abspath(os.path.split(_file_)[0])
with open(curPath + os.sep + 'dictionnaireMotsFrTriPython,txt','r', encoding="UTF-8") as inFile:
    for ligne in inFile.readline():
        while ligne != "":
            T.append(ligne.rstrip('\n'))
            ligne = f.readline()
print(liste_mot())

coups=11
reponse=random.liste_mots
while coups>0:
    proposition=input("Proposez une lettre} : ")
    if proposition in reponse:
        print("la lettre appartient au mot")
    else:
        print("pas bon")
        coups=coups-1
        print("_________")
