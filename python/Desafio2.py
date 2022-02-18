class Desafio2:
    altura = float(input("Informe a altura do triangulo: "))
    base = float(input("Informe a base do triangulo: "))

    @classmethod
    def calculaArea(cls):
        return cls.base * cls.altura / 2

    @classmethod
    def imprime(cls):
        area = cls.calculaArea()
        print(f"A área do triangulo é de {area} centimetros")


Desafio2.imprime()
