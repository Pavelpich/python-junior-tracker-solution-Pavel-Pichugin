from pydantic import BaseModel


class TaskBase(BaseModel):
    """Базовый класс создания задачи"""

    title: str
    completed: bool = False


class TaskCreate(TaskBase):
    """Схема для создания новой задачи."""

    pass


class TaskRead(TaskBase):
    id: int
