import java.util.Scanner;

public class Desafio9 {

    static Scanner scanner = new Scanner(System.in);
    static String empresa;

    static public void main (String[] args){
        int mes;
        int qtdProdutos = 0;
        double ganhoTotal = 0;
        double ganhoMedio = 0;

        System.out.print("Informe o nome da empresa: ");
            empresa = scanner.nextLine();

        for(mes=1; mes<=2; mes++){
            System.out.print("Informe a quantidade do mes " + mes + ": ");
            qtdProdutos = qtdProdutos + scanner.nextInt();
            System.out.print("Informe os ganhos do mes " + mes + ": ");
            ganhoTotal = ganhoTotal + Double.parseDouble(scanner.nextLine());
        }

        impressao(empresa, qtdProdutos, ganhoTotal);
    }

    static public void impressao(String empresa, int qtdProdutos, double ganhoTotal){

        double ganhoMedio = calculaGanhoMedio(ganhoTotal, qtdProdutos);

        System.out.println("Empresa: " + empresa);
        System.out.println("Quantidade de produtos/ano: " + qtdProdutos);
        System.out.println("Ganho total/ano: " + ganhoTotal);
        System.out.println("Ganho medio anual: " + ganhoMedio);
    }

    static public double calculaGanhoMedio(double ganhoTotal, int qtdProdutos){
        return ganhoTotal / qtdProdutos;
    }

}