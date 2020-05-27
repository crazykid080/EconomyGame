from secret import secret_key
import sqlalchemy as db
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

class database:
	def __init__(self):
		engine = db.create_engine('sqlite:///main.sqlite')
		connection = engine.connect()
		metadata = MetaData()
		users = Table('users', metadata, 
		Column('id', Integer, primary_key=True),
		Column('username', String(25)),
		Column('password', String(70)) )

if __name__ == '__main__':
	maindb = database()
	insertion = None