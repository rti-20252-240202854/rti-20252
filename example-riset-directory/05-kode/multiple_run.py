import pandas as pd
import numpy as np

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

from imblearn.over_sampling import SMOTE

# ======================
# Load Dataset
# ======================

df = pd.read_csv(
    "data/CIC_IDS2017/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv"
)

# Label Encoding
le = LabelEncoder()
df[' Label'] = le.fit_transform(df[' Label'])

# Pisahkan fitur dan label
X = df.drop(' Label', axis=1)
y = df[' Label']

# Bersihkan data
X = X.replace([np.inf, -np.inf], np.nan)
X = X.fillna(0)

# ======================
# Multiple Run
# ======================

seeds = [42, 123, 999, 2025, 777]

hasil = []

for seed in seeds:

    # Train Test Split
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=seed,
        stratify=y
    )

    # SMOTE hanya pada data training
    smote = SMOTE(random_state=seed)

    X_train_smote, y_train_smote = smote.fit_resample(
        X_train,
        y_train
    )

    # Random Forest
    rf = RandomForestClassifier(
        n_estimators=100,
        random_state=seed
    )

    rf.fit(X_train_smote, y_train_smote)

    # Prediksi
    y_pred = rf.predict(X_test)

    # Evaluasi
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred)
    rec = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    hasil.append([
        seed,
        acc,
        prec,
        rec,
        f1
    ])

# ======================
# DataFrame Hasil
# ======================

hasil_df = pd.DataFrame(
    hasil,
    columns=[
        'Seed',
        'Accuracy',
        'Precision',
        'Recall',
        'F1'
    ]
)

# ======================
# Tampilkan Hasil
# ======================

print("=" * 60)
print("HASIL MULTIPLE RUN RANDOM FOREST + SMOTE")
print("=" * 60)

print("\nHasil Setiap Run:")
print(hasil_df)

print("\n" + "=" * 60)
print("RATA-RATA")
print("=" * 60)
print(hasil_df.mean(numeric_only=True))

print("\n" + "=" * 60)
print("MEDIAN")
print("=" * 60)
print(hasil_df.median(numeric_only=True))

print("\n" + "=" * 60)
print("STATISTIK DESKRIPTIF")
print("=" * 60)
print(hasil_df.describe())

# ======================
# Simpan ke CSV
# ======================

hasil_df.to_csv(
    "hasil_smote.csv",
    index=False
)

print("\nHasil berhasil disimpan ke file:")
print("hasil_smote.csv")