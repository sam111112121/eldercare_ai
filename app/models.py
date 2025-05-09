from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    phone = Column(String)

    # روابط
    vitals = relationship("Vital", back_populates="user")
    alerts = relationship("Alert", back_populates="user")

class Vital(Base):
    __tablename__ = "vitals"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    heart_rate = Column(Float)
    blood_pressure = Column(Float)
    temperature = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)  # فقط ستون created_at باقی می‌ماند

    # رابطه برگشتی
    user = relationship("User", back_populates="vitals")

class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    type = Column(String)
    message = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    # رابطه برگشتی
    user = relationship("User", back_populates="alerts")
