import java.util.Scanner;

public class inversion_mot {

    public static String inversion(String mot) {
        String inverse = "";
        for (int i = mot.length() - 1; i >= 0; i--) {
            inverse += mot.charAt(i);
        }
        return inverse;
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Tapez un mot :");
        String mot1 = scanner.nextLine();
        String mot1Inverser = inversion(mot1);
        System.out.println("Le mot inversé de " + mot1 + " est " + mot1Inverser);
        scanner.close();
    }
}