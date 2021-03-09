import numpy as np
from sympy import symbols
from sympy import lambdify
import matplotlib.pyplot as plt

def produtorio(pontos, i, x=None):
    if x == None:
        x = symbols('x')
    resultado = 0
    for j, ponto in enumerate(pontos):
        if j != i:
            if resultado == 0:
                resultado = (x-ponto[0])/(pontos[i][0] - ponto[0])
            else:
                resultado *= (x-ponto[0])/(pontos[i][0] - ponto[0])

    return resultado

def calculate(pontos, x=None):
    n = len(pontos)

    sum = 0
    for i, ponto in enumerate(pontos):
        sum += ponto[1] * produtorio(pontos, i, x)
    return sum


pontos = [ [2, 0.3010299957], [3, 0.4771212547] ]
x = 2.4

polinomio = calculate(pontos)
resultado = calculate(pontos, 2.4)

print(f'p(x) = {polinomio}')
print(f'p({x}) = {resultado}')

x = np.linspace(-2.5, 4, 1000)
y = polinomio
z = 0.1 - 0.31666667*x + 0.35 * x**2  - 0.23333333 * x**3

lam_x = lambdify(symbols('x'), y, modules=['numpy'])
y_vals = lam_x(x)

plt.plot([ponto[0] for ponto in pontos], [ponto[1] for ponto in pontos], 'o', color='black')
plt.plot(x, y_vals, color='blue')
#plt.plot(x, z, color='red')
plt.legend(['dados', f'p(x) = {polinomio}']) 
plt.grid()
plt.show()
