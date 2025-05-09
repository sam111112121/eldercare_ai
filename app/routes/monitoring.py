# app/routes/monitoring.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import models, schemas, database

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{user_id}/status")
def get_user_status(user_id: int, db: Session = Depends(get_db)):
    # گرفتن آخرین علائم حیاتی کاربر
    last_vital = db.query(models.Vital).filter(models.Vital.user_id == user_id).order_by(models.Vital.timestamp.desc()).first()
    
    if not last_vital:
        return {"message": "No vitals found for this user"}
    
    # گرفتن آخرین هشدار کاربر
    last_alert = db.query(models.Alert).filter(models.Alert.user_id == user_id).order_by(models.Alert.created_at.desc()).first()
    
    status = {
        "user_id": user_id,
        "name": last_vital.user.name,
        "last_vital": {
            "heart_rate": last_vital.heart_rate,
            "blood_pressure": last_vital.blood_pressure,
            "temperature": last_vital.temperature,
            "timestamp": last_vital.timestamp,
        },
        "last_alert": {
            "type": last_alert.type if last_alert else "No alert",
            "message": last_alert.message if last_alert else "No alert",
            "created_at": last_alert.created_at if last_alert else None,
        }
    }
    
    return status
