
print('Suite arithmetique = 1')
print('Suite geometrique = 2')
print('Suite par division = 3')
print('Suite par puissance = 4')
suite = int(input('Quelle suite?: '))
premier_terme =  int(input('Premier terme en u0?: '))
nombre_de_terme = int(input('Nombre de terme?: '))
raison = int(input('Raison?: '))
liste_suite = [premier_terme]

for n in range(nombre_de_terme):
    if suite == 1:
        premier_terme = premier_terme + raison
        liste_suite.append(premier_terme)
    elif suite == 2:
        premier_terme = premier_terme * raison
        liste_suite.append(premier_terme)
    elif suite == 3:
        premier_terme = premier_terme / raison
        liste_suite.append(premier_terme)
    elif suite == 4:
        premier_terme = premier_terme ** raison
        liste_suite.append(premier_terme)
    else:
        print('erreur')

for index , value in enumerate(liste_suite):
    print(index, ':', value)
