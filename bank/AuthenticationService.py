import User
class AuthenticationService:
	def __init__(self):
		self.isAuthenticated
		self.user = None
		self.users = []
	def initUsers(self):
		user = User.User("pelle","persson")
		self.users.push(user)

	def login(user,self,username,password):
		for user in self.users:
			if user.username == username and user.password == password:
				self.isAuthenticated = True
	def getUser(self,username):
		returnValue = None
		for user in self.users:
			if user.username == username:
				returnValue = user
		return returnValue	