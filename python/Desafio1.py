class Desafio1:
    a = 10
    b = 20

    @classmethod
    def imprime(cls, etapa):
        print(f'## {etapa} ##')
        print(f'Valor de a {cls.a}')
        print(f'Valor de b {cls.b}')

    @classmethod
    def processa(cls):
        aux = cls.a
        cls.a = cls.b
        cls.b = aux
    
    @classmethod
    def main(cls):
        cls.imprime("inicio")
        cls.processa()
        cls.imprime("final")
        


Desafio1.main()