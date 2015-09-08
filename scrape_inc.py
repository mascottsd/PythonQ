import mechanize	# pip install mechanize

# The URL to this service
# URL = 'http://www.google.com'

def Scrape(url):
	# Create a Browser instance
	br = mechanize.Browser()

	# Browser options
	br.set_handle_equiv(True)
	br.set_handle_redirect(True)
	br.set_handle_referer(True)
	br.set_handle_robots(False)

	# Follows refresh 0 but not hangs on refresh > 0
	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

	# User-Agent (this is cheating, ok?)
	br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

	# Load the page
	if not url.startswith('http'):
	 	url = "http://"+ url;
	print "Downloading "+ url
	r = br.open(url)
	return r.read()

	
def encodeHTMLEntities(text):
	entities = [
		['amp', '&'],
		['quot', '"'],
		['apos', '\''],
		['lt', '<'],
		['gt', '>'],
	]
	for i in range(0, len(entities) ): 
		text = text.replace(entities[i][1], '&'+entities[i][0]+';')
	return text

def decodeHTMLEntities(text):
	entities = [
		['amp', '&'],
		['quot', '"'],
		['apos', '\''],
		['lt', '<'],
		['gt', '>'],
	]
	for i in range(0, len(entities) ): 
		text = text.replace('&'+entities[i][0]+';', entities[i][1])
	return text
