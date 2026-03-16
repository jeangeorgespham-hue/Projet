def recherche_max(liste):
    index_max = 0
    if not liste:
        return None
    for i in range(len(liste)):
        if liste[index_max] < liste[i]:
            index_max = i
    return liste[index_max]

liste_1 = [2,4,6,67,4,2,5,150]


print("La valeur maximal de la liste 1 est:", recherche_max(liste_1))

liste_2 = [23,24,66,46,947,23,235,132]

print("La valeur maximal de la liste 2 est:", recherche_max(liste_2))

liste_3 = []

print("La valeur maximal de la liste 3 est:", recherche_max(liste_3))