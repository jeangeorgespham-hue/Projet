def afficher_ou_erreur(liste_a_tester):
    if liste_a_tester:
        print('===Liste des tâche===')
        for i, element in enumerate(liste_a_tester):
            print(f"{i} : {element}")
    else:
        print('La liste est vide!')

tache = []
choix = 0

while choix != 4:
    print('========MENU=========')
    print('1 : Ajouter une tâche')
    print('2 : Supprimer une tâche')
    print('3 : Afficher toutes les tâches')
    print('4 : Quitter')
    choix = int(input('Que est votre choix?: '))

    if choix == 1:
         ajouter = input('Quelle est la tâche que vous voulez ajouter?: ')
         tache.append(ajouter)
         print('Tâche ajouter!')
    elif choix == 2:
         supprimer = int(input('Quelle est le numéro de la tâche que vous souhaiter supprimer?: '))
         if 0 <= supprimer < len(tache):
              tache.pop(supprimer)
              print('Tâche supprimer!')
         else:
              print("L'index n'est pas valide!")
    elif choix == 3:
         afficher_ou_erreur(tache)
    elif choix == 4:
         print('Gestionnaire des tâches quitter.')
         break