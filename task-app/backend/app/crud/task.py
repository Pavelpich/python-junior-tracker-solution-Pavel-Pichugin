from typing import List, Optional
from sqlalchemy.orm import Session
from app.db.models import Task
from app.schemas.task import TaskCreate


def get_tasks(db: Session) -> List[Task]:
    return db.query(Task).all()


def get_task(db: Session, task_id: int) -> Optional[Task]:
    return db.query(Task).filter(Task.id == task_id).first()


def create_task(db: Session, task_in: TaskCreate) -> Task:
    db_task = Task(**task_in.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def delete_task(db: Session, task_id: int) -> None:
    task = get_task(db, task_id)
    if task:
        db.delete(task)
        db.commit()
