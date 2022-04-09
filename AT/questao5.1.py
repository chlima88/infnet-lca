import csv

FILENAME = "Assessment_PIBs.csv"

def ler_entrada():
    try:
        pais = input("Informe o nome do país: ")
        ano = int(input("Informe o ano entre 2013 e 2020: "))
    
    except ValueError as err:
        raise ValueError({"msg": err.args[0],"error": "Valor invalido"})

    return {
        "pais": pais,
        "ano": ano
    }


def ler_arquivo(filename):
    data = []
    with open(filename, encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for linha in reader:
            data.append(linha)

    return data
            

def validar_entrada(entrada):

    filedata = ler_arquivo(FILENAME)

    if entrada["ano"] < 2013 or entrada["ano"] > 2020:
        raise ValueError({"msg": "Ano não disponível. O ano precisa estar entre 2013 e 2020", "error": "Valor invalido"})
    
    paises = []
    for item in filedata:
        paises.append(item["País"])

    if entrada["pais"] not in paises:
        raise ValueError({"msg": "País não disponível", "error": "Valor invalido"})


def encontrar_dados(entrada):

    filedata = ler_arquivo(FILENAME)

    for item in filedata:
        if item["País"] == entrada["pais"]:
            return {
                "pais": entrada["pais"],
                "ano": entrada["ano"],
                "pib": item[str(entrada["ano"])]
                }


def impressao(resultado):
    print(f'PIB {resultado["pais"]} em {resultado["ano"]}: R$ {resultado["pib"]} trilhões')
    

def main():
    try:
        entrada = ler_entrada()
        validar_entrada(entrada)
        resultado = encontrar_dados(entrada)
        impressao(resultado)
    
    except Exception as err:
        print(err)


if __name__ == "__main__":
    main()