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

    # Saída esperada (d) - Porta XOR
    EntradaInicial = [[0, 0], [0, 1], [1, 0], [1, 1]]
    EntradaFinal = []
    variacaoK = []
    deltaJ = []

    ResultNeuronio1 = 0
    ResultNeuronio2 = 0
    ResultNeuronio3 = 0

    cont = 0
    for c in range(10):
        print(f"\n>> {c+1}ª passada:")
        if c == 0:
            for i in range(len(EntradaInicial)):
                vetEntrada = EntradaInicial[i]      # Percorre os possíveis valores [0, 0], [0, 1], [1, 0], [1, 1]
                for j in range(len(vetEntrada)):
                    # Passo 3 (uj)

                    ResultNeuronio1 += (w[j] * vetEntrada[j])
                    ResultNeuronio2 += (w[j + 2] * vetEntrada[j])
        else:
            # for k, k_ in enumerate(variacaoK):
            #     print(f'varicaok {k} - {k_}')

            variacaoK.clear()

            # for var, var_ in enumerate(deltaJ):
            #     print(f'DeltaJ {var} - {var_}')

            deltaJ.clear()
        print(v)

        # Passo 3 (hj)
        EntradaFinal.append(logistica(ResultNeuronio1))
        EntradaFinal.append(logistica(ResultNeuronio2))

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

        # Passo 5 (ek)
        erro = esperado - ResultObtido

        print(f'-> {erro}')

        # Passo 6 (en)
        erroQuadratico = (1/2) * (erro ** 2)

        # Passo 7
        # Gradiente - camada de saida
        deltaK = erro * ResultObtido * (1 - ResultObtido)

        # Passo 8
        # Variacao da correcao dos pesos da camada de saída
        variacaoK.append(casasDecimais(0.5 * deltaK * EntradaFinal[0]))
        variacaoK.append(casasDecimais(0.5 * deltaK * EntradaFinal[1]))

        # Passo 9
        deltaJ.append(casasDecimais(deltaK * variacaoK[0] * EntradaFinal[0] * (1 - EntradaFinal[0])))
        deltaJ.append(casasDecimais(deltaK * variacaoK[0] * EntradaFinal[1] * (1 - EntradaFinal[1])))
        deltaJ.append(casasDecimais(deltaK * variacaoK[1] * EntradaFinal[0] * (1 - EntradaFinal[0])))
        deltaJ.append(casasDecimais(deltaK * variacaoK[1] * EntradaFinal[1] * (1 - EntradaFinal[1])))

        # Passo 10
        # variacaoJ = 0.5 * deltaJ *

        # Passo 11
        v[0] = v[0] * variacaoK[0]
        v[1] = v[1] * variacaoK[1]


        EntradaFinal.clear()


main()
