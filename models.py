from email.policy import default
from sqlalchemy import Boolean, Column, Integer, String
from database import Base


class Tasks(Base):
    __tablename__ = "tasks"
    task_name = Column(String(100))
    task_id = Column(Integer, primary_key=True)
