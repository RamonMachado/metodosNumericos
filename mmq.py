import numpy as np
import string

def somatorio_com_duas_funcoes(pontos, f1, f2):
    resultado = 0
    for ponto in pontos:
        resultado += f1(ponto[0]) * f2(ponto[0])
    return resultado

def somatorio_com_valor_e_funcao(pontos, f1):
    resultado = 0
    for ponto in pontos:
        resultado += ponto[1] * f1(ponto[0])
    return resultado

def criar_matriz_A(pontos, functions):

    n = len(pontos)
    qtdFunctions = len(functions)

    matrixA = [ [] for i in range(qtdFunctions)]
    for index, line in enumerate(matrixA):
        matrixA[index] = [0 for i in range(qtdFunctions)]

    for i, function1 in enumerate(functions):
        for j, function2 in enumerate(functions):
            matrixA[i][j] = somatorio_com_duas_funcoes(pontos, function1, function2)
        
   
    return matrixA

def criar_matriz_B(pontos, functions):

    qtdFunctions = len(functions)
    matrizB = [ 0 for i in range(qtdFunctions)]

    for i, function in enumerate(functions):
        matrizB[i] = somatorio_com_valor_e_funcao(pontos, function)
    return matrizB

def printar_resultado(matriz_resultado):
    letra = 'a'
    for valor in matriz_resultado:
        print(f'{letra} = {valor}')
        letra = chr(ord(letra) + 1)

def resolver_lista():
    pontos = [ [-8, 1.06635918], [-5.71428571, 0.80014487], [-3.42857143, 0.64216079], [-1.14285714, 0.54170856], [1.14285714, 0.44962931], [3.42857143, 0.39317197], [5.71428571, 0.33772819], [8, 0.31377657] ]

    functions = [
                 lambda x: x**3,
                 lambda x: x**2,
                 lambda x: x
                ]

    matrixA = criar_matriz_A(pontos, functions)
    matrixB = criar_matriz_B(pontos, functions)
    resultMatrix = np.linalg.solve(matrixA, matrixB)
    
    print(f'Matriz A: {matrixA}')
    print(f'Matriz B: {matrixB}')
    print(f'Matriz Resultado: {resultMatrix}')
    printar_resultado(resultMatrix)

resolver_lista()