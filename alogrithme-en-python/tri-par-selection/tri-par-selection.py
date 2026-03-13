def swap(listeX , x , y):
    listeX[x], listeX[y] = listeX[y], listeX[x]
    return listeX

liste_nombre = [124,353,123,143,53,1233,356,12,35,231,52]

for j in range(len(liste_nombre)-1):
    index_min = j
    for i in range(j +1, len(liste_nombre)):
        if liste_nombre[i] < liste_nombre[index_min]:
            index_min = i
    swap(liste_nombre, j , index_min)


print(liste_nombre)