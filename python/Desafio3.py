class Desafio3:
    anos = int(input("Informe a quantidade de anos: "))
    meses = int(input("Informe a quantidade de meses: "))
    dias = int(input("Informe a quantidade de dias: "))

    @classmethod
    def calculaQtdDias(cls) -> int:
        return 365 * cls.anos + 30 * cls.meses + cls.dias

    @classmethod
    def impressao(cls):
        idade = cls.calculaQtdDias()
        print(f"A sua idade em dias é {idade}")


Desafio3.impressao()
