
def recherche_binaire(liste, nombre_rechercher):
    left = 0 
    right = len(liste) - 1

    mid = (left + right) // 2
    tentative = 0
    while left <= right:
        mid = (left + right) // 2
        tentative = tentative + 1
        if liste[mid] == nombre_rechercher:
            print("Le chiffre a était trouvé avec ", tentative," tentatives.")
            return True
        elif nombre_rechercher < liste[mid]:
            right = mid - 1
        else : 
            left = mid + 1
    print("Le chiffre n'a pas était trouvé en ",tentative," tentatives.")
    return False


liste_nombre = [748, 212, 59, 934, 441, 128, 856, 303, 672, 15, 889, 412, 567, 23, 771, 904, 335, 618, 47, 829, 156, 993, 401, 725, 88, 542, 219, 664, 37, 911, 483, 106, 759, 284, 631, 142, 877, 520, 95, 804, 367, 692, 18, 946, 427, 581, 74, 833, 250, 611, 498, 117, 782, 329, 656, 163, 892, 534, 42, 917, 381, 705, 29, 963, 451, 574, 91, 847, 236, 622, 509, 131, 794, 342, 678, 185, 908, 553, 56, 924, 397, 718, 41, 975, 468, 593, 102, 861, 264, 645, 521, 148, 816, 355, 689, 197, 932, 564, 67, 941, 418, 731, 52, 986, 479, 604, 115, 872, 277, 658, 535, 171, 827, 368, 701, 209, 954, 576, 81, 967, 431, 744, 63, 998, 491, 615, 126, 884, 289, 669, 548, 184, 839, 382, 712, 224, 979, 588, 94, 912, 445, 756, 75, 852, 316, 639, 525, 139, 801, 351]
liste_nombre.sort()
nombre_1 = 150

nombre_2 = 904

nombre_3 = 852

recherche_binaire(liste_nombre, nombre_1)
recherche_binaire(liste_nombre, nombre_2)
recherche_binaire(liste_nombre, nombre_3)




