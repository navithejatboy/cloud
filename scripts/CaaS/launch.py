#!/usr/bin/python2

import cgi
import commands

print "content-type: text/html"
print

imageName = cgi.FormContent()['imagename'][0]
cName = cgi.FormContent()['name'][0]

if commands.getstatusoutput("sudo docker inspect {}".format(cName))[0] == 0:
	print "Container name {} already exists <br>".format(cName)
	print "<a href='launch_inp.py'> Go back and launch by another name </a>"
else:	
	if commands.getstatusoutput("sudo docker run -dit --name {} {}".format(cName,imageName))[0]==0:
		print "Container is launched <br>"
		print "<a href='manage.py'> Click here to manage container </a>"
	else:
		print "Try again"
