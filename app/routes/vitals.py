from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, database
from app.utils.ai import analyze_vitals  # اضافه کردن تابع هوش مصنوعی
from datetime import datetime

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_vital(vital: schemas.VitalCreate, db: Session = Depends(get_db)):
    # بررسی وجود کاربر در دیتابیس
    user = db.query(models.User).filter(models.User.id == vital.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # ذخیره علائم حیاتی در دیتابیس
    db_vital = models.Vital(**vital.dict(), created_at=datetime.utcnow())
    db.add(db_vital)
    db.commit()

    # استفاده از مدل AI برای تحلیل علائم حیاتی
    result = analyze_vitals(vital.heart_rate, vital.blood_pressure, vital.temperature)

    # در صورتی که از حد نرمال خارج باشد، هشدار ایجاد می‌شود
    if result == "danger":
        alert = models.Alert(
            user_id=vital.user_id,
            type="critical",
            message="Critical vital signs detected",
            created_at=datetime.utcnow()
        )
        db.add(alert)
        db.commit()

    # پاسخ به کاربر با پیام تحلیل
    return {"message": f"Vital signs recorded, AI says: {result}"}
