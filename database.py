from secret import secret_key
import sqlalchemy as db
from sqlalchemy import Table, Column, Numeric, Integer, String, MetaData, ForeignKey, DateTime
from sqlalchemy.sql import text
from sqlalchemy.orm import sessionmaker
import datetime
from exceptions import *

class database:
	connection = None
	session = None
	metadata = None
	users = None
	accounts = None
	transactions = None
	def __init__(self, name='main'):
		engine = db.create_engine('sqlite:///'+name+'.sqlite')
		self.connection = engine.connect()
		Session = sessionmaker(bind=engine)
		self.session = Session()
		self.metadata = MetaData()
		
		self.users = Table('users', self.metadata, 
		Column('id', Integer, primary_key=True),
		Column('username', String(25) ),
		Column('email', String(40) ),
		Column('password', String(80) ) )
		
		self.accounts = Table('accounts', self.metadata,
		Column('id', Integer, primary_key=True),
		Column('holder', Integer),
		Column('units', Integer)
		)
		
		self.transactions = Table('transactions', self.metadata,
		Column('id', Integer, primary_key=True),
		Column('timestamp', DateTime, default=datetime.datetime.utcnow()),
		Column('account_id', Integer),
		Column('units', Integer),
		Column('ref_id', Integer)
		)
		
		self.metadata.create_all(engine)

	def input_transaction(self, account, amount, ref_id=None):
		timestamp = datetime.datetime.utcnow()
		new_transaction = self.transactions.insert().values(timestamp=timestamp,account_id=account,units=amount, ref_id=ref_id)
		balance = self.get_balance(account)
		balance = balance + amount
		account_update = self.accounts.update().where(self.accounts.c.id == account).values(units=balance)
		self.session.execute(account_update)
		result = self.session.execute(new_transaction)
		self.session.commit()
		transaction_id = result.lastrowid
		return True, transaction_id
	
	def transfer(self, origin_id, reciever_id, amount):
		self.verify_account(reciever_id)
		origin_balance = self.get_balance(origin_id)
		if(origin_balance < amount): raise NotEnoughUnits
		result, ref_id_o = self.input_transaction(origin_id, -amount)
		result, ref_id_r = self.input_transaction(reciever_id, amount, ref_id_o)
		#update first transaction with ref id
		update = self.transactions.update().where(self.transactions.c.id == ref_id_o).values(ref_id=ref_id_r)
		self.session.execute(update)
		self.session.commit()
		return True
	
	def get_user(self, username):
		user = self.session.query(self.users).filter_by(username=username).all()
		if(user  == []): user = None
		return user
	
	def get_all_users(self):
		users = self.session.query(self.users).all()
		return users
	
	def get_email(self, email):
		user = self.session.query(self.users).filter_by(email=email).all()
		if(user  == []): user = None
		return user
	
	def get_password(self, user):
		user = self.session.query(self.users).filter_by(username=user).all()
		if(user  == []): raise NoUserExists
		return user[0][3]	
	
	def get_balance(self, account_id):
		account = self.session.query(self.accounts).filter_by(id=account_id).all()
		if(account == []): raise NoAccountExists
		return account[0][2]
		
	def verify_account(self, account_id):
		account = self.session.query(self.accounts).filter_by(id=account_id).all()
		if(account == []): raise NoAccountExists
		else: return True
		
	def add_user(self, name, email, password):
		#verify user does not exist
		try:
			user_check = self.get_user(name)
			#verify email does not exist
			email_check = self.get_email(email)
			if(user_check != None): raise UserExists
			if(email_check != None): raise UserExists
		except UserExists:
			print("User already exists")
			return False, None
		#sanitize. How? Regex maybe?
		#add user to database
		new_user = self.users.insert().values(username=name, email=email, password=password)
		result = self.session.execute(new_user)
		self.session.commit()
		user_id = result.lastrowid
		self.add_account(user_id)
		return True, user_id
	
	def add_account(self, holder, amount=0):
		new_account = self.accounts.insert().values(holder=holder, units=amount)
		self.session.execute(new_account)
		self.session.commit()
		return True

	def add_units(self, account_id, amount):
		units_update = self.accounts.update().where(self.accounts.c.id == account_id).values(units=amount)
		self.session.execute(units_update)
		self.session.commit()

	def change_password(self, user, new_password):
		#verify user exists
		if(get_user(user) == None): raise NoUserExists
		#get current password from db
		old_password = get_password(user)
		#compare current to old, return false if false
		if(bcrypt.verify(new_password, old_password)): raise SamePassword
		return None

	def get_tables(self):
		return self.metadata.tables.keys()

if __name__ == '__main__':
	maindb = database('direct')