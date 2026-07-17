import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score

# baca data
df = pd.read_csv(
    "data/CIC_IDS2017/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv"
)

# ubah label
le = LabelEncoder()
df[' Label'] = le.fit_transform(df[' Label'])

# fitur dan target
X = df.drop(' Label', axis=1)
y = df[' Label']

import numpy as np

X = X.replace([np.inf, -np.inf], np.nan)
X = X.fillna(0)

# split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# model
rf = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# training
rf.fit(X_train, y_train)

# prediksi
y_pred = rf.predict(X_test)

# evaluasi
print("Accuracy :", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall   :", recall_score(y_test, y_pred))
print("F1 Score :", f1_score(y_test, y_pred))