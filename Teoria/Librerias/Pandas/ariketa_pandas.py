import pandas as pd

""""
notak = pd.Series(
    [
        7,
        8,
        5,
        9,
    ],
    index=["Ane", "Jon", "Uxue", "Iker"],
)
print(notak)
"""


datuak = {
    "izena": ["ane", "Jon", "Uxue", "iker"],
    "adina": [6, 17, 16, 18],
    "nota": [7, 2, 5, 9],
}
df = pd.DataFrame(datuak)
# print(df)

"""
print(df.head(2))#imprime los dos primeros resutados de la lista
print(df.tail(2))#imprime los dos ultimos de la lista
print(df.shape)
print(df.columns)
print(df.info)
print(df.describe)
"""
df = pd.read_csv("ikasleak.csv")
# print(df.head)

df.to_csv("emaitzak.csv", index=False)
df.to_csv("emaitzak.xlsx", index=False)
