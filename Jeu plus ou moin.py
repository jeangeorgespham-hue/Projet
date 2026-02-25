#exo 11
import random
erreur = 0
historique = []

boucle = True
print('============================')
print('==== Jeu plus ou moins! ====')
print('============================')
print()
print('Entre combien et combien?')
print()
valeur1 = int(input('Nombre 1(Doit etre plus petit): '))
valeur2 = int(input('Nombre 2(Doit etre plus grand): '))
nombre = random.randint(valeur1,valeur2)

print('Trouve le nombre!')
reponse1 = int(input('Choisis un nombre: '))
if reponse1 == nombre:
    boucle = False
    print('Impressionnant du premier coup!')
    print('le nombre étais:', nombre)
elif reponse1 != nombre:
    erreur = erreur + 1
    historique.append(reponse1)
    if reponse1 < nombre:
        print('Plus grand!')
    elif reponse1 > nombre:
        print('Plus petit!')

while boucle == True:
    if erreur >= 20:
        print('Dommage le nombre étais:', nombre)
        break
    reponse2 = int(input('Réessaie!: '))
    if reponse2 == nombre:
        boucle = False
        if erreur <= 5:
            print('Bravo!')
        elif erreur <= 10:
            print('Pas mal!')
        elif erreur <= 15:
            print('Peu mieux faire!')
        print('le nombre étais:', nombre, 'et tu a fais', erreur, 'erreurs!')
    elif reponse2 != nombre:
        erreur = erreur + 1
        historique.append(reponse2)
        if reponse2 < nombre:
            print('Plus grand!')
        elif reponse2 > nombre:
            print('Plus petit!')

histo = input("Veut tu afficher l'historique?: ")
if histo.lower() == 'oui':
    for index , valeur in enumerate(historique):
        print('erreur',index + 1, ':', valeur)
    print("Merci d'avoir jouer!")
else:
    print("Merci d'avoir jouer!") 
