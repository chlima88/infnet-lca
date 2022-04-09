
def ler_entrada():
    try:
        capital = float(input("Informe o capital inicial: R$ "))
        rendimento = float(input("Informe o rendimento do período (%): "))
        aporte = float(input("Informe o valor do aporte: R$ "))
        periodos = int(input("Informe o total de perídos: "))

        return {
            "capital": capital,
            "rendimento": rendimento,
            "aporte": aporte,
            "periodos": periodos
        }

    except ValueError as err:
        raise ValueError({"msg": err.args[0],"error": "Valor invalido"})


def atualizar_valor_com_juros(montante, juros, aporte):
    return montante * (1 + juros / 100) + aporte


def gerar_evolucao_montante(entrada):
    evolucao = [entrada["capital"]] 
    for index in range(entrada["periodos"]):
        valor_atualizado = atualizar_valor_com_juros(evolucao[index], entrada["rendimento"], entrada["aporte"])
        evolucao.append(valor_atualizado)

    return evolucao


def impressao(resultado):
    for index, valor in enumerate(resultado):
        if index:
            print(f"Após {index} período(s), o montante será de R$ {valor:.2f}")


def main():
    try:
        entrada = ler_entrada()
        resultado = gerar_evolucao_montante(entrada)
        impressao(resultado)

    except Exception as err:
        print(err)


if __name__ == "__main__":
    main()

