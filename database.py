from secret import secret_key
import sqlalchemy as db
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

def __init__():
	engine = db.create_engine('sqlite:///main.sqlite')
	connection = engine.connect()
	metadata = MetaData()
	users = Table('users', metadata, 
	Column('id', Integer, primary_key=True),
	Column('username', String(25)),
	Column('password', String(70)) )

if __name__ == '__main__':
	__init__()
	insertion = None