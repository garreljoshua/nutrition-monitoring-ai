import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Baca dataset
df = pd.read_csv("dataset/nutrition.csv")

# Feature (input)
X = df[['age', 'gender', 'weight', 'height']]

# Target (output)
y = df['status']

# Bagi data train dan test
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Buat model
model = RandomForestClassifier()

# Training
model.fit(X_train, y_train)

# Hitung akurasi
accuracy = model.score(X_test, y_test)

print("Accuracy:", accuracy)

# Simpan model
joblib.dump(model, "nutrition_model.pkl")

print("Model berhasil disimpan!")