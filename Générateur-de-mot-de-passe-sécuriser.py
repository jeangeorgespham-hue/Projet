#exo18
import random
lettre_liste =['a', 'z', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'm', 'l', 'k', 'j', 'h', 'g', 'f', 'd', 's', 'q', 'w', 'x', 'c', 'v', 'b', 'n', 'A', 'Z', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'M', 'L' ,'K', 'J', 'H', 'G', 'F', 'D', 'S', 'Q', 'W', 'X','C','V','B','N']
nombre_liste =['1','2','3','4','5','6','7','8','9']
caractere_speciaux_liste =['!', '@', '#', '$', '%', '^', '&', '*', '(', ')','-', '_', '+', '=', '[', ']', '{', '}', '|', '\\',';', ':', '\'', '"', ',', '.', '<', '>', '/', '?','€', '£', '¥', '§', '°', '©', '®', '™', '…','~', '`']
liste_nombre_lettre = nombre_liste + lettre_liste
choixfait = set()
choix = 0
choix_2 = 0
choix_3 = 0
longueur = int(input('Longueur du mot de passe: '))
print('0) Aucun')
print('1) Lettres')
print('2) Nombre')
print('3) Caractere speciaux')

while True:
        choix = int(input('Quelle est votre 1er choix: '))
        if choix in [1,2,3,0]:
                if choix != 0:
                        choixfait.add(choix)
                        break
                elif choix == 0:
                        break
                else:
                        print('Incorrect veuiller choisir un nombre entre 0,1,2,3')
while True:
        choix_2 = int(input('Quelle est votre 2eme choix: '))
        if choix_2 in [1,2,3,0]:
                if choix_2 != 0 and choix_2 not in choixfait:
                        choixfait.add(choix_2)
                        break
                elif choix_2 == 0:
                        break
                elif choix_2 in choixfait:
                        print('Incorrect')
                else:
                        print('Incorrect veuiller choisir un nombre entre 0,1,2,3')

while True:
        choix_3 = int(input('Quelle est votre 3eme choix: '))
        if choix_3 in [1,2,3,0]:
                if choix_3 != 0 and choix_3 not in choixfait:
                        choixfait.add(choix_3)
                        break
                elif choix_3 == 0:
                        break
                elif choix_3 in choixfait:
                        print('Incorrect')
                else:
                        print('Incorrect veuiller choisir un nombre entre 0,1,2,3')
liste_complete = []

if 1 in choixfait:
        liste_complete.extend(lettre_liste)
if 2 in choixfait:
        liste_complete.extend(nombre_liste)
if 3 in choixfait:
        liste_complete.extend(caractere_speciaux_liste)

if not liste_complete:
        print('Aucun mot de passe ne peut etre génerer')

if liste_complete:
        print('Votre mot de passe est:')
        for i in range(longueur):
                x = random.choice(liste_complete)
                print(x , end='')