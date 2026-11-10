#con el modelo de KNN de las habitaciones en vez de usar Score usar lo de hoy
#de 1 a 6 vecinos y miraar donde hay underfit donde equilibrado y donde overfitt
from sklearn.preprocessing import StandardScaler

from sklearn.datasets import load_wine
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
df = pd.read_csv("etxeak.csv")

X = df[["azalera_m2", "prezioa", "urte_eraikia"]]
y = df["gela_kopurua"]

print(X.shape, y.shape)


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

sc = StandardScaler()
A, B = sc.fit_transform(X_train), sc.transform(X_test)


for i in range(1,7):
    modelo = KNeighborsClassifier(n_neighbors=i)
    modelo.fit(A, y_train)

    y_iragarpena = modelo.predict(B)
    mae = mean_absolute_error(y_test, y_iragarpena)
    mse = mean_squared_error(y_test, y_iragarpena)
    rmse = mse**0.5
    r2 = r2_score(y_test, y_iragarpena)
    print(f"{i}-Mae:{mae:.2f}, {i}-RMSE:{rmse:.4f}, {i}-r2:{r2:.4f}") 


#Modelo 2 da underfitt zergatik balioak  oso urrun daude 0 MAE eta RMSE eta R2 oso urriti 1
#Modelo optimoa 3 garrena da zegatik MAE balia da 0 bain gertuena dagoena RMSE ere eta R2 1 era gertuena dagoena .
#modelo 





