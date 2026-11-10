import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer

etxeak = pd.read_csv("etxeak.csv")

X = etxeak[["azalera_m2", "gela_kopurua", "urte_eraikia"]]
y = etxeak["prezioa"]
print(X.shape, y.shape)

Xn = X.astype(float)
r2 = np.random.default_rng(7)
Xn.loc[r2.choice(len(Xn), 8, replace=False), "azalera_m2"] = np.nan
Xn.loc[r2.choice(len(Xn), 6, replace=False), "urte_eraikia"] = np.nan
print(Xn.isna().sum().to_dict()) 
a, b, c, d = train_test_split(Xn, y, test_size=0.2, random_state=42)

try:
    LinearRegression().fit(a, c)
except ValueError as e:
    print(str(e).split(".")[0]) # Input X contains NaN




inputatzailea = SimpleImputer(strategy="median")
a_inp = inputatzailea.fit_transform(a)
b_inp = inputatzailea.transform(b)

print(inputatzailea.statistics_.round(1)) # [ 133.4 3. 1992.9]
print(np.isnan(a_inp).sum()) # 0
print(round(LinearRegression().fit(a_inp, c).score(b_inp, d), 4)) #0.9823
#print(Xn)
#print(etxeak)