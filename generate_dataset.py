import pandas as pd
import random

data = []

for i in range(500):

    age = random.randint(12, 60)
    gender = random.randint(0, 1)

    status = random.choice([
        "Gizi Baik",
        "Risiko Gizi Kurang",
        "Risiko Gizi Buruk"
    ])

    if status == "Gizi Baik":
        weight = round(random.uniform(10, 20), 1)
        height = round(random.uniform(80, 120), 1)

    elif status == "Risiko Gizi Kurang":
        weight = round(random.uniform(7, 12), 1)
        height = round(random.uniform(70, 100), 1)

    else:
        weight = round(random.uniform(5, 8), 1)
        height = round(random.uniform(60, 90), 1)

    data.append([
        age,
        gender,
        weight,
        height,
        status
    ])

df = pd.DataFrame(
    data,
    columns=[
        "age",
        "gender",
        "weight",
        "height",
        "status"
    ]
)

df.to_csv(
    "dataset/nutrition.csv",
    index=False
)

print("Dataset berhasil dibuat!")