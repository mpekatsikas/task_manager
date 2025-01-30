from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from backend.app.api.endpoints import tasks
from backend.app.auth.auth import auth
from backend.app.db.database import Base, engine

app = FastAPI(title="Task Manager API", version="1.0.0")


@app.on_event("startup")
def on_startup():
    # Ensure all tables are created
    Base.metadata.create_all(bind=engine)


# Include API routers
app.include_router(tasks.router, prefix="/tasks", tags=["tasks"], dependencies=[Depends(auth)])

@app.get("/")
def root():
    return {"message": "Welcome to the Task Manager API!"}


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
