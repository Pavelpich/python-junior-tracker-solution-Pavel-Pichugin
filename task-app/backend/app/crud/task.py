from typing import List, Optional

from sqlalchemy.orm import Session

from app.db.models import Task
from app.schemas.task import TaskCreate


def get_tasks(db: Session) -> List[Task]:
    raise NotImplementedError


def get_task(db: Session, task_id: int) -> Optional[Task]:
    raise NotImplementedError


def create_task(db: Session, task_in: TaskCreate) -> Task:
    raise NotImplementedError


def delete_task(db: Session, task_id: int) -> None:
    raise NotImplementedError
