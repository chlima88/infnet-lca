import csv
from matplotlib import pyplot as plt

FILENAME = "Assessment_PIBs.csv"


def ler_entrada():
    try:
        pais = input("Informe o nome do país: ")
    
    except ValueError as err:
        raise ValueError({"msg": err.args[0],"error": "Valor invalido"})

    return pais


def ler_arquivo(filename):
    data = []
    try:
        with open(filename, encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for linha in reader:
                data.append(linha)
    
    except FileNotFoundError as err:
        raise FileNotFoundError({"msg": err.args[1], "error": "Arquivo não encontrado"})

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


def obter_dados(entrada):

    filedata = ler_arquivo(FILENAME)
    for item in filedata:
        if item["País"] == entrada:
            int_list = [ float(i) for i in list(item.values())[1:] ]

            return {
                "pais": entrada,
                "eixo_x": list(item.keys())[1:],
                "eixo_y": int_list,
            }


def plotar(resultado):

    plt.plot(resultado["eixo_x"], resultado["eixo_y"], '-o')
    plt.xlabel("Ano")
    plt.ylabel("PIB")
    plt.title(f'Evolução do PIB {resultado["pais"]} (2013-2020)')
    plt.grid(True)
    plt.show()
        

def main():
    try:       
        entrada = ler_entrada() 
        resultado = obter_dados(entrada)
        plotar(resultado)
    
    except Exception as err:
        print(err)


if __name__ == "__main__":
    main()