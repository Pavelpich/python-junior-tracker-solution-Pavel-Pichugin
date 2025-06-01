# backend/app/main.py
from fastapi import FastAPI
from app.api.routes import router as tasks_router
from app.db.database import engine, Base

app = FastAPI(title="Task API")


# автоматическое создание таблиц при запуске
@app.on_event("startup")
def create_tables() -> None:
    Base.metadata.create_all(bind=engine)


app.include_router(
    tasks_router,
    prefix="/api/tasks",
    tags=["tasks"],
)
