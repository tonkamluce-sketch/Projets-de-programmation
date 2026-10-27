import java.util.Scanner;

public class MoyenneNotes {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] notes = new int[5];
        int somme = 0;

    for (int i = 0; i < 5; i++){
        System.out.println("Entrer une note : ");
        notes[i] = sc.nextInt();
        somme += notes[i];
    }
    
      double moyenne = (double) somme / notes.length;
      System.out.println("La moyenne est de : " + moyenne);

      sc.close();
    }
}

