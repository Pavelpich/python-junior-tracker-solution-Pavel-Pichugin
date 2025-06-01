from sqlalchemy import Column, Integer, String, Boolean
from app.db.database import Base


class Task(Base):
    __tablename__ = "tasks"
    id: int = Column(Integer, primary_key=True, index=True)
    title: str = Column(String, index=True, nullable=False)
    completed: bool = Column(Boolean, default=False)
