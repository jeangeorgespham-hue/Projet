def inverse_tableau(liste):
    debut = 0
    fin = len(liste) - 1
    n = len(liste)
    if not liste:
        return None
    for x in range(n // 2):
        liste[debut] , liste[fin] = liste[fin] , liste[debut]
        debut = debut + 1
        fin = fin - 1
    return liste

liste_1 = [12 ,32, 23, 53, 123, 42]

print(inverse_tableau(liste_1))

liste_2 = []

print(inverse_tableau(liste_2))