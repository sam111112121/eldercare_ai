from sqlalchemy.orm import Session
from app import models, schemas

# Create User
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Get Users
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

# Create Vital Signs
def create_vital(db: Session, vital: schemas.VitalCreate):
    db_vital = models.Vital(**vital.dict())
    db.add(db_vital)
    db.commit()
    return db_vital
