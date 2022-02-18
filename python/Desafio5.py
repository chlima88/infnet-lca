#  Receba o nome do time, a quantidade de vit�rias, a quantidade de empates.
#  Exiba o seguinte relat�rio:
#  "O time xxx est� com yyy pontos".


class Desafio5:

    time = str(input("Informe o nome do time: "))
    vitorias = int(input("Informe a quantidade de vitorias: "))
    empates = int(input("Informe a quantidade de empates: "))

    @classmethod
    def calculaPontos(cls):
        return cls.vitorias * 3 + cls.empates

    @classmethod
    def imprime(cls):
        print(f"O time {cls.time} esta com {cls.calculaPontos()} pontos")


Desafio5.imprime()
