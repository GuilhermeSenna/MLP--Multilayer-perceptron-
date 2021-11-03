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

    # Passo 1
    w = GerarPesos(4)
    v = GerarPesos(2)

    # Saída esperada (d) - Porta XOR
    EntradaInicial = [[0, 0], [0, 1], [1, 0], [1, 1]]
    EntradaFinal = []

    ResultNeuronio1 = 0
    ResultNeuronio2 = 0
    ResultNeuronio3 = 0

    while 1:
        for i in range(len(EntradaInicial)):
            vetEntrada = EntradaInicial[i]
            for j in range(len(vetEntrada)):
                # Passo 3 (uj)
                ResultNeuronio1 += (w[j] * vetEntrada[j])
                ResultNeuronio2 += (w[j + 2] * vetEntrada[j])

            # Passo 3 (hj)

            EntradaFinal.append(logistica(ResultNeuronio1))
            EntradaFinal.append(logistica(ResultNeuronio2))
            # print(EntradaFinal)

            # EntradaFinal[0] = logistica(ResultNeuronio1)
            # EntradaFinal[1] = logistica(ResultNeuronio2)

            # Passo 4 (uk)
            ResultNeuronio3 = (EntradaFinal[0] * v[0]) + (EntradaFinal[1] * v[1])

            # Passo 4 (yk)
            ResultObtido = sinal(ResultNeuronio3)

            # XOR
            if vetEntrada[0] == 0 and vetEntrada[1] == 0:
                esperado = -1
            elif vetEntrada[0] == 0 and vetEntrada[1] == 1:
                esperado = 1
            elif vetEntrada[0] == 1 and vetEntrada[1] == 0:
                esperado = 1
            elif vetEntrada[0] == 1 and vetEntrada[1] == 1:
                esperado = -1

            # Passo 5
            erro = esperado - ResultObtido
            print(erroQuadratico)

            # Passo 6
            erroQuadratico = (1/2) * (erro ** 2)

            # Gradiente - camada de saida (Passo 7)
            deltaK = erro * ResultObtido * (1 - ResultObtido)

            # Variacao da correcao dos pesos da camada de saída (Passo 8)
            varicaoK = 0.5 * deltaK * EntradaFinal[0]

            EntradaFinal.clear()


main()
