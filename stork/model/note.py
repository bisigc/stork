from sqlalchemy import Sequence
from controller import dbController.Base

class Note(Base):
	__tablename__ = 'note'
	id = Column(Integer, Sequence('note_id_seq'), primary_key=True)
	note = Column(String(2500), nullable=True)
	creator_id = Column(Integer(), nullable=False)
	task_id = Column(Integer(), nullable=False)
	created = Column(Float(), nullable=True)
	modified = Column(Float(), nullable=True)
	
