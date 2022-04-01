# Desenvolva um programa que calcule a divisão de uma conta de consumo (conta de restaurante 
# ou bar), em reais, considerando o número de pessoas que estavam consumindo e a taxa de 
# serviço que será paga ao garçom.
# 
# Ao usuário do programa serão solicitados o valor total do consumo, em reais, o número total
# de pessoas e o percentual do serviço prestado, entre 0 e 100.
#
# Fluxo de execução: 
# 	• O programa deve verificar se o número total de pessoas é maior do que zero.
# 	• O programa deve verificar se o percentual do serviço está dentro do intervalo válido,
# de 0 a 100. 
# 	• Caso valores inválidos sejam digitados, deve ser exibida a mensagem de erro “Valor 
# inválido” e o programa deve ser interrompido.
# 
# Dica: Em Python, o valor monetário calculado ao final pode ser informado, na função print(), 
# usando vírgula como separador de casa decimal, em vez de pontos.
# 


def ler_entrada():
    try:
        consumo = float(input("Informe o valor total do consumo: "))
        num_pessoas = int(input("Informe o numero de pessoas: "))
        taxa_servico = float(input("Informe a taxa de serviço em % (entre 0 e 100): "))

    except ValueError as err:
        raise ValueError({"error": "Valor invalido!", "msg": err.args[0]})
    
    return {
        "consumo": consumo,
        "num_pessoas": num_pessoas,
        "taxa_servico": taxa_servico
    }


def validar_entrada(conta):

    if (conta["consumo"] <= 0):
        raise ValueError({"error": "Valor de consumo invalido", "msg": "O valor do consumo deve ser superior a zero"})

    if (conta["num_pessoas"] <= 0):
        raise ValueError({"error": "Numero de pessoas invalido", "msg": "O numero de pessoas deve ser superior a zero"})

    if (conta["taxa_servico"] < 0) or (conta["taxa_servico"] > 100):
        raise ValueError({"error": "Taxa de serviço inválida", "msg": "A taxa de serviço dever ser um valor de 0 a 100"})

    return


def fechar_conta(conta):
    total_da_conta = round(conta["consumo"] * (1 + conta["taxa_servico"] / 100), 2)
    valor_por_pessoa = round(total_da_conta/conta["num_pessoas"], 2)
    total_da_conta = formatar_valor(total_da_conta)
    valor_por_pessoa = formatar_valor(valor_por_pessoa)
    return {"valor_total": total_da_conta, "valor_pessoa": valor_por_pessoa}

def formatar_valor(valor):
    return f"{valor:.2f}".replace(".",",")

def impressao(conta):
    conta_total = fechar_conta(conta)

    print(f'O valor total da conta, com a taxa de serviço, será de R$ {conta_total["valor_total"]}')
    print(f'Dividindo a conta por {conta["num_pessoas"]} pessoa(s), cada pessoa deverá pagar R$ {conta_total["valor_pessoa"]}')


try:
    conta = ler_entrada()
    validar_entrada(conta)
    impressao(conta)
    
except Exception as err:
    print(err)