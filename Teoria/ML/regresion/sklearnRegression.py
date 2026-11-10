import pandas as pd
from sklearn.linear_model import LinearRegression


df = pd.read_csv("switch2_precios.csv")
x_train = df.iloc[1:, 0]  # Dia
y_train = df.iloc[1:, 1]  # Precio

x_train_sk = x_train.values.reshape(-1,1)


modelo_regresion=LinearRegression()
modelo_regresion.fit(x_train_sk,y_train)


print ( f"Pendiente A = { modelo_regresion.coef_ [0]}")# El valor que va ha tener de diferencia cada dia 0,15€
print ( f"Intercepto B = { modelo_regresion.intercept_ }")#Sube o baja la grafia para equilibrar los pesos por que el dia 1 
#la switch no valia 0,15 sino que 449€


