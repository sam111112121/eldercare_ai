# app/utils/ai.py
import joblib
import os

# مسیر مدل ذخیره‌شده
model_path = os.path.join(os.path.dirname(__file__), "../ml_model.pkl")
model = joblib.load(model_path)

# تابع تحلیل علائم حیاتی
def analyze_vitals(heart_rate, blood_pressure, temperature):
    prediction = model.predict([[heart_rate, blood_pressure, temperature]])
    return "danger" if prediction[0] == 1 else "normal"
