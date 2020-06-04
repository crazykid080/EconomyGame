def convert_currency(self, amount):
	units = amount * 10000
	return units

class economy:
	work_payment = 0.007
	wage_tax = 0.35
	referral_tax = 0.1
	
	budget = 1000
	
	def work_tax(self, units, refferer_ID):
		taxed = units * wage_tax
		units -= taxed
		units = round(units, 4) #Prevent floating point errors
		budget += round(taxed, 4)
		return units