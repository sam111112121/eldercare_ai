from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, database

router = APIRouter()

# تابع دریافت اتصال به دیتابیس
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# دریافت هشدارها بر اساس شناسه کاربر
@router.get("/")
def get_alerts(user_id: int, db: Session = Depends(get_db)):
    alerts = db.query(models.Alert).filter(models.Alert.user_id == user_id).order_by(models.Alert.created_at.desc()).all()
    
    if not alerts:
        raise HTTPException(status_code=404, detail="No alerts found for this user")
    
    return alerts
