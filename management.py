import database, economy, player
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
	amount = testdb.convert_currency(amount)
	result, id = testdb.input_transaction(account, amount)
	return result

def add_transfer(testdb, origin, reciever, amount):
	amount = testdb.convert_currency(amount)
	testdb.transfer(origin, reciever, amount)

if __name__ == "__main__":
	if(len(sys.argv) < 2):
		print("Not enough arguments")
		exit()
	command = sys.argv[1]
	testdb = database.database('test')
	if(command == 'get_users'):
		get_users(testdb)
		exit()
	if(command == 'get_tables'):
		get_tables(testdb)
		exit()
	if(command == 'get_balance'):
		if(len(sys.argv) < 3):
			print("Not enough arguments")
			exit()
		get_balance(testdb, sys.argv[2])
	if(command == 'transfer'):
		if(len(sys.argv) < 5):
			print("Not enough arguments")
			exit()
		add_transfer(testdb, sys.argv[2], sys.argv[3], int(sys.argv[4]))
	if(command == 'add_transaction'):
		if(len(sys.argv) < 4):
			print("Not enough arguments")
			exit()
		result = add_transaction(testdb, sys.argv[2], sys.argv[3])
		print(result)
		exit()
	if(command == 'login'):
		if(len(sys.argv) < 4):
			print("Not enough arguments")
			exit()
		result = login(testdb, sys.argv[2], sys.argv[3])
		print(result)
		exit()
	if(command == 'add_user'):
		if(len(sys.argv) < 5):
			print("Not enough arguments")
			exit()
		result = add_user_test(testdb, sys.argv[2], sys.argv[3], sys.argv[4])
		print(result)
		exit()