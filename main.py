import random
import math

def sigmoid(x):
  return 1 / (1 + math.exp(-x))


def main():
    w = []                                           # Vetor W
    for c in range(4):                               # x0, x1, x2, x3
        aux = round(random.uniform(0, 1), 1)         # Número de 1 casa decimal.
        while aux == 1 or aux == 0:                  # Não pode ser igual a 0 ou 1.
            aux = round(random.uniform(0, 1), 1)
        w.append(aux)

    print(w)
    neuronio1 = (w[0]*0 + w[1]*0) + (w[0]*0 + w[1]*1) + (w[0]*1 + w[1]*0) + (w[0]*1 + w[1]*1)
    neuronio2 = (w[2]*0 + w[3]*0) + (w[2]*0 + w[3]*1) + (w[2]*1 + w[3]*0) + (w[2]*1 + w[3]*1)

    print(f'neuronio1 - {neuronio1}')
    print(f'neuronio2 - {neuronio2}')

    h_neur1 = sigmoid(neuronio1)
    h_neur2 = sigmoid(neuronio2)

    print(f'h_neuronio1 - {h_neur1}')
    print(f'h_neuronio2 - {h_neur2}')


if __name__ == '__main__':
    main()
