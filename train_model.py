from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
import numpy as np
import os

# داده‌های تمرینی: [ضربان قلب، فشار خون، دمای بدن]
X = np.array([
    [72, 120, 36.5],
    [85, 140, 38.2],
    [60, 110, 35.8],
    [95, 160, 39.0],
    [55, 100, 36.0],
    [100, 170, 39.5],
    [65, 115, 37.0],
])

# برچسب‌ها: 0 = طبیعی، 1 = خطرناک
y = np.array([0, 1, 0, 1, 0, 1, 0])

# آموزش مدل
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = RandomForestClassifier()
model.fit(X_train, y_train)

# ذخیره مدل داخل پوشه app
output_path = os.path.join("app", "ml_model.pkl")
joblib.dump(model, output_path)

print("✅ مدل ذخیره شد در app/ml_model.pkl")
