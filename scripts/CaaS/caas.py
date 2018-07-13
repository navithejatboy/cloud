#!/usr/bin/python2

import commands
import cgi

print "content-type: text/html"
choice=cgi.FormContent()['choice'][0]



if choice=="launch":
	print "location: launch_inp.py"
	print
if choice=="customize":
	print "location: customize_img_inp.py"
	print
if choice=="manage":
	print "location: manage.py"
	print
if choice=="access":
	print "location: access_inp.py"
	print
else:
	print "location: ../../caas.html"
	print

