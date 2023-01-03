from pydantic import BaseModel


class Tasks(BaseModel):
    task_id : int
    task_name: str
    
