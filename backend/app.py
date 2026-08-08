from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

from predictor import predict_text
from lime_explainer import explain_prediction
from database import init_db, save_prediction, get_history
from suggestion_engine import generate_suggestion   # <-- NEW

app = Flask(__name__)
CORS(app)

# ==========================
# Initialize Database
# ==========================
init_db()


# ==========================
# Home Page
# ==========================
@app.route("/")
def home():
    return render_template("index.html")


# ==========================
# History Page
# ==========================
@app.route("/history-page")
def history_page():
    return render_template("history.html")


# ==========================
# Dashboard Page
# ==========================
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# ==========================
# Predict API
# ==========================
@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({"error": "No text received"}), 400

    text = data["text"]

    # ==========================
    # AI Prediction
    # ==========================
    result = predict_text(text)

    if "error" not in result:

        # --------------------------
        # LIME Explanation
        # --------------------------
        try:
            explanation = explain_prediction(text)
            result["explanation"] = explanation

        except Exception as e:

            print("LIME Error:", e)
            result["explanation"] = []

        # --------------------------
        # Generate Suggestion
        # --------------------------
        try:
            result["suggestion"] = generate_suggestion(text)

        except Exception as e:

            print("Suggestion Error:", e)
            result["suggestion"] = text

        # --------------------------
        # Save Prediction
        # --------------------------
        save_prediction(
            text,
            result["prediction"],
            result["confidence"]
        )

    else:
        result["explanation"] = []
        result["suggestion"] = text

    return jsonify(result)


# ==========================
# History API
# ==========================
@app.route("/history", methods=["GET"])
def history():

    rows = get_history()

    history = []

    for row in rows:
        history.append({
            "id": row[0],
            "comment": row[1],
            "prediction": row[2],
            "confidence": row[3],
            "created_at": row[4]
        })

    return jsonify(history)


# ==========================
# Run Flask
# ==========================
if __name__ == "__main__":
    app.run(debug=True)