public class Desafio1 {
    
    static int a = 10;
    static int b = 20;
    
    public static void main(String args[]) {
        
        Desafio1.impressao("pre-processamento");
        Desafio1.processamento();
        Desafio1.impressao("pos-processamento");
    }
    
    private static void processamento(){
        int aux;
        
        aux = Desafio1.a;
        Desafio1.a = Desafio1.b;
        Desafio1.b = aux;
    }
    
    private static void impressao(String etapa){
        System.out.println("# " + etapa);
        System.out.println("Valor de A: " + Desafio1.a);
        System.out.println("Valor de B: " + Desafio1.b);
    }

}