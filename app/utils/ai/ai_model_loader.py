import joblib
import os

model_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../ai/vital_model.pkl'))
model = joblib.load(model_path)

def predict_alert(heart_rate: float, blood_pressure: float, temperature: float) -> str:
    prediction = model.predict([[heart_rate, blood_pressure, temperature]])[0]
    return "danger" if prediction == 1 else "normal"
