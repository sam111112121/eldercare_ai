# app/routes/alerts.py
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

@router.get("/{user_id}")
def get_alerts(user_id: int, db: Session = Depends(get_db)):
    alerts = db.query(models.Alert).filter(models.Alert.user_id == user_id).all()
    if not alerts:
        return {"message": "No alerts found for this user"}
    return alerts
