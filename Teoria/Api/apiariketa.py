from fastapi import FastAPI,Query,HTTPException
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from zeregina import ZereginBerria,Zeregina


#crear una funcion que si llamamaos a /score nos devuelve el score con numero de vecinos 

app = FastAPI(title="Zereginen APIa")

@app.get("/agurra")
def hasiera():
    return {"mezua": "Kaixo , Asier naiz! Guapo "}

@app.get("/kurtsoa")
def hasiera():
    return {"mezua": "ABuDabi kurstoa egiten ari naiz"}

@app.get("/agurra/{izena}")
def agurra(izena):
    return {"mezua": f"Kaixo {izena}"}


df = load_iris()
print(df)

X = df.data
y = df.target

emaitza = cross_val_score(KNeighborsClassifier(n_neighbors=7), X, y, cv=5,
                            scoring="accuracy")


@app.get("/score")
def scorea():
    return {"score":emaitza.mean()}


#modeloa sortzea
modelo = KNeighborsClassifier(n_neighbors=3)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

modelo.fit(X_train,y_train)

@app.get("/predict")
def predict(largo_sepalo:float,ancho_sepalo:float,largo_petalo:float,ancho_petalo:float):
    predicciones = modelo.predict([[largo_sepalo,ancho_sepalo,largo_petalo,ancho_petalo]])
    return {"erantzuna":f"{df.target_names[predicciones]}"}

zereginak: dict[int, Zeregina] = {} # memorian
hurrengo_id = 1

@app.get("/zereginak", response_model=list[Zeregina])
def zerrenda(egina: bool | None = None,muga: int = Query(10, ge=1, le=100)):
    emaitza = list(zereginak.values())
    if egina is not None:
        emaitza = [z for z in emaitza if z.egina == egina]
    return emaitza[:muga]


@app.get("/zereginak/kopurua")
def kopurua():
    return f"zereginkopurua : {len(zereginak)}"

@app.get("/zereginak/{zeregin_id}", response_model=Zeregina)
def bat_lortu(zeregin_id: int):
    if zeregin_id not in zereginak:
        raise HTTPException(status_code=404,detail="Zeregina ez da aurkitu")
    return zereginak[zeregin_id]


@app.post("/zereginak", response_model=Zeregina , status_code=201)
def sortu(berria: ZereginBerria):
    global hurrengo_id
    zeregina = Zeregina(id=hurrengo_id , izenburua = berria.izenburua,egina=berria.egina)
    zereginak[zeregina.id] = zeregina
    hurrengo_id += 1
    return zeregina

@app.put("/zereginak/{zeregin_id}", response_model=Zeregina)
def ordezkatu(zeregin_id: int, datuak: ZereginBerria):
    if zeregin_id not in zereginak:
        raise HTTPException(status_code=404, detail="Ez da aurkitu")
    zereginak[zeregin_id] = Zeregina(id=hurrengo_id , izenburua = datuak.izenburua,egina=datuak.egina)
    return zereginak[zeregin_id]

@app.delete("/zereginak/{zeregin_id}", status_code=204)
def ezabatu(zeregin_id: int):
    if zeregin_id not in zereginak:
        raise HTTPException(status_code=404, detail="Ez da aurkitu")
    del zereginak[zeregin_id]



