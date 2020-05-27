from secret import secret_key
import sqlalchemy
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey


if __name__ == '__main__':
	metadata = MetaData()
	users = Table('users', metadata, 
	Column('id', Integer, primary_key=True),
	Column('username', String),
	Column('password', String) )