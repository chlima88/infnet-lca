/*
Desafio 6

Exiba a seguinte mensagem: "O aluno xxx foi yyy no curso www com média zzz". Onde:
xxx: nome do aluno; yyy: aprovado/reprovado; www: nome do curso; zzz: média
A média deve ser calculada da seguinte forma:
= ((nota da primeira prova 7 + nota do primeiro trabalho 3) + (nota da segunda prova 6 + nota 
do segundo trabalho 4))2
Se a média do aluno for maior ou igual a 70, considere-o aprovado; caso contrário, reprovado.


 */

import java.util.Scanner;

public class Desafio6 {

    static String nome;
    static String curso;
    static double prova1;
    static double trabalho1;
    static double prova2;
    static double trabalho2;

    static public void main(String[] args) {

        receberDados();

        double media = calculaMedia();
        String resultado = calculaResultado(media);

        imprimeResultado(resultado);

    }

    static public void receberDados() {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Informar o nome: ");
        nome = scanner.nextLine();
        System.out.print("Informar o curso: ");
        curso = scanner.nextLine();

        System.out.print("Informar a nota da Prova 1: ");
        prova1 = Double.parseDouble(scanner.nextLine());
        System.out.print("Informar a nota do Trabalho 1: ");
        trabalho1 = Double.parseDouble(scanner.nextLine());
        System.out.print("Informar a nota da Prova 2: ");
        prova2 = Double.parseDouble(scanner.nextLine());
        System.out.print("Informar a nota do Trabalho 2: ");
        trabalho2 = Double.parseDouble(scanner.nextLine());
    }

    static public double calculaMedia() {
        return ( prova1 * 7 + trabalho1 * 3 + prova2 * 6 + trabalho2 * 4 ) / 2;
    }

    static public void calculaResultado(double media) {

        if (media >= 70) {
            return "aprovado";
        } else {
            return "reprovado";
        }

    }

    static public void imprimeResultado(String resultado) {

        System.out.print("O aluno " + nome + " foi " + resultado + " no curso "
                        + curso + " com media " + media);
    }
}