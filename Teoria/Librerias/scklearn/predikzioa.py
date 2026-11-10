import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("etxeak.csv")

X = df[["azalera_m2", "prezioa", "urte_eraikia"]]
y = df["gela_kopurua"]
print(X.shape, y.shape)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Escalamos los dato StandardScaler
sc = StandardScaler()
A, B = sc.fit_transform(X_train), sc.transform(X_test)

modelo = KNeighborsClassifier(n_neighbors=5)
modelo.fit(A, y_train)

prezioa = input("Dame un precio:")
urtea = input("Dame un año:")
m2 = input("Dame m2:")

X_berria = pd.DataFrame(
    [[m2, prezioa, urtea]], columns=["azalera_m2", "prezioa", "urte_eraikia"]
)
X_berria_sc = sc.transform(X_berria)

print("gela kopurua:", modelo.predict(X_berria_sc)[0])

# con knn  que diga dado un precio ,azalera,año cuantas habitaciones tiene ?
# Una vez echo al usuario le pides los 3 datos y que el programa responda
