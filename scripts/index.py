#!/usr/bin/python2

import cgi

print "content-type: text/html"


user_name=cgi.FormContent()['user_name'][0]
user_pass=cgi.FormContent()['user_pass'][0]

auser="navi"
apass="1"

if user_name==auser and user_pass==apass :
	print "location: ../welcome.html"
	print
else:
	print "location: ../index.html"
	print

