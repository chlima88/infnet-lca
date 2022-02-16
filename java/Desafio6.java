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


    static int prova1;
    static int trabalho1;
    static int prova2;
    static int trabalho2;
    static int media;
    static String resultado;
    
    static Scanner scanner = new Scanner(System.in);


    static public void main(String[] args) {

        System.out.print("Informar o nome: ");
        Desafio6.nome = scanner.nextLine();
        System.out.print("Informar o curso: ");
        Desafio6.curso = scanner.nextLine();

        System.out.print("Informar a nota da Prova 1: ");
        prova1 = scanner.nextInt();
        System.out.print("Informar a nota do Trabalho 1: ");
        trabalho1 = scanner.nextInt();
        System.out.print("Informar a nota da Prova 2: ");
        prova2 = scanner.nextInt();
        System.out.print("Informar a nota do Trabalho 2: ");
        trabalho2 = scanner.nextInt();

        calculaResultado();

        imprimeResultado();

    }

    static public void calculaMedia() {
        media =  ( prova1 + trabalho1 + prova2 + trabalho2 ) / 2;
    }

    static public void calculaResultado() {
        calculaMedia();

        if (media >= 70) {
            resultado = "aprovado";
        } else {
            resultado = "reprovado";
        }

    }

    static public void imprimeResultado() {

        System.out.print("O aluno " + nome + " foi " + resultado + " no curso "
                        + curso + " com media " + media);
    }
}