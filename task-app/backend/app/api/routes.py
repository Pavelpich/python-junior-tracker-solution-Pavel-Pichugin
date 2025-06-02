from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.task import TaskCreate, TaskRead
from app.crud.task import get_tasks, create_task, get_task, delete_task
from app.db.database import get_db

router = APIRouter()


@router.get("/", response_model=List[TaskRead])
def read_tasks(db: Session = Depends(get_db)) -> List[TaskRead]:
    """
    Возвращает список всех задач
    """
    tasks = get_tasks(db)
    return tasks


@router.post("/", response_model=TaskRead, status_code=status.HTTP_201_CREATED)
def add_task(task: TaskCreate, db: Session = Depends(get_db)):
    """
    Принимает json с данными задачи и из них создаёт новую задачу
    """
    new_task = create_task(db, task)
    return new_task


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_task(task_id: int, db: Session = Depends(get_db)) -> None:
    existing = get_task(db, task_id)
    if not existing:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Task not found"
        )
    delete_task(db, task_id)
    return None
