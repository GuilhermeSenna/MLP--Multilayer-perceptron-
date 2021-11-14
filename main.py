import numpy
import math


def logistica(x):
    return 1 / (1 + math.exp(-x))


def sinal(x):
    if x > 0:
        return 1.5
    else:
        return -1.5


def GerarPesos(TAM):
    vetor = numpy.random.uniform(0.1, 1.0, TAM)
    return vetor


def casasDecimais(valor):
    return float(format(valor, ".2f"))


def main():
    # Passo 1
    w = GerarPesos(4)
    v = GerarPesos(2)
    deltaJ = []

    # Saída esperada (d) - Porta XOR
    EntradaInicial = [[0, 0], [0, 1], [1, 0], [1, 1]]
    EntradaFinal = []
    variacaoK = []
    deltaJ = []
    variacaoJ = []

    ResultNeuronio1 = 0
    ResultNeuronio2 = 0
    ResultNeuronio3 = 0

    cont = 0
    while 1:
        marcador = 0
        for i in range(len(EntradaInicial)):
            vetEntrada = EntradaInicial[i]
            for j in range(len(vetEntrada)):
                # Passo 3 (uj)
                ResultNeuronio1 += (w[j] * vetEntrada[j])
                ResultNeuronio2 += (w[j + 2] * vetEntrada[j])

            print(v[0])

            # Passo 3 (hj)
            EntradaFinal.append(logistica(ResultNeuronio1))
            EntradaFinal.append(logistica(ResultNeuronio2))

            # Passo 4 (uk)
            ResultNeuronio3 = (EntradaFinal[0] * v[0]) + (EntradaFinal[1] * v[1])

            # Passo 4 (yk)
            ResultObtido = sinal(ResultNeuronio3)

            # XOR
            if vetEntrada[0] == 0 and vetEntrada[1] == 0:
                esperado = -1.5
            elif vetEntrada[0] == 0 and vetEntrada[1] == 1:
                esperado = 1.5
            elif vetEntrada[0] == 1 and vetEntrada[1] == 0:
                esperado = 1.5
            elif vetEntrada[0] == 1 and vetEntrada[1] == 1:
                esperado = -1.5

            # Passo 5 (ek)
            erro = esperado - ResultObtido

            # Passo 6 (en)
            erroQuadratico = (1 / 2) * (erro ** 2)

            # Passo 7
            # Gradiente - camada de saida
            deltaK = erro * ResultObtido * (1 - ResultObtido)

            # Passo 8
            # Variacao da correcao dos pesos da camada de saída
            variacaoK.append(casasDecimais(0.5 * deltaK * EntradaFinal[0]))
            variacaoK.append(casasDecimais(0.5 * deltaK * EntradaFinal[1]))

            # Passo 9
            for j in range(len(v)):
                aux = 0
                for cont in range(len(v)):
                    aux += (deltaK * v[cont])
                aux = aux * EntradaFinal[j] * (1 - EntradaFinal[j])
                deltaJ.append(casasDecimais(aux))

            # Passo 10

            for z in range(len(deltaJ)):
                for j in range(len(vetEntrada)):
                    variacaoJ.append(0.5 * deltaJ[z] * vetEntrada[j])

            # Passo 11
            for z in range(len(v)):
                v[z] += variacaoK[z]
            for z in range(len(w)):
                w[z] += variacaoJ[z]

            if erro != 0:
                marcador = 1

            ResultNeuronio1 = 0
            ResultNeuronio2 = 0
            EntradaFinal.clear()
            variacaoK.clear()
            deltaJ.clear()
        if marcador == 0:
            break


main()
