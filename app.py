from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load("nutrition_model.pkl")

@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None
    confidence = None
    recommendation = None

    if request.method == "POST":

        age_year = float(request.form["age"])
        age = age_year * 12
        gender = int(request.form["gender"])
        weight = float(request.form["weight"])
        height = float(request.form["height"])

        data = [[age, gender, weight, height]]

        prediction = model.predict(data)[0]

        probabilities = model.predict_proba(data)[0]
        confidence = round(max(probabilities) * 100, 2)

        if prediction == "Gizi Baik":
            recommendation = "Pertahankan pola makan sehat dan rutin memantau pertumbuhan anak."

        elif prediction == "Risiko Gizi Kurang":
            recommendation = "Tingkatkan asupan nutrisi dan konsultasikan dengan tenaga kesehatan."

        else:
            recommendation = "Segera lakukan pemeriksaan ke fasilitas kesehatan untuk penanganan lebih lanjut."

    return render_template(
        "index.html",
        prediction=prediction,
        confidence=confidence,
        recommendation=recommendation
    )

if __name__ == "__main__":
    app.run(debug=True)