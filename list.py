import connect_db
cur = connect_db.connect()
		
cur.execute("SELECT * FROM tbl_jobs")
for row in cur.fetchall() :
	print row[0] ,'-', row[1]
