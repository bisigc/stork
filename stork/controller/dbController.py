from stork import stork
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

app = stork.app
Base = declerative_base()

def create_engine():
	"""Creates the database engine."""
	engine = create_engine('sqlite:///' + app.config['DATABASE'], echo=True)
	return engine

def get_engine():
	"""Returns the db engine."""
	if not hasattr(g, 'sqlite_engine'):
		g.sqlite_engine = create_engine()
	return g.sqlite_engine

@app.teardown_appcontext
def close_db(error):
	"""Closes the databse again at the end of the request."""
	if hasattr(g, 'sqlite_engine'):
		g.sqlite_engine.close()

def init_db():
	engine = get_engine()
	Base.metadata.create_all(engine)

@app.cli.command('initdb')
def initdb_command():
	"""Initializes the database."""
	init_db()
	print('Initialized the datbase.')

def create_session():
	Session = sessionmaker(bind=get_engine)
	return Session()

