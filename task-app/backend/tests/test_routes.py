from fastapi import APIRouter

router = APIRouter()


@router.get("/tasks")
def read_tasks():
    pass


@router.post("/tasks")
def add_task():
    pass
