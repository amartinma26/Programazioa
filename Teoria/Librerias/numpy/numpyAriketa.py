import numpy as np

zerrenda_arrunta = [1, 2, 3, 4, 5]
zerrenda_nummpy = np.array(zerrenda_arrunta)
print(zerrenda_nummpy)
print(type(zerrenda_nummpy))

print(np.zeros(7))  # una lista de 7 0
print(np.ones(10))  # una lista de 10 unos
print(np.full(8, 14))  # una lista de 8 14s


print(np.arange(0, 100, 5))  # Creamos una lista desde el 0 al 100 de 5 en 5
print(np.linspace(0, 100, 5))  # Creamos una lista del 0 al 100 con 5 numeros


print(np.arange(0, 225, 25))
# del 0 a 200 pero 200 fuera y que aparezca de 25 en 25 y conseguir el mismo array con linsapce
print(np.linspace(0, 200, 9))
print(np.random.rand(11))#Genera un array de 11 números decimales (floats) aleatorios comprendidos en el rango de 0.0 (incluido) a 1.0 (excluido).
print(np.random.randint(0,11,11))#Genera un array de 11 números enteros aleatorios comprendidos entre 0 (incluido) y 10 (el límite 11 no se incluye).

np.random.seed(50)

print(np.arange(0, 51, 10))
print(np.zeros(6))
print(np.arange(0, 21, 2))
print(np.random.randint(0,100,10))

