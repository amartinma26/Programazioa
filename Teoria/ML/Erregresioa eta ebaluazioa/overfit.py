from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd

df = pd.read_csv("etxeak.csv")

X = df[["azalera_m2"]]
y = df["prezioa"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
for gradua in [1, 2, 3, 5, 8, 12]:
    pf = PolynomialFeatures(degree=gradua, include_bias=False)
    sc = StandardScaler()
    X_tr = sc.fit_transform(pf.fit_transform(X_train))
    X_te = sc.transform(pf.transform(X_test))
    e = LinearRegression().fit(X_tr, y_train)
    print(gradua, round(e.score(X_tr, y_train), 3), # entrenamendua
    round(e.score(X_te, y_test), 3)) 