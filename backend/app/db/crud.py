from sqlalchemy.orm import Session
from backend.app.db.models import Task
from backend.app.db.schemas import TaskCreate, TaskUpdate
from fastapi import HTTPException

# ✅ Retrieve all tasks
def get_tasks(db: Session):
    return db.query(Task).all()

# ✅ Retrieve a single task by ID
def get_task(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()

# ✅ Create a new task
def create_new_task(db: Session, task: TaskCreate):
    db_task = Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

# ✅ Update an existing task
def update_specific_task(db: Session, task_id: int, task_update: TaskUpdate):
    db_task = db.query(Task).filter(Task.id == task_id).first()

    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")

    for key, value in task_update.dict(exclude_unset=True).items():
        setattr(db_task, key, value)

    db.commit()
    db.refresh(db_task)
    return db_task

# ✅ Delete a task
def delete_specific_task(db: Session, task_id: int):
    db_task = db.query(Task).filter(Task.id == task_id).first()

    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(db_task)
    db.commit()
    return {"message": "Task deleted successfully"}