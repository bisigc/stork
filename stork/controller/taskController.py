from stork.controller.dbController import create_session
from stork.model.task import Task

class TaskController():

	def getAllTasks(self):
		session = create_session()
		taskList = session.query(Task).order_by(Task.id).all()
		session.close()
		return taskList

	def getTasksByProjectId(self, projectId):
		session = create_session()
		taskList = session.query(Task).filter(Task.project_id == projectId).all()
		session.close()
		return taskList

	def getTaskById(self, id):
		session = create_session()
		task = session.query(Task).filter(Task.id == id).one()
		session.close()
		return task

	def addTask(self, task):
		session = create_session()
		session.add(task)
		session.commit()
		session.close()

