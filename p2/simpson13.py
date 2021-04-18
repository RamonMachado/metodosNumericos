import string
import math

def getC(i, n):
    if (i == 0 or i == n):
        return 1
    elif (i % 2 == 0):
        return 2
    else:
        return 4


def simpson13(qtdIntervalos, a, b, fx):
    h = (b-a) / qtdIntervalos
    xi = a
    resultado = 0
    for i in range(qtdIntervalos+1):
        c = getC(i, qtdIntervalos)
        resultado += (h/3) * (c * fx(xi))
        print(f'i = {i}, h = {h}, c = {c}, xi = {xi}, f(xi) = {fx(xi)}, c*f(xi) = {c * fx(xi)}, integração = {resultado}')
        xi += h
    return  resultado

def aula_11_exemplo1():
    a = 0
    b = 1
    fx = lambda x: x**2
    qtdIntervalos = 5

    resultado = simpson13(qtdIntervalos, a, b, fx)

    print(f'Resultado = {resultado}')

def lista_integracao_questao2():
    a = 1
    b = 4
    fx = lambda x: (1/x)*math.exp(x/2)
    qtdIntervalos = 30

    resultado = simpson13(qtdIntervalos, a, b, fx)

    print(f'Resultado = {resultado}')

def lista_integracao_questao3():
    a = 2
    b = 4
    fx = lambda x: 1/(1+x)
    qtdIntervalos = 300

    resultado = simpson13(qtdIntervalos, a, b, fx)

    print(f'Resultado = {resultado}')


def resolver_lista():
    lista_integracao_questao2()
    #lista_integracao_questao3()
    #aula_11_exemplo1()

resolver_lista()