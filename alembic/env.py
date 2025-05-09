from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context

# اضافه کردن import مدل‌های خود
from app import models  # مدل‌ها را از app import کنید
from app.database import engine

# این خط از فایل Alembic Config برای دسترسی به تنظیمات استفاده می‌کند.
config = context.config

# تنظیمات مربوط به لاگینگ
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# اضافه کردن مدل‌ها و تنظیم target_metadata
target_metadata = models.Base.metadata  # مدل‌های شما از این طریق در دسترس قرار می‌گیرند

def run_migrations_offline() -> None:
    """اجرای مهاجرت در حالت 'off-line'."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """اجرای مهاجرت در حالت 'online'."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
