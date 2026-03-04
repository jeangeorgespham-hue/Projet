Présentation du projet:

Ce projet est une application console en Java permettant de simuler la gestion de comptes bancaires. Il a été conçu avec une architecture orientée objet, séparant la logique métier de l'interface utilisateur.

Fonctionnalités:

Sélection de compte : Choisir entre différents utilisateurs au démarrage.

Dépôt d'argent : Ajouter un montant positif au solde actuel.

Retrait sécurisé : Retirer de l'argent avec vérification du solde disponible pour éviter les découverts.

Consultation du solde : Afficher le solde actuel du compte sélectionné.

Encapsulation : Les données sensibles (solde, nom) sont protégées par le modificateur private.

Structure:

compteBancaire.java : Contient la logique métier (calculs, gestion des montants).

affichage.java : Gère uniquement les menus et l'affichage textuel pour l'utilisateur.

main.java : Point d'entrée de l'application qui initialise les objets et lance la boucle principale.