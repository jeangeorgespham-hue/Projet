def mot_de_passe_valide(mdp):
    majuscule = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    chiffre = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    Longueur_accepter = False
    majuscule_accepter = False
    chiffre_accepter = False
    longueur = 8
    if len(mdp) >= longueur:
        Longueur_accepter = True
    else:
        Longueur_accepter = False

    for x in mdp:
        if x in majuscule:
            majuscule_accepter = True
        if x in chiffre:
            chiffre_accepter = True
    if Longueur_accepter == True and majuscule_accepter == True and chiffre_accepter == True:
        return True
    else:
        return False

#Teste
mot_de_passe_1 = 'dzeefzeffeffgtdfv'
mot_de_passe_2 = 'dD1fe'
mot_de_passe_3 = 'aDDDeDDDzz'
mot_de_passe_4 = 'dzDfff1fffff'

print('Le mot de passe:', mot_de_passe_1 , 'est', mot_de_passe_valide(mot_de_passe_1))
print('Le mot de passe:', mot_de_passe_2 , 'est', mot_de_passe_valide(mot_de_passe_2))
print('Le mot de passe:', mot_de_passe_3 , 'est', mot_de_passe_valide(mot_de_passe_3))
print('Le mot de passe:', mot_de_passe_4 , 'est', mot_de_passe_valide(mot_de_passe_4)) 
