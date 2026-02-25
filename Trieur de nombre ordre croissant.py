#exo 16

liste_nombre = []

for i in range(1,10+1):
    nombre = int(input('Choissiser un nombre: '))
    liste_nombre.append(nombre)
n = len(liste_nombre)

for i in range(n):
    echange = False
    for x in range(0,n - i - 1):
        if liste_nombre[x] > liste_nombre[x + 1]:
            liste_nombre[x], liste_nombre[x + 1] = liste_nombre[x + 1] , liste_nombre[x]
            echange = True
    if echange == False:
        break

print(liste_nombre)