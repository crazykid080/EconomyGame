import database, economy, player
import sys
import bcrypt

def add_user_test(testdb, name, email, password):
	salt = bcrypt.gensalt()
	password = password.encode()
	enc_password = bcrypt.hashpw(password, salt)
	result = testdb.add_user(name, email, enc_password)
	return result

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

def add_transaction(testdb, account, amount):
	result, id = testdb.input_transaction(account, amount)
	return result

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