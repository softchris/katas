
import unittest
from dto import Account
from services import AuthenticationService

class AccountTest(unittest.TestCase):
	def testDeposit(self):
		a = Account.Account("pelle persson")
		a.deposit(100)
		self.assertEqual(a.balance,100)
	def testWithdrawOvercharge(self):
		authService = AuthenticationService.AuthenticationService
		a = Account.Account("pelle persson",50)
		a.withdraw(100,authService)
		self.assertEqual(a.balance,0)


if __name__ == '__main__':
    unittest.main()