from sqlalchemy import Sequence
from ../controller/dbController import Base

class Project(Base):
	__tablename__ = 'project'
	id = Column(Integer, Sequence('project_id_seq'), primary_key=True)
	title = Column(String(255), nullable=False)
	description = Column(String(2500), nullable=True)
	creator_id = Column(Integer(), nullable=False)
	created = Column(Float(), nullable=True)
	modified = Column(Float(), nullable=True)
	
