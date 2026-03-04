import java.util.Scanner;
public class compteBancaire{
    private String nomCompte;
    private double solde;
    public compteBancaire(String nomCompte, double solde){
        this.nomCompte = nomCompte;
        this.solde = solde;
    }
    public void deposer(double montant){
        if (montant > 0){
            solde = solde + montant;
            System.out.println("Vous avez ajouté "+ montant + " Euro.");
        }
    }
    public void retirer(double montant){
        if (montant > 0 && montant <= solde) {
            solde = solde - montant;
            System.out.println("Vous avez retiré "+ montant + " Euro.");
        }else {
            System.out.println("Montant non valide.");
        }
    }
    public double afficherSolde() {
        return solde;
    }
    public String afficherNom() {
        return nomCompte;
    }
    public static void utilisateurMethode(compteBancaire nom){
        Scanner scanner = new Scanner(System.in);
        while (true){
          affichage.menuCompte();
          int choixMenu = scanner.nextInt();
          if (choixMenu == 1){
            System.out.println("Combien?");
            double montantDeposer = scanner.nextDouble();
            nom.deposer(montantDeposer);
          }else if (choixMenu == 2) {
            System.out.println("Combien?");
            double montantRetirer = scanner.nextDouble();
            nom.retirer(montantRetirer);
          }else if (choixMenu == 3) {
            System.out.println("Vous avez "+nom.afficherSolde()+ "euros.");
          }else if (choixMenu == 4){
            System.out.println("Merci aurevoir.");
            break;
          }else {
            System.out.println("Entrer un choix valide.");
          }
        }
    }
}