#!/usr/bin/python2

import commands
import cgi

print "content-type: text/html"

cName = cgi.FormContent()['x'][0]

con_rem_status=commands.getstatusoutput("sudo docker rm -f {}".format(cName))

if con_rem_status[0]==0:
	print "location: manage.py"
	print 
	
else:
	print "naah"
