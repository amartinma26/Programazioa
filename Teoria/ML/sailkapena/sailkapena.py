from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("ikasleak_sailkapena.csv")

X = df[["ordu_ikasketa", "asistentzia", "aurreko_nota"]]
y = df["arriskuan"]

X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size=0.25, random_state=42, stratify=y
)

#print(y.value_counts().to_dict()) # {0: 239, 1: 161}
#print(y_test.value_counts().to_dict()) # {0: 60, 1: 40}

scaler = StandardScaler()
X_train_esk = scaler.fit_transform(X_train)
X_test_esk = scaler.transform(X_test)
log = LogisticRegression()
log.fit(X_train_esk, y_train)
print(log.score(X_test_esk, y_test)) # 0.85