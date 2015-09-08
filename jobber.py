import sys
import time
import scrape
import connect_db
db = connect_db.connect()
cur = connect_db.get_cursor(db)

outputWaiting = 1 # when we don't do any work, tell them we're waiting
# GET THE NEXT JOB IN THE LIST...
def MainFn():
	cur.execute("SELECT * FROM tbl_jobs WHERE html IS NULL OR html='' ORDER BY ID")
	try:
		row = cur.fetchone()
		id = str(row[0]);
		url = row[1]
		# SCRAPE THE URL...
		try:
			print "Retrieving Job"+ id  # row[0] is a number & doesn't concat nicely
			html = scrape.Scrape(url)
			outputWaiting = 1;
			# SAVE THE HTNL TO THE DATABASE
			html = scrape.encodeHTMLEntities(html)
			sqlTxt = 'UPDATE tbl_jobs SET html="'+ html +'" WHERE id='+ id
			# print sqlTxt
			cur.execute(sqlTxt) # save the downloaded html
			db.commit();
		except ErrTxt:
			print 'Error: '+ ErrTxt
			
	except:
		if outputWaiting:
			print 'No jobs left to perform'
		outputWaiting = 0
		
	finally:
		print 'Waiting...'
		time.sleep(5) # delays for 5 seconds
		MainFn()


MainFn()