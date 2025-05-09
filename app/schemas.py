from pydantic import BaseModel
from datetime import datetime

# ---------------- Users ----------------
class UserCreate(BaseModel):
    name: str
    age: int
    phone: str

class UserOut(UserCreate):
    id: int
    class Config:
        orm_mode = True

# ---------------- Vitals ----------------
class VitalCreate(BaseModel):
    user_id: int
    heart_rate: float
    blood_pressure: float
    temperature: float

class VitalOut(VitalCreate):
    id: int
    created_at: datetime  # در صورتی که در مدل دیتابیس دارید
    class Config:
        orm_mode = True

# ---------------- Alerts ----------------
class AlertOut(BaseModel):
    id: int
    user_id: int
    type: str
    message: str
    created_at: datetime
    class Config:
        orm_mode = True
