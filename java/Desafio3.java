import java.util.Scanner;

public class Desafio3 {

    static public void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        System.out.print("Informe quantos anos você tem: ");
        int anos = scanner.nextInt();
        System.out.print("Informe quantos meses você tem: ");
        int meses = scanner.nextInt();
        System.out.print("Informe quantos dias você tem: ");
        int dias = scanner.nextInt();

        int totalDias = Desafio3.calculaDias(dias, meses, anos);

        impressao(totalDias);
    }

    static public int calculaDias(int dias, int meses, int anos){
        return 365 * anos + 30 * meses + dias;
    }

    static public void impressao(int totalDias){
        System.out.print("Dias: " + totalDias);
    }    
}