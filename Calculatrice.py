
print('------------------')
print('---Calculatrice---')
print('------------------')

calcule_liste = []

print('Operateur = +, *, -, /')
print('Pour calculer "=" ou "stop"')
valide = True
correct = True
while True:
    if valide == True:
        try:
            nombre = float(input('Nombre: '))
            calcule_liste.append(nombre)
            correct = True
        except:
            print('Non valide')
            correct = False
            continue


    if correct == True:
        operateur = input('operateur: ')
        if operateur in ['+', '/', '*', '-']:
            valide = True
            calcule_liste.append(operateur)
        elif operateur == '='or operateur.lower() == 'stop':
            break
        else:
            valide = False
            print('Non valide')

expression = " ".join(map(str, calcule_liste))
result = eval(expression)
print('Le resultat de', expression,'est:', result)