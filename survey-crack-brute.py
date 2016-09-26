import itertools
from itertools import product
import string
import urllib
import urllib2
import re
import time
import requests
from requests.exceptions import HTTPError
# Set password complexity - remove string character sets not required
chars = string.uppercase
days = 0
content = ''
i = ''
req = ''
# Set max password length to crack - change 10 to desired length 
for guess in itertools.product((chars), repeat=2):
	i = ''.join(guess)
	# Set URL to page receiving login POST data - Change url within single quotes
	req = urllib2.Request('http://tinyurl.com/SEC580-45177-'+str(i))
	try:
		urllib2.urlopen(req)
	except urllib2.HTTPError as e:
		#print e.code
		continue
	content = urllib2.urlopen(req).read()
	#uncomment below to debug returned content 
	#print content
	matches = re.findall(r'(?i)Unable to find', content)
	#uncomment below to debug regex query
	#print matches
	if len(matches) > 0:
	#uncomment below to debug attempted passwords
		print i + " - is not the URL"
		#uncomment below to throttle down script speed - change sleep timer as needed
		#time.sleep(0.1)
		continue
	else:
		print "\n\nURL found - http://tinyurl.com/SEC580-45177-" + i
		days = days + 1
		if days > 99:
			break
		else:
			continue