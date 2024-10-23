from abc import ABC, abstractmethod

#Definindo uma interface
class Forma_Geometrica (ABC):
    @abstractmethod
    def calcular_area(self):
        pass

#Implementação de uma forma: Círculo
class Circulo (Forma_Geometrica):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return 3.14159 * self.raio ** 2

#Implementação de outra forma: Retângulo
class Retangulo (Forma_Geometrica):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura

#Função genérica para calcular área
def calcular_area_da_forma (forma):
    return forma.calcular_area()

if __name__ == "__main__":
    circulo = Circulo (5)
    retangulo = Retangulo (4, 6)

    print(f"Área do círculo: {calcular_area_da_forma(circulo)}")
    print(f"Área do retângulo: {calcular_area_da_forma(retangulo)}")