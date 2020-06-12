import economy
import database
import sys
if __name__ == "__main__":
	if(len(sys.argv) == 0):
		print("Please provide a database")
		exit() 
	db_name = sys.argv[1]
	database = database.database(db_name)
	economy = economy.economy(database)