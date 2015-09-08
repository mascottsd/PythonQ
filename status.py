import sys
import scrape
import connect_db
db = connect_db.connect()
cur = connect_db.get_cursor(db)

# RETRIEVE THE HTML FOR THE JOB ID...
try:
	id = str(sys.argv[1])
	html = 'Job '+ id +' not found'
	try:
		sqlTxt = "SELECT html FROM tbl_jobs WHERE ID="+ id
		cur.execute(sqlTxt)
		row = cur.fetchone()
		if row:
			html = row[0]
			if not html:
				html = 'Job '+ id +' not yet completed'
			else:
				html = scrape.decodeHTMLEntities(html);

	finally:
		print html
	
except:
	print 'Please gimme an id'
