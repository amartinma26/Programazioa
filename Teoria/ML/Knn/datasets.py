from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

df_iris = load_iris(as_frame=True)

X = df_iris.data
y = df_iris.target

print(X.shape)
print(y.shape)

print(list(X.columns))#Columnas de dataset
print(df_iris.target_names)# tipos de flores 

X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size=0.2, random_state=42)# entrenar 80% testo 20% y hacemos que el orden del random sea el mismo 

eredua = KNeighborsClassifier(n_neighbors=3)# explicacion de kNN
eredua.fit(X_train, y_train)
print(eredua.score(X_test, y_test)) # 1.0

berria = X.iloc[[0]]

print(eredua.predict(berria))#tenemos la infromacion de berria que son las caracteristicas de una 
#flor desconocida. La gracia de predict es que sea capaz de predecir de que familia de flor pertenece

print(eredua.score(X_test, y_test))# pasa tener una medida general de que tan bueno es el modelo de prediccion

