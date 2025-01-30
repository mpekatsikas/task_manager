from fastapi import APIRouter, Depends, HTTPException
from backend.app.db.schemas import TaskCreate, TaskUpdate
from backend.app.db.crud import get_tasks, get_task, create_new_task, update_specific_task, \
    delete_specific_task
from backend.app.db.database import get_db
from sqlalchemy.orm import Session

router = APIRouter()


# ✅ Get all tasks
@router.get("/")
def read_tasks(db: Session = Depends(get_db)):
    return get_tasks(db)


# ✅ Get a single task
@router.get("/{task_id}")
def read_task(task_id: int, db: Session = Depends(get_db)):
    task = get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


# ✅ Create a task
@router.post("/")
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    return create_new_task(db, task)


# ✅ Update a task
@router.put("/{task_id}")
def update_task(task_id: int, task_update: TaskUpdate, db: Session = Depends(get_db)):
    return update_specific_task(db, task_id, task_update)


# ✅ Delete a task
@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    return delete_specific_task(db, task_id)
