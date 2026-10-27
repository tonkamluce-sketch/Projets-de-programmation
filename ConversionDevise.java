import java.util.Scanner;

public class ConversionDevise {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int dollarToFranc = 550;
        int euroToFranc = 650;
        float dollarToEuro = 0.89f;
        float euroToDollar = 1.12f;

        System.out.println("Entrer le type de conversion que vous voulez effectuer (Dollar, Euro, Franc) : ");
        String conversion = sc.nextLine().toLowerCase();

        if (conversion.equals("dollar")) {
            System.out.println("Entrer le montant que vous voulez convertir : ");
            float montant = sc.nextFloat();
            sc.nextLine();
            System.out.println("Vous voulez le convertir en quel type de monnaie ? (Franc, Euro) : ");
            String typeMontant = sc.nextLine().toLowerCase();
            
            if (typeMontant.equals("franc")) {
                float result = montant * dollarToFranc;
                System.out.println("Résultat : " + result + " FCFA");
            } 
            else if (typeMontant.equals("euro")) {
                float result = montant * dollarToEuro;
                System.out.println("Résultat : " + result + " EUR");
            }
            else {
                System.out.println("Option impossible.");
            }

        } 
        else if (conversion.equals("euro")) {
            System.out.println("Entrer le montant que vous voulez convertir : ");
            float montant = sc.nextFloat();
            sc.nextLine();

            System.out.println("Vous voulez le convertir en quel type de monnaie ? (Franc, Dollar) : ");
            String typeMontant = sc.nextLine().toLowerCase();

            if (typeMontant.equals("franc")) {
                float result = montant * euroToFranc;
                System.out.println("Résultat : " + result + " FCFA");
            }
            else if (typeMontant.equals("dollar")) {
                float result = montant * euroToDollar;
                System.out.println("Résultat : " + result + " USD");
            }
            else {
                System.out.println("Option impossible.");
            }

        } 
        else if (conversion.equals("franc")) {
            System.out.println("Entrer le montant que vous voulez convertir : ");
            float montant = sc.nextFloat();
            sc.nextLine();

            System.out.println("Vous voulez le convertir en quel type de monnaie ? (Dollar, Euro) : ");
            String typeMontant = sc.nextLine().toLowerCase();

            if (typeMontant.equals("dollar")) {
                float result = montant / dollarToFranc;
                System.out.println("Résultat : " + result + " USD");
            }
            else if (typeMontant.equals("euro")) {
                float result = montant / euroToFranc;
                System.out.println("Résultat : " + result + " EUR");
            } 
            else {
                System.out.println("Option impossible.");
            }

        } else {
            System.out.println("Devise non reconnue.");
        }

        sc.close();
    }
}