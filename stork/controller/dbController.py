from flask import current_app as app
from flask import g
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from stork import base

def get_engine():
	"""Returns the db engine."""
	if not hasattr(g, 'sqlite_engine'):
		g.sqlite_engine = create_engine('sqlite:///' + app.config['DATABASE'], echo=True)
	return g.sqlite_engine

def close_db(error):
	"""Closes the databse again at the end of the request."""
	if hasattr(g, 'sqlite_engine'):
		g.sqlite_engine.dispose()

def init_db():
	engine = get_engine()
	from stork.model import user, note, task, project
	base.Base.metadata.drop_all(engine)
	base.Base.metadata.create_all(engine)
	# Do script import with basic sqlite3 library
	import sqlite3
	db = sqlite3.connect(app.config['DATABASE'])
	db.row_factory = sqlite3.Row
	with app.open_resource('data.sql', mode='r') as f:
		db.cursor().executescript(f.read())
	db.commit()
	db.close()

def create_session():
	Session = sessionmaker(bind=get_engine())
	return Session()

