import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

df = pd.read_csv("etxeak.csv")

X = df[["azalera_m2","gela_kopurua","urte_eraikia"]]
y = df["prezioa"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


eredua = LinearRegression().fit(X_train, y_train)
y_iragarpena = eredua.predict(X_test)
mae = mean_absolute_error(y_test, y_iragarpena)
mse = mean_squared_error(y_test, y_iragarpena)
rmse = mse**0.5
r2 = r2_score(y_test, y_iragarpena)
print(f"Mae:{mae}\nRMSE:{rmse}\nr2:{r2}")  
