// Desafio 07: Cálculo do imposto de renda

/*
Exiba a seguinte mensagem:

"O funcionário aaa da empresa bbb terá o valor de R$ccc a deduzir do salário" 
(quando a alíquota for superior a zero)

ou

"O funcionário aaa da empresa bbb está isento de qualquer dedução" 
(quando a alíquota for igual a zero)

Onde:
aaa: nome do funcionário; bbb: nome da empresa; ccc: parcela a deduzir

Utilize a seguinte tabela como base para calcular o valor da alíquota:

Base de cálculo; Alíquota
Até 1.903,98 = 0; 
De 1.903,99 até 2.826,65 = 7,50%; 
De 2.826,66 até 3.751,05 = 15%; 
De 3.751,06 até 4.664,68 = 22,50%; 
Acima de 4.664,68 = 27,50%

 */

import java.util.Scanner;

public class Desafio7 {

    static Scanner scanner = new Scanner(System.in);
    
    static public void main(String[] args) {
        String nome;
        String empresa;
        double salario;
        double valorDevido;
        
        System.out.print("Informe o nome do funcionario: ");
        nome = scanner.nextLine();
        System.out.print("Informe o nome da empresa: ");
        empresa = scanner.nextLine();
        System.out.print("Informe o salario do funcionario: ");
        salario = scanner.nextInt();

        valorDevido = calculaDesconto(salario);

        imprime(nome, empresa, valorDevido);
    }

    static public double calculaAliquota(double salario) {
        if (salario <= 1903.98) {
            System.out.println(salario);
            return 0;
        } else if (salario <= 2826.65) {
            return 7.5;
        } else if ( salario <= 3751.05) {
            return 15;
        } else {
            return 27.5;
        }
    }

    static public double calculaDesconto(double salario) {
        return salario * ( calculaAliquota(salario) / 100 );
    }

    static public void imprime(String nome, String empresa, double valorDevido){
        if ( valorDevido == 0 ) {
            System.out.print("O funcionario " + nome + " da empresa " 
                            + empresa + " esta isento");
        } else {
            System.out.print("O funcionario " + nome + " da empresa " 
                            + empresa + " tera o valor de " + valorDevido 
                            + " a deduzir do salario");

        }
    }
}