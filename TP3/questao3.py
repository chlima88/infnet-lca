# Em um concurso de fantasias, os jurados precisam digitar os nomes dos 5 participantes e suas 
# respectivas notas, variando de 0 até 10. Crie uma função que leia os nomes dos participantes 
# e, ao final, apresente apenas o nome e a nota do vencedor.
#  
# Fluxo de exceção: 
# 
# O programa deve verificar se a nota da pessoa é maior ou igual a zero e menor ou igual a dez.


def ler_entrada(indice):
    nome = input(f"Informe o nome do {indice+1}º participante: ")
    if nome == '':
        raise ValueError("Nome inválido!")
    
    
    nota = float(input(f"Informe a nota do {indice+1}º participante: "))
    if nota < 0 and nota > 10:
        raise ValueError("Nota inválida!")
    
    return (nome,nota)

def obter_vencedor():
    vencedor = (0,0)

    for participante in participantes:
        if vencedor[1] < participante[1]:
            vencedor = participante

    return vencedor

def impressao():
    vencedor = obter_vencedor()
    print(f"O(a) vencedor(a) foi {vencedor[0]} com nota {vencedor[1]:.1f}")

def obter_participantes():
    for indice in range(10):
        try:
            participante = ler_entrada(indice)
            participantes.append(participante)

        except ValueError as err:
            print(err)
            exit(1)

participantes = []

obter_participantes()
impressao()
