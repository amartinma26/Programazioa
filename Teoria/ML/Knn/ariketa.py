from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

df_wine = load_wine(as_frame=True)

X = df_wine.data
y = df_wine.target

print(X.shape)
print(X.describe())

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

modelo = KNeighborsClassifier(n_neighbors=3)
modelo.fit(X_train, y_train)

print(modelo.score(X_test, y_test))
