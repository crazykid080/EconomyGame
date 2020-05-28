from secret import secret_key
import sqlalchemy as db
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

class database:
	connection = None
	users = None #Bad way to do it? Probably.
	def __init__(self, name='main'):
		engine = db.create_engine('sqlite:///'+name+'.sqlite')
		self.connection = engine.connect()
		metadata = MetaData()
		self.users = Table('users', metadata, 
		Column('id', Integer, primary_key=True),
		Column('username', String(25) ),
		Column('email', String(40) ),
		Column('password', String(70) ) )
	
	def get_user(self, username):
		user = self.connection.query(users).filter_by(username=username)
		return user
	
	def get_email(self, email):
		user = self.connection.query(users).filter_by(email=email)
		return user
	
	def add_user(self, name, email, password):
		#verify user does not exist
		user_check = get_user(name)
		if(user_check != None):
			raise Exception
		#verify email does not exist
		user_check = get_email(email)
		if(user_check != None):
			raise Exception
		#sanitize. How? Regex maybe?
		#add user to database
		return None
	
	def change_password(self, user, old_password, new_password):
		#verify user exists
		#get current password from db
		#compare current to old, return false if false
		if(old_password == new_password):
			raise Exception
		return None

if __name__ == '__main__':
	maindb = database()
	insertion = None