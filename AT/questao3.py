PERCENTUAIS_RECOMENDADOS = {
    "moradia": 30, 
    "educacao": 20, 
    "transporte": 15
}


def ler_entrada():
    try:
        renda = float(input("Informe a Renda Mensal: R$ "))
        moradia = float(input("Informe os gastos com moradia: R$ "))
        educacao = float(input("Informe os gastos com educação: R$ "))
        transporte = float(input("Informe os gastos com transporte: R$ "))

        return {
            "renda": renda,
            "gastos": {
                "moradia": moradia,
                "educacao": educacao,
                "transporte": transporte,
            },
        }

    except ValueError as err:
        raise ValueError({"msg": err.args[0],"error": "Valor invalido"})


def calcula_percentual(valor_total, valor_parcial):
    return valor_parcial / valor_total * 100


def calcula_valor_max_por_categoria(renda, categoria):
    return renda * PERCENTUAIS_RECOMENDADOS[categoria] / 100


def criar_mensagem_padrão(categoria, percentual_categoria):
    return (
        f"- Seus gastos totais com {categoria} comprometem "
        f"{percentual_categoria:.2f}% de sua renda total. "
        f"O máximo recomendado é de {PERCENTUAIS_RECOMENDADOS[categoria]:.2f}%. "
    )


def criar_mensagem_condicional(renda, categoria, percentual_categoria):
    if percentual_categoria < PERCENTUAIS_RECOMENDADOS[categoria]:
        return "Seus gastos estão dentro da margem recomendada."
    else:
        valor_max_categoria = calcula_valor_max_por_categoria(renda, categoria)
        return (
            f"Portanto, idealmente, o máximo de sua renda comprometida "
            f"com {categoria} deveria ser de R$ {valor_max_categoria:.2f}"
        )


def gerar_relatorio_saude_financeira(financas):
    relatorio = {}

    for categoria, valor in financas["gastos"].items():
        percentual_categoria = calcula_percentual(financas["renda"], valor)

        relatorio[categoria] = (
            criar_mensagem_padrão(categoria, percentual_categoria)
            + criar_mensagem_condicional(financas["renda"], categoria, percentual_categoria)
        )

    return relatorio


def impressao(resuldado):
    print(f"\nDiagnóstico:\n")
    for item in resuldado.values():
        print(f'{item}\n')


def main():
    try:
        entrada = ler_entrada()
        resultado = gerar_relatorio_saude_financeira(entrada)
        impressao(resultado)

    except Exception as err:
        print(err)


if __name__ == "__main__":
    main()
