import numpy
import math


def logistica(x):
    return 1 / (1 + math.exp(-x))


def sinal(x):
    if x > 0:
        return 1
    else:
        return -1


def GerarPesos(TAM):
    vetor = numpy.random.uniform(0.1, 1.0, TAM)
    return vetor


def main():
    w = GerarPesos(4)
    v = GerarPesos(2)

    EntradaInicial = [[0, 0], [0, 1], [1, 0], [1, 1]]
    EntradaFinal = []

    ResultNeuronio1 = 0
    ResultNeuronio2 = 0
    ResultNeuronio3 = 0

    while 1:
        for i in range(len(EntradaInicial)):
            vetEntrada = EntradaInicial[i]
            for j in range(len(vetEntrada)):
                ResultNeuronio1 += (w[j] * vetEntrada[j])
                ResultNeuronio2 += (w[j + 2] * vetEntrada[j])

            EntradaFinal[0] = logistica(ResultNeuronio1)
            EntradaFinal[1] = logistica(ResultNeuronio2)

            ResultNeuronio3 = (EntradaFinal[0] * v[0]) + (EntradaFinal[1] * v[1])
            ResultObtido = sinal(ResultNeuronio3)

            if vetEntrada[0] == 0 and vetEntrada[1] == 0:
                esperado = -1
            elif vetEntrada[0] == 0 and vetEntrada[1] == 1:
                esperado = 1
            elif vetEntrada[0] == 1 and vetEntrada[1] == 0:
                esperado = 1
            elif vetEntrada[0] == 1 and vetEntrada[1] == 1:
                esperado = -1

            erro = esperado - ResultObtido

            erroQuadratico = (1/2) * (erro ** 2)

            # Gradiente - camada de saida
            deltaK = erro * ResultObtido * (1 - ResultObtido)

            # Variacao da correcao dos pesos da camada de saída
            varicaoK = 0.5 * deltaK * EntradaFinal[0]


main()
