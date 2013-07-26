class Account:
	def __init__(self,accountOwner,startSum=0):
		self.owners = [] 
		self.owners.append(accountOwner)
		self.balance = startSum
	def deposit(self,amount):
		self.balance += amount
	def withdraw(self,amount, authenticationService):
		self.balance -= amount
	def addOwner(self,newOwner, authenticationService):
		self.owners.append(newOwner)


# adding money can be done without permission
# withdrawing needs to be authenticated
# adding an owner can only be done as authenticated and by one of the previous owners

# task is to add authentication in a loose coupling manner
# task is to enforce all business rules

