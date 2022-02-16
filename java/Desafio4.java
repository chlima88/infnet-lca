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
        nome = scanner.nextLine();
        System.out.print("Informe o sobrenome: ");
        sobrenome = scanner.nextLine();
        System.out.print("Informe a idade: ");
        idade = scanner.nextInt();
        System.out.print("Informe o salario: ");
        salario = scanner.nextDouble();
        System.out.print("Informe o desconto: ");
        desconto = scanner.nextDouble();

        impressao();

    }

    static public void impressao(){
        int anoNascimento = calculaAnoNascimento(idade);
        double salarioLiquido = calculaSalarioLiquido(salario, desconto);

        System.out.print("O funcionario " + nome + " " + sobrenome 
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