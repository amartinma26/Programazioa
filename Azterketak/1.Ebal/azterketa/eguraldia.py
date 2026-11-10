import pandas as pd


df = pd.read_csv("eguraldia.csv")

tenperatura = df["tenperatura"].mean().round()
prezipitazio = df["euria_mm"].mean().round()

print(f"Tenperatura batazbestekoa {tenperatura}C")
print(f"Prezipitazio bataz bestekoa {prezipitazio}mm")

beroa = df["tenperatura"].idxmax()
print(f"Bero gehiago egiten duen eguna {beroa+1} eguna  da")
minimo = df["tenperatura"].idxmin()
print(f"Bero gutxien egiten zuen eguan {minimo +1} eguna  da ")

"""
egunak=[]
ezetasun =[]
kalkulua = lambda x,y : x >20 and y > 10 if egunak.append(x) hezetasun.append(y) else None
kalkuluak.apply("tenpera")
print(egunak)
"""

for i in df["tenperatura"]
    if i > 20:
        