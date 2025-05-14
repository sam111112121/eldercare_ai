# app/utils/ai_model.py
import pickle
import os
import numpy as np

# مسیر مدل ذخیره‌شده
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'vital_model.pkl')

# بارگذاری مدل
with open(MODEL_PATH, 'rb') as f:
    model = pickle.load(f)

def predict_vital_status(heart_rate: float, blood_pressure: float, temperature: float) -> str:
    X = np.array([[heart_rate, blood_pressure, temperature]])
    prediction = model.predict(X)
    return 'danger' if prediction[0] == 1 else 'normal'
