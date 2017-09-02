from sqlalchemy import Sequence
from ../controller/dbController import Base

class Note(Base):
	__tablename__ = 'note'
	id = Column(Integer, Sequence('note_id_seq'), primary_key=True)
	note = Column(String(2500), nullable=True)
	creator_id = Column(Integer(), nullable=False)
	task_id = Column(Integer(), nullable=False)
	created = Column(Float(), nullable=True)
	modified = Column(Float(), nullable=True)
	

drop table if exists project;
create table project (
id integer primary key autoincrement,
title text,
description text,
creator_id integer not null,
created real not null,
modified real not null);

drop table if exists user;
create table user (
id integer primary key autoincrement,
username text not null,
password text not null,
firstname text,
surname text,
email text not null,
mobile text,
created real not null,
modified real not null);


insert into user (username, password, email, created, modified) VALUES ('cbi', 'test', 'cbisig@gmail.com', date('now'), date('now'));

