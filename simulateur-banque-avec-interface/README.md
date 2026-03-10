Gestion de Compte Bancaire en Java
Ce projet est une application desktop permettant de simuler des opérations bancaires de base via une interface graphique Swing.

Fonctionnement
L'application se découpe en deux phases principales :

Sélection du compte : L'utilisateur choisit le compte à gérer.

Menu de gestion : Une fois le compte sélectionné, l'interface se met à jour pour proposer les options de dépôt, de retrait et de consultation du solde.

Structure du code
Le programme repose sur trois fichiers sources :

main.java : Initialise un objet compteBancaire avec un nom et un solde de départ, puis lance l'interface graphique.

compteBancaire.java : Contient la logique métier, notamment le stockage du solde et les méthodes de calcul pour les transactions.

affichage.java : Gère la création de la fenêtre, le placement des composants (boutons, labels) et les interactions avec l'utilisateur via des boîtes de dialogue.

Fonctionnalités incluses
Dépôt : Ajoute un montant positif au solde du compte.

Retrait : Déduit une somme du solde si les fonds sont suffisants.

Consultation : Affiche le solde actuel dans une fenêtre contextuelle.

Logs console : Chaque transaction réussie ou échouée est enregistrée dans le terminal pour le suivi technique.