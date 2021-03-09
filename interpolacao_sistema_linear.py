#Created by Ramon Machado de Almeida in 07/03/2021
import numpy as np

pontos = [ [0.50, -2.80], [0.75, -0.60], [1, 1], [1.5, 3.2], [2, 4.8] ]
pontos2 = [ [-2, 4], [-1, 1], [2, -1], [0.5, 0] ]

def criar_matriz_A(pontos):
    n = len(pontos)
    matrixA = [ [] for y in range(n)] #initialize an empty A matrix
    for index, ponto in enumerate(pontos):
        for i in range(n):
            pushValue = 0
            if i == 0:
                pushValue = 1
            else:
                pushValue = np.power(ponto[0], i)
            matrixA[index].append(pushValue)

    return matrixA

def criar_matriz_B(pontos):
    matrixB = [] #initialize an empty B matrix
    for index, ponto in enumerate(pontos):
        matrixB.append(ponto[1])
    return matrixB

def polinomio_interpolador_por_sistema_linear(pontos):

    n = len(pontos)
    matrixA = criar_matriz_A(pontos)
    matrixB = criar_matriz_B(pontos)

    print(f'Matrix A: {matrixA}')
    print(f'Matrix B: {matrixB}')

    resultMatrix = np.linalg.solve(matrixA, matrixB)
    print(f'Result: {resultMatrix}')

    #daqui pra baixo é só pra printar direitinho, mas o calculo principal já foi feito

    arrayOfKeys = []
    for index, result in enumerate(resultMatrix):
        arrayOfKeys.append(f'a{index}')
        print(f'a{index} = {result}')

    variablesDict = dict(zip(arrayOfKeys, resultMatrix))

    print(variablesDict)

    valor = -0.5
    resultado = 0
    for index in range(len(resultMatrix)):
        resultado += variablesDict[f'a{index}'] * np.power(valor, index)
    
    print(f'Resultado de f({valor}) = {resultado}')


polinomio_interpolador_por_sistema_linear(pontos)