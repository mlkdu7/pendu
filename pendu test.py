
print("Bienvenue dans le jeu du Pendu")
play=int(input("Tape 1 si tu veux jouer ! \n "))
if play == 1 :
     
    prénom=input("Quel est ton nom ?")
    print("\n")
    print("Salut", prénom)
    import random
    liste_mots=["laitue", "hareng", "jambon", "pharynx", "phoque", "langue",
                "stylo","agent","fromage","whisky","billet","boyaux",
                "laser","joystick","crane","joyeux","cahier","camping","argent",
                "rivage","physique","casque","orange","habituel"]


#système de vie (et début score)
    score = 0
    print("Tu as 6 vies")
    print("\n")
    vie = 6
    
#affichage des mots
    while play == 1 :
        vie = 6
        mot=(liste_mots[random.randint(0,24)])
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
            print("Tu as perdu")
#systéme de score
        elif grandeur==0 :
            print("Bravo ! Tu as trouvé le mot !")
            score=score+5
            print("Tu a gagné 5 points !")
        replay=int(input("Tape 1 pour rejouer, et sur 2 si tu veux quitter le jeu   "))
        if replay != 1 :
            break
    print(prénom,"vous avez un score de ",score)
    
    if score>=50 :
        print("WOW")
        time.sleep(1)
        print("Tu est un pro du Pendu !")
        
        
if play!=1:
    print(".....")
    import time
    time.sleep(1)
    print("Bah que voulez vous faire alors ?")
    time.sleep(2)
    print("Il devait avoir un easter egg ici")
    time.sleep(2)
    print("Mais le développeur a eu un peu la flemme")
    time.sleep(2)
    print("Désolé ;-)")
    
    

    
    
    

        
       
    

    





    
