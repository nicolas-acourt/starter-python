print("Bonjour, quel âge as tu ?")
âge = input()
# "int" convertie une valeur texte en valeur chiffre.
âge = int(âge) 
if âge < 18:
    print("Tu es mineur")
if âge >= 18:
    print("Tu es majeur")
