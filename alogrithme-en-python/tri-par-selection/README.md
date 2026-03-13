Description:

Le principe du tri par sélection est simple :

On divise la liste en deux parties : une partie déjà triée (au début) et une partie non triée.

On parcourt la partie non triée pour trouver l'élément le plus petit (index_min).

On échange ce plus petit élément avec le premier élément de la partie non triée.

On recommence l'opération en décalant la limite d'un cran vers la droite.

Utilisation:

Le script contient :

Une fonction swap(listeX, x, y) qui permet d'échanger deux éléments d'une liste selon leurs index.

Une double boucle for qui gère la recherche du minimum et le placement.