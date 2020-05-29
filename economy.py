class economy:
	work_payment = 0.007
	wage_tax = 0.35
	referral_tax = 0.1
	
	budget = 1000
	
	def work_tax(self, amount, refferer_ID):
		taxed = amount * wage_tax
		amount -= taxed
		amount = round(amount, 4) #Prevent floating point errors
		budget += round(taxed, 4)
		return amount