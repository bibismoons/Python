class Calculdora:
    def somar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b
    
    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b != 0:
            return a / b

        else:
            return "Erro: Divisão por zero não permitida."

if __name__ == "__main__":
    calculadora = Calculdora()

    resultado_soma = calculadora.somar(5, 3)
    print(f"Soma: {resultado_soma}")

    resultado_subtracao = calculadora.subtrair(10, 4)
    print(f"Subtracao: {resultado_subtracao}")

    resultado_multiplicacao = calculadora.multiplicar(6, 7)
    print(f"Multiplicação: {resultado_multiplicacao}")

    resultado_divisao = calculadora.dividir(8, 2)
    print(f"Divisão: {resultado_divisao}")
