from sqlalchemy import Sequence, Column, Integer, String, Float
from stork.base import Base

class User(Base):
	__tablename__ = 'user'
	id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
	username = Column(String(100), nullable=False)
	password = Column(String(255), nullable=False)
	firstname = Column(String(255), nullable=True)
	surname = Column(String(255), nullable=True)
	email = Column(String(255), nullable=False)
	mobile = Column(String(50), nullable=True)
	created = Column(Float(), nullable=True)
	modified = Column(Float(), nullable=True)

