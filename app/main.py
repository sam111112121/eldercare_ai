from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import users, vitals, alerts, monitoring
from app.database import engine, Base

# اتصال به دیتابیس
Base.metadata.create_all(bind=engine)

# فقط یک بار ایجاد FastAPI
app = FastAPI()

# فعال‌سازی CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # برای تولید بهتر فقط دامین‌های مشخص را مجاز کنید
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ثبت routeها
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(vitals.router, prefix="/vitals", tags=["Vitals"])
app.include_router(alerts.router, prefix="/alerts", tags=["Alerts"])
app.include_router(monitoring.router, prefix="/monitoring", tags=["Monitoring"])

@app.get("/")
def root():
    return {"message": "ElderCare AI is running"}
