import pandas as pd

df = pd.read_csv("emaitzak.csv")

print(df.isna())  # ->Comprueba cada celda y comprueba que este vacia o no
print(df.isna().sum)  # ->Cuenta los valores de cada colubna
print(df.dropna)  # ->Elimina las fila que tengan algun dato vacio
print(df.fillna(0))  # ->rellena los valores que faltan con 0


df["gaindituak"] = df["ikasgela"].fillna(False)

df["gaindituak"] = df["ikasgela"].fillna(df["nota"] >= 7)
print(df)
