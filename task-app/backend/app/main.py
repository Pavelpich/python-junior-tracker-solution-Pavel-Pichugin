from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.database import engine, Base

app = FastAPI(title="Task API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# автоматическое создание таблиц при запуске
@app.on_event("startup")
def create_tables() -> None:
    Base.metadata.create_all(bind=engine)


from app.api.routes import router as tasks_router

app.include_router(
    tasks_router,
    prefix="/api/tasks",
    tags=["tasks"],
)
