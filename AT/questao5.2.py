import csv

FILENAME = "Assessment_PIBs.csv"


def ler_arquivo(filename):
    data = []
    try:
        with open(filename, encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for linha in reader:
                data.append(linha)
    
    except FileNotFoundError as err:
        raise FileNotFoundError({"msg": err.args[1], "error": "Arquivo não encontrado"})

    return data[:]
            

def calcular_variacao(valor_inicial, valor_final):

    try:
        if valor_inicial > valor_final:
            return (valor_inicial - valor_final) / valor_inicial * (-100)

        else:
            return (valor_final - valor_inicial) / valor_inicial * 100

    except ZeroDivisionError as err:
        raise ZeroDivisionError({"msg": err.args[1], "error": f"Dados invalidos: valor_inicial {valor_inicial}"})


def processar_dados():

    filedata = ler_arquivo(FILENAME)

    lista_estimativas = []

    for item in filedata:

        variacao = calcular_variacao(float(item["2013"]), float(item["2020"]))

        lista_estimativas.append({
            "pais": item["País"],
            "variacao": variacao
            })

    return lista_estimativas


def impressao(resultado):
    for dados in resultado:
        print(f'{dados["pais"]:<15}Variação de {dados["variacao"]:>6.2f} entre 2013 e 2020')
    

def main():
    try:        
        resultado = processar_dados()
        impressao(resultado)
    
    except Exception as err:
        print(err)


if __name__ == "__main__":
    main()