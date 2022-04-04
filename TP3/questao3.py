# Em um concurso de fantasias, os jurados precisam digitar os nomes dos 5 participantes e suas 
# respectivas notas, variando de 0 até 10. Crie uma função que leia os nomes dos participantes 
# e, ao final, apresente apenas o nome e a nota do vencedor.
#  
# Fluxo de exceção: 
# 
# O programa deve verificar se a nota da pessoa é maior ou igual a zero e menor ou igual a dez.


def ler_entrada(indice):
    nome = input(f"Informe o nome do {indice+1}º participante: ")     
    nota = float(input(f"Informe a nota do {indice+1}º participante: "))
 
    return {"nome": nome, "nota": nota}


def validar_entrada(entrada):

    if entrada["nome"] == '':
        raise ValueError({"error":"Nome inválido","msg":"O nome não pode ser vazio"})
    
    if entrada["nota"] < 0 or entrada["nota"] > 10:
        raise ValueError({"error":"Nota inválida","msg":"A nota deve ser um valor de 0 e 10"})

    return


def obter_vencedor():
    vencedor = {"nome": "", "nota":0}

    for participante in participantes:
        if vencedor["nota"] < participante["nota"]:
            vencedor = participante

    return vencedor


def obter_participantes():
    for indice in range(5):
        participante = ler_entrada(indice)
        validar_entrada(participante)
        participantes.append(participante)


def impressao():
    vencedor = obter_vencedor()
    print(f'O(a) vencedor(a) foi {vencedor["nome"]} com nota {vencedor["nota"]:.1f}')


participantes = []

try:
    obter_participantes()
    impressao()
except ValueError as err:
    print(err)
