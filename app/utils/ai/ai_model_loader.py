
import joblib
import os
import numpy as np

# بارگذاری مدل آموزش‌دیده
model_path = os.path.join(os.path.dirname(__file__), "vital_model.pkl")
model = joblib.load(model_path)

# تابع تحلیل وضعیت حیاتی
def predict_alert(heart_rate: float, blood_pressure: float, temperature: float, age: float = 65, cholesterol: float = 200) -> str:
    features = np.array([[heart_rate, blood_pressure, temperature, age, cholesterol]])
    prediction = model.predict(features)
    return "danger" if prediction[0] == 1 else "normal"
