def palindrome(mot):
    mot_inverser = ''
    for i in mot:
        mot_inverser = i + mot_inverser
    if mot_inverser.lower() == mot.lower():
        return True
    else:
        return False

#teste
print(palindrome('kayak'))
print(palindrome('bateau'))
print(palindrome('mot'))
