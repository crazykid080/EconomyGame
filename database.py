from secret import secret_key
import sqlalchemy as db
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

class database:
	connection = None
	users = None #Bad way to do it? Probably.
	def __init__(self):
		engine = db.create_engine('sqlite:///main.sqlite')
		self.connection = engine.connect()
		metadata = MetaData()
		self.users = Table('users', metadata, 
		Column('id', Integer, primary_key=True),
		Column('username', String(25)),
		Column('password', String(70)) )

if __name__ == '__main__':
	maindb = database()
	insertion = None