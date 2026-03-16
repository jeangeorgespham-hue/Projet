Description:

Au lieu de vérifier chaque élément un par un (recherche linéaire), la recherche binaire divise par deux l'espace de recherche à chaque étape :

On regarde l'élément au milieu de la liste.

Si c'est le bon, c'est fini.

S'il est plus grand que le nombre cherché, on recommence dans la moitié gauche.

S'il est plus petit, on recommence dans la moitié droite.

Le script affiche également le nombre de tentatives nécessaires pour arriver au résultat.

Utilisation:
Le script commence par trier la liste fournie (liste_nombre.sort()).

Il définit la fonction recherche_binaire(liste, nombre).

Il teste la présence de trois nombres (150, 904, 852).