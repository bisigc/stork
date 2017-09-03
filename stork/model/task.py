from sqlalchemy import Sequence, Column, Integer, String, Float
from stork.base import Base

class Task(Base):
	__tablename__ = 'task'
	id = Column(Integer, Sequence('task_id_seq'), primary_key=True)
	title = Column(String(255), nullable=False)
	description = Column(String(2500), nullable=True)
	duedate = Column(String(23), nullable=True)
	creator_id = Column(Integer(), nullable=False)
	assignee_id = Column(Integer(), nullable=True)
	project_id = Column(Integer(), nullable=True)
	finished = Column(Integer(), nullable=True)
	created = Column(Float(), nullable=True)
	modified = Column(Float(), nullable=True)
	
