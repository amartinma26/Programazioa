import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("switch2_precios.csv")
x = df.iloc[1:, 0]  # Dia
y = df.iloc[1:, 1]  # Precio

# CALCULAR LOS COEFICIENTES
X_media = x.mean()  # Media de X
Y_media = y.mean()  # Media de Y
n_elementos = len(x)  # numero de elementos


# DOS FORMAS DE SACAR LOS NUMERADORES
# 1.

numerador_1 = (x * y).sum()  # Para

# 2.
numerador_1_b = 0
for i in range(n_elementos):
    numerador_1_b += x.iloc[i] * y.iloc[i]


numerador_2 = n_elementos * X_media * Y_media

numerador = numerador_1_b - numerador_2


# DOS FORMAS DE SACAR EL DENOMINADOR
# 1.
denominador_1 = (x**2).sum()
# 2.
denominador_1_b = 0
for i in range(n_elementos):
    denominador_1_b += x.iloc[i] ** 2


denominador_2 = n_elementos * (X_media**2)


denominador = denominador_1_b - denominador_2

A = numerador / denominador

B = Y_media - A * X_media

eguna = int(input("Dame un dia"))
prezio_estimatua = lambda x: B + x * A
print(f"En {eguna} el precio estimado fue de {prezio_estimatua}")


plt.scatter(x, y)
plt.plot(x,prezio_estimatua(x), "r")
plt.show()


# Metricas
y_pred = A * x + B
mse = (( y - y_pred ) ** 2) . mean ()
rmse = np . sqrt ( mse )
mae = ( y - y_pred ) .abs () . mean ()
ss_res = (( y - y_pred ) ** 2) .sum ()
ss_tot = (( y - y . mean () ) ** 2) .sum ()
r2 = 1 - ss_res / ss_tot


#Metricas de error
print ( f"MSE = {mse :.4f}")
print ( f"RMSE = { rmse :.4f}")
print ( f"MAE = {mae :.4f}")
print ( f"R2 = {r2 :.4f}")
