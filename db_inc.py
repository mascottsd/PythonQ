import MySQLdb	# (1) pip install MySQL-python & (2) http://sourceforge.net/projects/mysql-python/files/mysql-python/ to get the latest installer (ie. MySQL-python-1.2.3.win32-py2.7.msi)

# IGNORE MySQL Table already exists & Field doesn't have a default value WARNINGS
from warnings import filterwarnings
filterwarnings('ignore', category = MySQLdb.Warning)


def connect():
	return MySQLdb.connect(host="127.0.0.1", # localhost didn't work
						 user="root", # your username
						 passwd="mypwd", # your password
						 db="awesome_db") # name of the data base

# a Cursor object will let you execute all the queries you need
# db.commit() must be called after UPDATEs & INSERTs
def get_cursor(db):
	return db.cursor() 
