from pydantic import BaseModel
from typing import Optional

# ✅ Base Task Schema
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

# ✅ Schema for Creating a New Task (inherits TaskBase)
class TaskCreate(TaskBase):
    pass

# ✅ Schema for Updating a Task (allows partial updates)
class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

# ✅ Schema for Reading Tasks (includes an ID)
class Task(TaskBase):
    id: int

    class Config:
        orm_mode = True