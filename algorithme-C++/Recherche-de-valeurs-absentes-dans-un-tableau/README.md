Recherche de nombres disparus
Ce projet contient une solution en C++ pour identifier les nombres manquants dans un tableau d'entiers.

Description du probleme
Etant donne un tableau d'entiers nums de taille N ou chaque element est compris entre 1 et N, l'objectif est de retourner une liste de tous les entiers entre 1 et N qui n'apparaissent pas dans le tableau.

Algorithme
La solution utilise une approche avec un tableau de marquage :

Initialisation : Un vecteur seen de taille N est cree et rempli de zeros.

Marquage : On parcourt le tableau d'entree. Pour chaque nombre present, on marque sa position correspondante dans le vecteur seen.

Collecte : On parcourt le vecteur seen. Si une position contient toujours un zero, cela signifie que le nombre correspondant est absent de la liste initiale.