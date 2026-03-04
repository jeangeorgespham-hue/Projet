import java.util.Scanner;
public class main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        boolean danielActif = false;
        boolean martinActif = false;
        compteBancaire daniel = new compteBancaire("Daniel", 1000.00);
        compteBancaire martin = new compteBancaire("Martin", 100.00);
        affichage.menu();
        System.out.println("1:" + daniel.afficherNom());
        System.out.println("2:" + martin.afficherNom());

        while (true) {
            int choixCompte = scanner.nextInt();
            if (choixCompte == 1){
                danielActif = true;
                break;
            }else if (choixCompte == 2){
                martinActif = true;
                break;
            }
        }
        if (danielActif){
            compteBancaire.utilisateurMethode(daniel);
        }else if (martinActif){
            compteBancaire.utilisateurMethode(martin);
        }
        scanner.close();
    }
}