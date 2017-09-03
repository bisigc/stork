from stork.controller.dbController import create_session
from stork.model.project import Project

class ProjectController():

	def getAllProjects(self):
		session = create_session()
		projectList = session.query(Project).order_by(Project.id).all()
		session.close()
		return projectList

	def getProjectById(self, id):
		session = create_session()
		project = session.query(Project).filter(Project.id == id).one()
		session.close()
		return project

	def addProject(self, project):
		session = create_session()
		session.add(project)
		session.commit()
		session.close()

