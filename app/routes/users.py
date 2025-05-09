from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, database

router = APIRouter()

# تابع اتصال به دیتابیس
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# دریافت لیست کاربران
@router.get("/", response_model=list[schemas.UserOut])
def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

# ایجاد کاربر جدید
@router.post("/", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# دریافت علائم حیاتی یک کاربر
@router.get("/{user_id}/vitals")
def get_user_vitals(user_id: int, db: Session = Depends(get_db)):
    vitals = db.query(models.Vital).filter(models.Vital.user_id == user_id).all()
    if not vitals:
        raise HTTPException(status_code=404, detail=f"No vitals found for user with ID {user_id}")
    return vitals
