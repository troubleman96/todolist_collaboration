# backend_fastapi/app/todos.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, database
from app.database import get_db

router = APIRouter()

@router.post("/todos", response_model=schemas.TaskOut)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    new_task = models.Task(**task.dict(), user_id=1)  # Hardcoded for demo
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@router.get("/todos", response_model=list[schemas.TaskOut])
def get_tasks(db: Session = Depends(get_db)):
    return db.query(models.Task).filter(models.Task.user_id == 1).all()

@router.put("/todos/{task_id}", response_model=schemas.TaskOut)
def update_task(task_id: int, task: schemas.TaskCreate, db: Session = Depends(get_db)):
    db_task = db.query(models.Task).get(task_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    for k, v in task.dict().items():
        setattr(db_task, k, v)
    db.commit()
    return db_task

@router.delete("/todos/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    return {"detail": "Deleted"}