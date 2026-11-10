from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import learning_curve

import pandas as pd

df = pd.read_csv("etxeak.csv")

X = df[["azalera_m2"]]
y = df["prezioa"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
"""""
pf = PolynomialFeatures(degree=2, include_bias=False)
X_train_pol = pf.fit_transform(X_train)
X_test_pol = pf.transform(X_test)
print(pf.get_feature_names_out()) # ['azalera_m2' 'azalera_m2^2']
eredua_pol = LinearRegression().fit(X_train_pol, y_train)
print(eredua_pol.score(X_test_pol, y_test)) # 0.988
"""""
tamainak, tr, va = learning_curve(LinearRegression(), X, y,
train_sizes=[0.2, 0.4, 0.6, 0.8, 1.0], cv=5)
print(tamainak) # [ 6 12 19 25 32]
print(tr.mean(axis=1)) # [0.970 0.961 0.955 0.949 0.945]
print(va.mean(axis=1)) # [0.911 0.916 0.923 0.926 0.929]