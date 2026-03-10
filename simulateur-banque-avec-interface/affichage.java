import javax.swing.*;
import java.awt.event.*;
import java.awt.*;

public class affichage {
    public static void creerFenetre(compteBancaire compte){

        JFrame frame = new JFrame("Banque");
        frame.setSize(600,400);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(null);

        JLabel titreBanque = new JLabel("MA BANQUE");
        titreBanque.setBounds(225, 20, 400, 50);
        titreBanque.setFont(new Font("Arial", Font.BOLD, 25));
        frame.add(titreBanque);

        JLabel selection = new JLabel("SELECTIONNER UN COMPTE :");
        selection.setBounds(220, 120, 400, 50);
        frame.add(selection);

        JLabel gestion = new JLabel("GESTION");
        gestion.setBounds(275, 100, 400, 50);

        JButton boutonCompte = new JButton(compte.afficherNom());
        boutonCompte.setBounds(245, 180, 100,25);
        frame.add(boutonCompte);

        boutonCompte.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {

                frame.add(gestion);
                JButton boutonDeposer = new JButton("Déposer");
                boutonDeposer.setBounds(150, 150, 120, 30);

                JButton boutonRetirer = new JButton("Retirer");
                boutonRetirer.setBounds(330, 150, 120, 30);

                JButton boutonSolde = new JButton("Afficher solde");
                boutonSolde.setBounds(240, 220, 120, 30);

                boutonDeposer.addActionListener(ev -> {
                    String input = JOptionPane.showInputDialog(frame, "Somme à déposer :");
                    if (input != null) {
                        double montant = Double.parseDouble(input);
                        compte.deposer(montant);
                        JOptionPane.showMessageDialog(frame, "Dépôt réussi !");
                    }
                });

                boutonRetirer.addActionListener(ev -> {
                    String input = JOptionPane.showInputDialog(frame,"Somme à retirer:");
                    if (input != null) {
                        double montant = Double.parseDouble(input);
                        if (compte.retirer(montant)) {
                            JOptionPane.showMessageDialog(frame, "Retrait réussi !");
                        }else {
                            JOptionPane.showMessageDialog(frame, "Retrait impossible !");
                        }
                    }
                });

                boutonSolde.addActionListener(ev -> {
                    JOptionPane.showMessageDialog(frame, "Solde actuel : " + compte.afficherSolde() + " €");
                });


                frame.remove(selection);
                frame.remove(boutonCompte);
                frame.add(boutonSolde);
                frame.add(boutonDeposer);
                frame.add(boutonRetirer);

                frame.repaint();
                boutonCompte.setEnabled(false);
                
                System.out.println("Menu de gestion affiché pour " + compte.afficherNom());
            }
        });


        frame.setVisible(true);
    }
}
