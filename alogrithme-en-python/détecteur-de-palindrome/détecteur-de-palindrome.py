
def detecteur_palindrome(mot):
    mot_inverse = ''
    for i in mot:
        mot_inverse = i + mot_inverse
    if mot_inverse.lower() == mot.lower():
        print("votre mot se lit pareil à l'envers")
    else:
        print("Votre mot ne se lit pas à l'envers", mot_inverse.lower())

mot_1 = "KayAk"
mot_2 = "ManGer"

detecteur_palindrome(mot_1)

detecteur_palindrome(mot_2)