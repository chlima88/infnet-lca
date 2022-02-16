import java.util.Scanner;

public class Desafio5 {
    static public void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        String nome;
        int vitorias;
        int empates;
        int pontos;

        System.out.print("Informe o nome do time: ");
        nome = scanner.nextLine();
        System.out.print("Informe a qtd de vitorias: ");
        vitorias = scanner.nextInt();
        System.out.print("Informe a qtd de empates: ");
        empates = scanner.nextInt();
        
        pontos = calculaPontos(vitorias, empates);
        impressao(nome, pontos);
    }

    static public void impressao(String nome, int pontos){
        System.out.print("O time " + nome + " est� com "
                        + pontos + " pontos.");
    }

    static public int calculaPontos(int vitorias, int empates){
        return vitorias * 3 + empates;
    }
}