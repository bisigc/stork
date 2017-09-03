import os
from stork.controller import dbController
from stork.controller.projectController import ProjectController
from stork.controller.taskController import TaskController
from flask import Flask, request, session, redirect, url_for, abort, render_template, flash

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
	DATABASE=os.path.join(app.root_path, 'stork.db'),
	SECRET_KEY='development key',
	USERNAME='admin',
	PASSWORD='default'
	)
)

# Load additional (or overwrite) configuration from a file set in the env variable STORK SETTINGS. If not sent, no exception will be thrown (silent)
app.config.from_envvar('STORK_SETTINGS', silent=True)

@app.route("/")
def index():
	projectCtrl = ProjectController()
	projectList = projectCtrl.getAllProjects()	
	return render_template('projectList.html', projectList=projectList)

@app.route("/project/<id>")
def projectListView(id):
	projectCtrl = ProjectController()
	project = projectCtrl.getProjectById(id)	
	taskCtrl = TaskController()
	taskList = taskCtrl.getTasksByProjectId(id)	
	return render_template('projectTaskList.html', project=project, taskList=taskList)

@app.cli.command('initdb')
def initdb_command():
	dbController.init_db()

@app.teardown_appcontext
def close_db_context(error):
	dbController.close_db(error)

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

