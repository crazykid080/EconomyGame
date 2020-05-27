from secret import secret_key

econ_ref = None

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
	
	def work_tax(amount, refferer_ID):
		taxed = amount * wage_tax
		amount -= taxed
		amount = round(amount, 4) #Prevent floating point errors
		return amount
	
class player:
	able_to_work = True
	refferer_id = 0
	balance = 0.0000

	def work():
		assert(self.able_to_work)
		self.able_to_work = False
		econ_ref.work_tax(econ_ref.work_payment)
		return None
	
	def pay(amount, player):
		assert(self.balance > amount and amount > 0)
		balance -= amount
		return None
	
	def recieve(amount, sender):
		assert(amount > 0) #Prevent negative transfers
		return None