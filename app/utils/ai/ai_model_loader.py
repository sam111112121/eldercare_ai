
import joblib
import os
import numpy as np

# مسیر به مدل ذخیره‌شده
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'vital_model.pkl')

# بارگذاری مدل تنها یک بار هنگام ایمپورت
model = joblib.load(MODEL_PATH)

def predict_alert(heart_rate: float, blood_pressure: float, temperature: float) -> str:
    # تبدیل ورودی‌ها به آرایه NumPy
    input_data = np.array([[heart_rate, blood_pressure, temperature]])
    prediction = model.predict(input_data)
    return "danger" if prediction[0] == 1 else "normal"
