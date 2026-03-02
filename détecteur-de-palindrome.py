mot = input('Choisir un mot: ')
mot_inverse = ''
for i in mot:
    mot_inverse = i + mot_inverse

if mot_inverse.lower() == mot.lower():
    print("votre mot se lit pareil à l'envers")
else:
    print("Votre mot ne se lit pas à l'envers", mot_inverse)