import java.util.Scanner;

public class Desafio2 {

    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        System.out.print("Informe a altura do triangulo em cm: ");
        double altura = scanner.nextDouble();

        System.out.print("Informe a base do triangulo em cm: ");
        double base = scanner.nextDouble();

        double area = Desafio2.calculaArea(base, altura);
        Desafio2.impressao(area);

    }

    private static double calculaArea(double base, double altura){
        return (base * altura) / 2;
    }

    private static void impressao(double area){
        System.out.println("A área é de " + area + " centímetros");
    }
}