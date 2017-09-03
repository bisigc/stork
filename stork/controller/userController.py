from stork.controller.dbController import create_session
from stork.model.user import User

class UserController():

	def getAllUsers(self):
		session = create_session()
		userList = session.query(User).order_by(Task.username).all()
		session.close()
		return userList

	def getUserById(self, id):
		session = create_session()
		user = session.query(User).filter(User.id == id).one()
		session.close()
		return user

	def addUser(self, user):
		session = create_session()
		session.add(user)
		session.commit()
		session.close()

