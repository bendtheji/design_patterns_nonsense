class Customer(object):

	def __init__(self, name, balance):
		self.name = name
		self.balance = balance

	def withdraw(self, amount):

		if amount > self.balance:
			raise RuntimeError('Amount greater than available balance.')
		self.balance -= amount
		return self.balance

	def deposit(self, amount):

		self.balance += amount
		return self.balance

	@staticmethod
	def make_complain_noise():
		print "Where's your manager?"	

def main():
	first_customer = Customer("Bryan", 730.57)

	print first_customer.withdraw(50.0)
	Customer.make_complain_noise()

if __name__ == "__main__":
	main()				


