valeur1 = input ("valeur 1 :")
valeur2 = input ("valeur 2 :")
valeur1 = int(valeur1)
valeur2 = int(valeur2)
compteur = 1
if valeur1 < valeur2:
    ecriture = valeur1 + 1
    while compteur != valeur2-1:
        print (ecriture)
        compteur = compteur + 1
        ecriture = ecriture + 1

if valeur2 < valeur1:
    ecriture = valeur1 - 1
    while compteur != valeur1 - 1:
        print(ecriture)
        compteur = compteur + 1
        ecriture = ecriture - 1
if valeur1 == valeur2:
    print ("valeurs egales") 