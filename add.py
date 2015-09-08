import sys
import connect_db
db = connect_db.connect()
cur = connect_db.get_cursor(db)
	
def isset(x):
	return x in locals() or x in globals()
	
# CREATE THE TABLE IF NECESSARY...
try:
	cur.execute("CREATE TABLE IF NOT EXISTS tbl_jobs (	\
		id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,	\
		url varchar(1024) NOT NULL,	\
		html text,					\
		created_at datetime,		\
		updated_at datetime)")

finally:
	# ADD THE JOB TO THE DATABASE...
	try:
		url = sys.argv[1]
		sqlTxt = 'INSERT INTO tbl_jobs (url) VALUES ("'+ url +'")'
		cur.execute(sqlTxt)
		db.commit();
		print cur.lastrowid
		
	except:
		print 'Please gimme a url as the first argument'
