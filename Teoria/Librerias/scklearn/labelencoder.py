from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder,OrdinalEncoder
import pandas as pd

ik = pd.read_csv("ikasleak.csv")
#label encoder
le = LabelEncoder()
ik["ikasgela_kod"] = le.fit_transform(ik["ikasgela"])
print(ik) # ['A' 'B' 'C'] (A -> 0, B -> 1, C -> 2)



Xl = ik[["adina", "ikasgela_kod"]]
yl = ik["nota"]

a, b, c, d = train_test_split(Xl, yl, test_size=0.2, random_state=42)
lr = LinearRegression()
lr.fit(a,c)

print(round(lr.score(a, c), 3)) 


#One hot encoder
ohe = OneHotEncoder()
M = ohe.fit_transform(ik[["ikasgela"]]).toarray()
print(ohe.get_feature_names_out()) # ['ikasgela_A' 'ikasgela_B' 'ikasgela_C']
print(M[:3])

Xo = pd.concat([ik[["adina"]], pd.get_dummies(ik["ikasgela"]).astype(int)], axis=1)
a, b, c, d = train_test_split(Xo, ik["nota"], test_size=0.2, random_state=42)

print(Xo)

#Get Dummies
mo = LinearRegression().fit(a, c)
print(round(mo.score(b, d), 3)) # 0.787
print(pd.Series(mo.coef_, index=Xo.columns).round(2).to_dict())
print(mo.intercept_)
# {'adina': 0.16, 'A': -0.26, 'B': 1.79, 'C': -1.53}


#Ordinal encoder

tam = pd.DataFrame({"tamaina": ["handia", "txikia", "ertaina", "txikia"
]})
oe = OrdinalEncoder(categories=[["txikia", "ertaina", "handia"]])
print(oe.fit_transform(tam).ravel()) # [2. 0. 1. 0.]
ohe = OneHotEncoder(handle_unknown="ignore").fit(ik[["ikasgela"]])
print(ohe.transform(pd.DataFrame({"ikasgela": ["D"]})).toarray()) #[[0. 0. 0.]]