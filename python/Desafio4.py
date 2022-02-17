# Ler nome, sobrenome, idade, salario e desconto do funcionario
# Exiba a seguinte frase: "O funcion�rio aaa bbb nasceu em ccc e ganha R$ddd"

class Desafio4:

    nome = str( input("Informe o nome: "))
    sobrenome = str( input("Informe o sobrenome: "))
    idade = int( input("Informe o idade: "))
    salario = float( input("Informe o salario: "))
    desconto = float( input("Informe o desconto: "))

    @classmethod
    def calculaSalarioLiquido(cls):
        return cls.salario - cls.desconto
    
    @classmethod
    def calculaAnoNascimento(cls):
        return 2022 - cls.idade
    
    @classmethod
    def imprime(cls):
        print(f"O funcionario {cls.nome} {cls.sobrenome} nasceu em "
                f"{cls.calculaAnoNascimento()} e ganha {cls.calculaSalarioLiquido()}")

Desafio4.imprime()