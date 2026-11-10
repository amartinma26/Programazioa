import numpy as np

"""""
matrizea = np.array(
    [
        [
            1,
            2,
            3,
        ],
        [4, 5, 6],
    ]
)
# 6 elementos
# shape es la azalera que es 3 numeros por cada fila y 2 filas es decir shape= (2,3)
# Dimensiones1, 2 y 3
# 1 dimension->
# 2 dimension->
# 3 dimension->

print(matrizea.shape)  # Para saber las columnas y las filas
print(matrizea.ndim)  # Saber la dimension de la matriz
print(matrizea.size)  # Cuantos elementos contiene en total
print(matrizea.dtype)
print(np.linalg.matrix_rank(matrizea))

# Acceder a los valores dentro de una matrix


m = np.array([
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
    ])

print(m[0, 0])  # 1 (0. fila, 0. columna)
print(m[1, 2])  # 6 (1. fila, 2. columna)
print(m[0])  # [1 2 3] (0. fila osoa)
print(m[:, 1])  # [2 5 8] (1. columnaosoa)
print(m[0:2, 0:2])  # [[1 2] [4 5]] (azpimatrizea)


m = np.array([[2, 4, 6], [8, 10, 12], [14, 16, 18]])

print(m[1])
print(m[:, 2])
print(m[1, 1])
print(m[0:2, 0:2])
"""

# BROADCASTING
"""""
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

print(a + b) # [11 22 33]-> Se suma entre las dos listas
print(a * b) # [10 40 90]-> Se multiplica entre las dos listas
print(a * 2)#-> Se multiplica cada valor uno por uno 
print(b - a) # [9 18 27]->Se resta los valores de entre las listas
print(b / a) # [10. 10. 10.]->Se divide los valores de entre las listas
print(a ** 2) # [1 4 9]-> En potencia de cada valor de las listas

a = np.array([1, 2, 3, 4])

print(a + 10) # [11 12 13 14]
print(a * 2) # [2 4 6 8]
print(a > 2) # [False False True True]


print(np.arange(0, 26, 5))
m = np.random.randint(0, 10, 5)

print(m + 3)

print(m * 2)
print(m > 10)


#ARIKETA 4
notak = np.array([[7, 6, 8], [5, 9, 7], [8, 8, 6]])
media_col = notak.mean(axis=0)
media_fil = notak.mean(axis=1)

print(media_col)
print(media_fil)
print(np.max(notak))
""" ""




