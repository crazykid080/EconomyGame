import database, beginning
import sys
import bcrypt
from secret import salt

def add_user_test(testdb, name, email, password):
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
	enc_password = bcrypt.hashpw(password, salt)
	db_password = testdb.get_password(user)
	print(db_password)
	print(enc_password)
	#print(result)
	return None
	

if __name__ == "__main__":
	if(len(sys.argv) < 2):
		print("Not enough arguments")
		exit()
	command = sys.argv[1]
	testdb = database.database('test')
	if(command == 'get_users'):
		get_users(testdb)
		exit()
	if(command == 'login'):
		login(testdb, sys.argv[2], sys.argv[3])
	if(command == 'add_user'):
		if(len(sys.argv) < 5):
			print("Not enough arguments")
			exit()
		result = add_user_test(testdb, sys.argv[2], sys.argv[3], sys.argv[4])
		print(result)
		exit()