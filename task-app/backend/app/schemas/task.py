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

    class Config:
        orm_mode = True
        allow_population_by_field_name = True

        def alias_generator(s):
            return "".join(
                [s[0].lower()] + [c if c.islower() else "_" + c.lower() for c in s[1:]]
            )
