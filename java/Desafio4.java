import java.util.Scanner;

public class Desafio4 {

    static String nome = "charles";
    static String sobrenome = "costa";
    static int idade = 34;
    static double salario = 1000;
    static double desconto = 100;

    static public void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        System.out.print("Informe o nome: ");
        Desafio4.nome = scanner.nextLine();
        System.out.print("Informe o sobrenome: ");
        Desafio4.sobrenome = scanner.nextLine();
        System.out.print("Informe a idade: ");
        Desafio4.idade = scanner.nextInt();
        System.out.print("Informe o salario: ");
        Desafio4.salario = scanner.nextDouble();
        System.out.print("Informe o desconto: ");
        Desafio4.desconto = scanner.nextDouble();

        Desafio4.impressao();

    }

    static public void impressao(){
        int anoNascimento = calculaAnoNascimento(Desafio4.idade);
        double salarioLiquido = calculaSalarioLiquido(Desafio4.salario, Desafio4.desconto);

        System.out.print("O funcionario " + Desafio4.nome + " " + Desafio4.sobrenome 
                        + " nasceu em " + anoNascimento + " e ganha R$" 
                        + salarioLiquido );
    }

    static public double calculaSalarioLiquido(double salario, double desconto) {
        return salario - desconto;
    }

    static public int calculaAnoNascimento(int idade){
        return 2022 - idade;
    }
}