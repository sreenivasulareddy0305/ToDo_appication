from fastapi import FastAPI,HTTPException
import schemas
import models
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from fastapi.params import Depends
models.Base.metadata.create_all(engine)


app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/')
def index():
    return {"Welcome to ToDo application"}


@app.get("/tasks_list")
def tasks_list(db: Session = Depends(get_db)):
    """ Function to display all tasks present in db"""
    all_tasks = db.query(models.Tasks).all()
    if all_tasks:
        return all_tasks
    return {"No tasks are assigned"}


@app.get('/task/{id}')
def get_task(id, db: Session = Depends(get_db)):
    """ Function to get details of each individual task """
    task = db.query(models.Tasks).filter(models.Tasks.task_id == id).first()
    if task:
        return task
    raise HTTPException(status_code=404, detail="Task Not Found ")


@app.post("/addtask")
def add_task(request: schemas.Tasks, db: Session = Depends(get_db)):
    """ Function to create or add new task"""
    new_task = models.Tasks(task_name=request.task_name,
                            task_id=request.task_id)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


@app.put('/update/{id}')
def update_task(id, request: schemas.Tasks, db: Session = Depends(get_db)):
    """ Function to update the task"""
    task = db.query(models.Tasks).filter(models.Tasks.task_id == id)
    if not task.first():
        return {"There is no task with id : {id}"}
    task.update(request.dict())
    db.commit()
    return {"Successfully updated the task"}


@app.delete('/task/{id}')
def delete_task(id, db: Session = Depends(get_db)):
    """ Function to deleate the task """
    # db.query(models.Tasks).filter(models.Tasks.task_id == id).delete(synchronize_session=False)
    task = db.query(models.Tasks).get(id)
    # db.commit()
    if task:
        db.delete(task)
        db.commit()
        return {"product deleted"}
    return {f"there is no task to delete with id : {id}"}
