#  Desenvolva uma função que recebe a idade de uma pessoa e informe se essa pessoa é:
# 		1. Eleitor obrigatório (18 anos completos e menos de 70 anos de idade)
# 		2. Eleitor facultativo (16 anos completos e menos de 18 anos ou 70 anos de idade 
#       ou mais).
# 		3. Não tem direito a voto (menor de 16 anos).
# 
# Fluxo de exceção: 
# 
# O programa deve verificar se a idade da pessoa é maior do que zero.


def verificar_idade(idade):
    if idade < 16:
        return "Não tem direito a voto."
    elif idade < 18 or idade >= 70:
        return "Eleitor facultativo."
    else:
        return "Eleitor obrigatório."

def impressao(idade):
    resultado = verificar_idade(idade)
    print(resultado)

def ler_entrada():
    try:
        idade = int(input("Informe a idade: "))
        if idade < 0: 
            raise(ValueError('Idade não pode ser menor que 0'))
        else:
            return idade

    except ValueError as err:
        print(f"Idade inválida! {err}")
        exit(1)

impressao(ler_entrada())