nombre_list = []
boucle = True
result = 0
while boucle == True:
    nombre = input('Nombre: ')
    if nombre.lower() == 'stop':
        boucle = False

    if nombre.isdigit():
        nombre_list.append(int(nombre))
longueur = len(nombre_list)
print('Il y a', longueur, 'valeurs')

for i in nombre_list:
    result = result + i

moyenne = result / longueur

print('La moyenne est',moyenne)

maxi = max(nombre_list)
mini = min(nombre_list)

print('La valeur la plus haute est', maxi)
print('La valeur la plus Basse est', mini) 