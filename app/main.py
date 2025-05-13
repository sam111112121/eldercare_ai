from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import users, vitals, alerts, monitoring
from app.database import engine, Base

# ساخت جداول دیتابیس
Base.metadata.create_all(bind=engine)

# ایجاد اپلیکیشن FastAPI
app = FastAPI()

# فعال‌سازی CORS برای ارتباط با کلاینت (مثل Flutter)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # در محصول نهایی بهتر است فقط دامنه‌های مجاز تعریف شوند
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ثبت مسیرها (endpoints)
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(vitals.router, prefix="/vitals", tags=["Vitals"])
app.include_router(alerts.router, prefix="/alerts", tags=["Alerts"])
app.include_router(monitoring.router, prefix="/monitoring", tags=["Monitoring"])

@app.get("/")
def root():
    return {"message": "ElderCare AI is running"}
