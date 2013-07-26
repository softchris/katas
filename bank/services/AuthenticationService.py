from dto import User
class AuthenticationService:
	def __init__(self):
		self.isAuthenticated = False
		self.users = []
		self.initUsers()
	def initUsers(self):
		self.users.append(User.User("karl karlsson"))
	def authenticate(self, username, password):
		for user in users:
			if user.username == username and user.password == password:
				self.isAuthenticated = True
