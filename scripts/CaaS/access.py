#!/usr/bin/python2

import commands
import cgi

print "content-type: text/html"
print

d_name=cgi.FormContent()['c_name'][0]
port_number=cgi.FormContent()['port_number'][0]

print "1"
if commands.getstatusoutput("sudo docker inspect {}".format(c_name))[0] == 0:
	print "2"
	print "Container name {} already exists <br>".format(c_name)
	print "<a href='access_inp.py'> Go back and launch by another name </a>"
else:	
	if commands.getstatusoutput("sudo docker run -dit -p {1}:22 --name {0} centos:latest".format(c_name,port_number))[0]==0:
		print "Container is launched <br>"
		print "<a href='manage.py'> Click here to manage container </a>"
	else:
		print "Try again"
