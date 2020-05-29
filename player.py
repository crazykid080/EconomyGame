class player:
	able_to_work = True
	refferer_id = 0
	balance = 0.0000

	def work(self):
		if(not self.able_to_work):
			raise Exception
		self.able_to_work = False
		econ_ref.work_tax(econ_ref.work_payment)
		return None
	
	def pay(self, amount, player):
		if((self.balance > amount and amount > 0) == False):
			raise Exception
		balance -= amount
		return None
	
	def recieve(self, amount, sender):
		assert(amount > 0) #Prevent negative transfers
		return None