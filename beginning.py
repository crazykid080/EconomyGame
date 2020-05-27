from secret import secret_key

class admin:
	def mint(amount):
		econ_ref = None
		econ_ref.stored_money += amount
		return None

class economy:
	work_payment = 0.007
	wage_tax = 0.35
	referral_tax = 0.1
	
	stored_money = 1000
	
	def tax(amount, refferer_ID):
		return None
	
class player:
	able_to_work = True
	refferer_id = 0
	balance = 0.0000

	def work():
		assert(self.able_to_work)
		self.able_to_work = False
		return None
	
	def pay(amount):
		assert(self.balance > amount)
		balance -= amount
		return None
	
	def recieve(amount, sender):
		return None