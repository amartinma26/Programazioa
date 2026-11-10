import pandas as pd

datuak = {
    "izena": ["Mikel", "Manuel", "Ruben", "Irene", "Xabier"],
    "adina": [16, 7, 34, 37, 12],
    "nota": [8, 4, 9, 10, 5],
}

df = pd.DataFrame(datuak)
# print(df.head)
# print(df.info)
# print(df.describe)

df.to_csv("Ikasleak2.csv", index=False)
# print(df["izena"])
# print(df.adina)
"""
print(df.loc[0])  # ->el indice que tenga 0 (mediante nombre)
print(df.loc[0, "izena"])

print(df.iloc[0])
print(df.iloc[0:2])  # ->Lehen bi lenengoak de 0 a 2
print(df.iloc[0, 1])
print(df.iloc[0::2])  # -> Salen de las posiciones de dos en dos
"""
df = pd.read_csv("ikasleak.csv")
# print(df)
gaindituak = df[
    df["nota"] < 5
]  # ->miramos de la seccion notak quienes tienen mayor que 5
#print(gaindituak)

nagusiak = df[df["adina"] >= 18]
# print(nagusiak)

"""
print(df[df["adina"] >= 17])
print(df[df["nota"] < 5])
print(df[(df["nota"] >= 5) & (df["adina"] == 16)])
biak = df[(df["nota"] >= 5) & (df["adina"] == 16)]
"""
df["gainditua"] = df["nota"] >= 5
df["nota_100"] = df["nota"] * 10

print(df["gainditua"])
print(df["nota_100"])
