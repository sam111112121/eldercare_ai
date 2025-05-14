# فاز ۱: ساخت مدل یادگیری ماشین برای تحلیل علائم حیاتی
# مسیر ذخیره: eldercare_ai/app/utils/ai/vital_predictor.py

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
import os

# داده‌های نمونه‌سازی شده
data = pd.DataFrame({
    'heart_rate': [72, 95, 110, 60, 45, 130, 82],
    'blood_pressure': [120, 145, 160, 110, 90, 170, 125],
    'temperature': [36.8, 37.5, 38.2, 36.5, 35.8, 39.0, 36.9],
    'alert': [0, 1, 1, 0, 1, 1, 0]  # 1: خطر، 0: عادی
})

X = data[['heart_rate', 'blood_pressure', 'temperature']]
y = data['alert']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# ارزیابی مدل
print(classification_report(y_test, model.predict(X_test)))

# مسیر ذخیره فایل مدل
model_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../ai'))
os.makedirs(model_dir, exist_ok=True)
model_path = os.path.join(model_dir, 'vital_model.pkl')

# ذخیره مدل
joblib.dump(model, model_path)
print(f"✅ مدل در مسیر ذخیره شد: {model_path}")
