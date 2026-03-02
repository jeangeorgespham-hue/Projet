import java.util.Scanner;

public class JeuAventure {
    //METHODE POUR DEMANDER LE CHOIX
    public static int saisie(Scanner scanner, String message, String message2) {
        while (true) {
                System.out.println(message);
                System.out.println(message2);
                int choix = scanner.nextInt();
                if (choix == 1 || choix == 2) {
                        return choix;
                }else {
                        System.out.println("Saisie invalide ! Tapez 1 ou 2.");
                }
        }
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        boolean jouer = true;

        //BOUCLE PRINCIPALE DU JEU
        while (jouer) {
            // Initialisation des variables de la partie
            String[] inventaire = new String[2];
            boolean salle = false;
            boolean grotte = false;
            boolean épéeMauditeTrouver = false;
            boolean ammuletteTrouver = false;

            //ETAPE 1 : LE CHOIX DU CHEMIN
                String chemin = "Tu vois deux chemin different.";
                String choix1 = "1: Tu prends à droite. : 2: Tu prends à gauche";
                int sorti1 = saisie(scanner , chemin , choix1);
                
                if (sorti1 == 1) {
                        System.out.println("Tu prends a droite et tu arrive devant un salle.");
                        salle = true;
                } else if (sorti1 == 2) {
                        System.out.println("Tu prend a gauche et tu arrive devant une grotte");
                        grotte = true;
                }

            //ETAPE 2 : EXPLORATION DU LIEU CHOISI
            
            //SALLE
            if (salle) {
                String salleMessage = "Tu vois une épée au loin.";
                String choix2A = "1: tu la prends / 2: Tu l’ignore et passe ton chemin.";
                int sorti2 = saisie(scanner , salleMessage , choix2A);
                if (sorti2 == 1) {
                        System.out.println("Tu saisie l’épée, elle est lourde...");
                        inventaire[0] = "épéeMaudite";
                }else if (sorti2 == 2) {
                        System.out.println("Tu passe ton chemin.");
                }
            } 
            //GROTTE
            else if (grotte) {
                String grotteMessage = "Tu arrive dans une grotte, il fait très sombre... Tu vois une ammulette.";
                String choix2B = "1: tu la prends / 2: tu passes ton chemin";
                int sorti2 = saisie(scanner , grotteMessage , choix2B);
                if (sorti2 == 1) {
                        System.out.println("Tu saisi l’ammulette, tu sens un courant d’air.");
                        inventaire[1] = "ammulette";
                }else if (sorti2 == 2) {
                        System.out.println("Tu passe ton chemin.");
                }
            }

            //ETAPE 3 : BOSS
            System.out.println("Tu arrive devant une arène un géant se dresse devant toi.");

            //verification de l'inventaire
            for (int i = 0 ; i < inventaire.length ; i++) {
                if (inventaire[i] != null) {
                        if (inventaire[i].equals("épéeMaudite")) {
                                épéeMauditeTrouver = true;
                        }
                        if (inventaire[i].equals("ammulette")) {
                                ammuletteTrouver = true;
                        }
                }
            }
            if (ammuletteTrouver) {
                System.out.println("L'amulette brille... Elle te protège! Tu es sauvé!! VICTOIRE.");
            }else if (épéeMauditeTrouver) {
                System.out.println("L'épée te consume... Tu es maudit. MORT.");
            }else {
                System.out.println("Tu n'as rien pour te défendre. MORT.");
            }

            //MENU DE FIN DE PARTIE
            String menuMessage = "/// Menu ///";
            String menuMessage2 = "1: Quitter / 2: Réessayer";
            
            int menu = saisie(scanner , menuMessage , menuMessage2);
            if (menu == 1) {
                jouer = false;
                System.out.println("Merci d'avoir joué !");
            } else if (menu == 2) {
                jouer = true;
            }
        }
        
        scanner.close();
    }
}