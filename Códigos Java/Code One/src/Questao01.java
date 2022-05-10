import java.util.Scanner;

public class Questao01 {
    public static void main(String[] args) throws Exception {
        try (Scanner entrada = new Scanner(System.in)) {
            System.out.println("Digite um número entre 1 e 10: ");
            int numero = entrada.nextInt();

            for(int i = 1; i <= 10; i++){
                System.out.println("Tabuada de " + numero +": " +numero+ " * " +i+" = " +(numero*i));
            }
        }        
    }