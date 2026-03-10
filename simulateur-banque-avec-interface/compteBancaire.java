import java.util.Scanner;

import javax.swing.JOptionPane;
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
    public boolean retirer(double montant){

        if (montant > 0 && montant <= solde) {
            solde = solde - montant;
            System.out.println("Vous avez retiré "+ montant + " Euro.");
            return true;
        }else {
            System.out.println("Montant non valide.");
            return false;
        }
    }
    public double afficherSolde() {
        return solde;
    }
    public String afficherNom() {
        return nomCompte;
    }
}