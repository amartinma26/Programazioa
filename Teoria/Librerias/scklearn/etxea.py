import numpy as np
import pandas as pd
from sklearn.linear_model import Lasso, LinearRegression, Ridge
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler

df = pd.read_csv("etxeak.csv")


X = df[["azalera_m2", "gela_kopurua", "urte_eraikia"]]
y = df["prezioa"]
print(X.shape, y.shape)

modeloa = LinearRegression()

try:
    modeloa.fit(df[["azalera_m2"]], y)
except:
    print("Algo ha ido mal.")


# Aqui podemos pedir o predict o Score
print(modeloa.predict([[90]])[0].round(2))


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)

modeloa2 = LinearRegression()

modeloa2.fit(X_train, y_train)
print(modeloa2.score(X_test, y_test))

print(pd.Series(modeloa2.coef_, index=X.columns).round(1))
print(modeloa2.intercept_.round(2))

w0 = modeloa2.intercept_.round(2)
w1 = modeloa2.coef_[0].round(2)
w2 = modeloa2.coef_[1].round(2)
w3 = modeloa2.coef_[2].round(2)

print(f"prezioa = {w0} + azaleram2 {w1} + gela kop {w2} + urtea {w3}")

print(modeloa2.predict(X_test.iloc[[0]]).round(2))
# azalera_m2 = X_test.iloc[0]["azlaera_m2"]
gela = X_test.iloc[0]["gela_kopurua"]
urtea = X_test.iloc[0]["urte_eraikia"]
# predikzioa = w0 + azalera_m2

# 2.Creando Ruido

rng2 = np.random.default_rng(1)
zarata = pd.DataFrame(
    rng2.normal(size=(len(X), 15)), columns=[f"z{i}" for i in range(15)]
)

X_z = pd.concat([X.reset_index(drop=True), zarata], axis=1)
y_z = df["prezioa"] + rng2.normal(0, 50000, len(df))

Xz_tr, Xz_te, yz_tr, yz_te = train_test_split(X_z, y_z, train_size=0.25, random_state=0)
print(X_z)

# 3 Uso de StandardScaler

sc = StandardScaler()
A, B = sc.fit_transform(Xz_tr), sc.transform(Xz_te)

lin = LinearRegression().fit(A, yz_tr)
print(round(lin.score(A, yz_tr), 3), round(lin.score(B, yz_te), 3))  # 0.941 0.538


# 4 Ridge  Lasso

ridge = Ridge(alpha=3.0)  # modeloa sortu
ridge.fit(A, yz_tr)  # Entrenatu

lasso = Lasso(alpha=3000)  # modeloa sortu
lasso.fit(A, yz_tr)  # modeloa entrenatu

print(f"Ridge: {round(ridge.score(B, yz_te), 3)}")  # 0.694
print(f"Lasso: {round(lasso.score(B, yz_te), 3)}")  # 0.741

# 5. El imacto de Alpha
# Ridge
print("alpha, sc on Train, Sc on test")
for alpha in [0.1, 1, 3, 10, 30, 100]:
    r = Ridge(alpha=alpha).fit(A, yz_tr)
    print(alpha, round(r.score(A, yz_tr), 3), round(r.score(B, yz_te), 3))

# Lasso
print("alpha, sc on Train, Sc on test, W =0")
for alpha in [100, 1000, 3000, 10000, 30000]:
    l = Lasso(alpha=alpha).fit(A, yz_tr)
    print(
        alpha,
        round(l.score(A, yz_tr), 3),
        round(l.score(B, yz_te), 3),
        sum(l.coef_ == 0),
    )


for i in range(5):
    Xz_tr, Xz_te, yz_tr, yz_te = train_test_split(
        X_z, y_z, train_size=0.25, random_state=i
    )
    sc = StandardScaler()
    Xz_tr_sc = sc.fit_transform(Xz_tr)
    Xz_te_sc = sc.transform(Xz_te)
    lasso = lasso(alpha=3000)
    lasso.fit(Xz_tr_sc, yz_tr)
    print(f"{lasso.score(Xz_tr_sc, yz_tr)}       {lasso.score(Xz_te_sc, yz_te)}")


Xz_tr, Xz_te, yz_tr, yz_te = train_test_split(
    X_z, y_z, train_size=0.25, random_state=42
)
print(f"Media: {Xz_tr.mean_(axis=0).round(2)}       debiazioa : {Xz_tr_sc.std(axis=0).round(2)}")

Xz_te_sc=sc.transform(Xz_te)

print(f"Media: {Xz_te.mean_(axis=0).round(2)}       debiazioa : {Xz_te_sc.std(axis=0).round(2)}")

mm= MinMaxScaler()


print(f"Media: {Xz_tr.mean_(axis=0).round(2)}       debiazioa : {Xz_tr_sc.std(axis=0).round(2)}")

Xz_tr_sc= mm.fit_transform(Xz_tr)

print(f"Media: {Xz_tr.mean_(axis=0).round(2)}       debiazioa : {Xz_tr_sc.std(axis=0).round(2)}")
