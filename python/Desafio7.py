def main():

    nome = str(input("Informe o nome do funcionario: "))
    empresa = str(input("Informe o nome da empresa: "))
    salario = float(input("Informe o salario: "))

    aliquota = calcula_aliquota(salario)
    parcela = calcula_parcela(salario)

    imprime(nome, empresa, parcela, aliquota)


def calcula_aliquota(salario: float) -> float:
    if salario <= 1903.98:
        aliquota = 0
    elif salario <= 2826.65:
        aliquota = 0.75
    elif salario <= 3751.05:
        aliquota = 0.15
    elif salario <= 4664.68:
        aliquota = 0.225
    else:
        aliquota = 0.275

    return float(aliquota)


def calcula_parcela(salario: float, aliquota: float) -> float:
    parcela = salario * aliquota
    return parcela


def imprime(nome: str, empresa: str, parcela: float, aliquota: float) -> None:

    if aliquota == 0:
        print(f"O funcionario {nome} da empresa {empresa} está isento")
    else:
        print(
            f"O funcionario {nome} da empresa {empresa} "
            f"deve deduzir o valor de R${parcela} "
        )


main()
