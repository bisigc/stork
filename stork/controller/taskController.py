from ../stork import app
from dbController import get_db
from flask import request, render_template

@app.route('/task', methods=['GET'])
def getAllTasks():
	db = get_db()
	cur = db.execute('select title, created from task order by duedate, modified')
	entries = cur.fetchall()
	return render_template

@app.route('/task', methods=['PUT'])
def addTask():
	if not session.get('username'):
		abort(401)
	db = get_db()
	db.execute(
	
