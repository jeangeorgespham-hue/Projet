Nombre d'elements plus petits que l'element actuel
Ce projet contient une solution en C++ pour calculer, pour chaque nombre d'un tableau, combien d'autres nombres lui sont inferieurs.

Description du probleme
Etant donne un tableau d'entiers nums, l'objectif est de construire un nouveau tableau de meme taille. Pour chaque element nums[i], on compte combien d'elements nums[x] dans le tableau sont strictement plus petits que lui.

Algorithme
La solution utilise une double boucle imbriquee :

Premiere boucle : Elle parcourt chaque element du tableau un par un.

Deuxieme boucle : Pour l'element selectionne, elle parcourt a nouveau tout le tableau pour comparer sa valeur avec celle des autres.

Comptage : Si l'element de la deuxieme boucle est plus petit, on incremente un compteur.

Stockage : Le resultat du compteur est ajoute a la liste finale avant de passer a l'element suivant.