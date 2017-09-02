from sqlalchemy import Sequence
from ../controller/dbController import Base

class Task(Base):
	__tablename__ = 'task'
	id = Column(Integer, Sequence('task_id_seq'), primary_key=True)
	title = Column(String(255), nullable=False)
	description = Column(String(2500), nullable=True)
	duedate = Column(String(23), nullable=True)
	creator_id = Column(Integer(), nullable=False)
	assignee_id = Column(Integer(), nullable=False)
	assignee_id = Column(Integer(), nullable=True)
	project_id = Column(Integer(), nullable=True)
	finished = Column(Integer(), nullable=True)
	created = Column(Float(), nullable=True)
	modified = Column(Float(), nullable=True)
	

drop table if exists note;
create table note (
id integer primary key autoincrement,
note text,
creator_id integer not null,
task_id integer not null,
created real not null,
modified real not null);

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

