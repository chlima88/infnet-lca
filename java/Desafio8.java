import java.util.Scanner;

public class Desafio8 {
    static public String nome;
    static public String posicao;
    static public int camisa;
    static Scanner scanner = new Scanner(System.in);
    
    static public void main (String[] args){

        receberDados();
        posicao = obterPosicao(camisa);
        impressao(nome, posicao);
    }

    static public void receberDados() {
        System.out.print("Nome do jogador: ");
        nome = scanner.nextLine();
        System.out.print("Numero da camisa: ");
        camisa = scanner.nextInt();
    }

    static public void impressao(String nome, String posicao) {
        System.out.print("O jogador " + nome + " e um " + posicao);
    }

    static public String obterPosicao(int camisa){
        String posicao; 

        if (camisa == 1) {
            posicao = "goleiro";
        } else if ( camisa == 2 || camisa == 6 ) {
            posicao = "lateral";
        } else if ( camisa == 3 || camisa == 4 ) {
            posicao = "zagueiro";
        } else if ( camisa == 5 || camisa == 8 || camisa == 10 ){
            posicao = "meio-campista";
        } else if ( camisa == 2 || camisa == 6 ) {
            posicao = "atacante";
        } else {
            posicao = "reserva";
        }

        return posicao;
    }


}