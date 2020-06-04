import database, economy, player
from economy import convert_currency
from exceptions import *
import sys
import bcrypt

def add_user_test(testdb, name, email, password):
	salt = bcrypt.gensalt()
	password = password.encode()
	enc_password = bcrypt.hashpw(password, salt)
	result = testdb.add_user(name, email, enc_password)
	return result[0]

def get_users(testdb):
	users = testdb.get_all_users()
	print(users)
	return True

def login(testdb, user, password):
	password = password.encode()
	db_password = testdb.get_password(user)
	return bcrypt.checkpw(password, db_password)

def get_tables(testdb):
	print(testdb.get_tables())
	return True

def get_balance(testdb, account_id):
	amount = testdb.get_balance(account_id)
	currency = amount/10000
	print(currency)
	return True

def add_transaction(testdb, account, amount):
	amount = convert_currency(amount)
	result, id = testdb.input_transaction(account, amount)
	return result

def add_transfer(testdb, origin, reciever, amount):
	amount = convert_currency(amount)
	result = testdb.transfer(origin, reciever, amount)
	return result

def add_money(testdb, account, amount):
	units = convert_currency(amount)
	testdb.input_transaction(account, units, "MINT")

if __name__ == "__main__":
	if(len(sys.argv) < 3):
		print("Not enough arguments")
		exit()
	command = sys.argv[1]
	testdb = database.database(sys.argv[2])
	if(command == 'get_users'):
		get_users(testdb)
		exit()
	if(command == 'get_tables'):
		get_tables(testdb)
		exit()
	if(command == 'get_balance'):
		if(len(sys.argv) < 4):
			print("Not enough arguments")
			exit()
		get_balance(testdb, sys.argv[3])
	if(command == 'add_money'):
		if(len(sys.argv) < 5):
			print("Not enough arguments")
			exit()
		add_money(testdb, sys.argv[3], float(sys.argv[4]))
	if(command == 'transfer'):
		if(len(sys.argv) < 6):
			print("Not enough arguments")
			exit()
		result = add_transfer(testdb, sys.argv[3], sys.argv[4], float(sys.argv[5]))
		print(result)
	if(command == 'add_transaction'):
		if(len(sys.argv) < 5):
			print("Not enough arguments")
			exit()
		result = add_transaction(testdb, sys.argv[3], sys.argv[4])
		print(result)
		exit()
	if(command == 'login'):
		if(len(sys.argv) < 5):
			print("Not enough arguments")
			exit()
		result = login(testdb, sys.argv[3], sys.argv[4])
		print(result)
		exit()
	if(command == 'add_user'):
		if(len(sys.argv) < 6):
			print("Not enough arguments")
			exit()
		result = add_user_test(testdb, sys.argv[3], sys.argv[4], sys.argv[5])
		print(result)
		exit()