#!/usr/bin/python2

import cgi
import commands

print "content-type: text/html"
print


os = cgi.FormContent()['os'][0]
conname = cgi.FormContent()['conname'][0]
version = cgi.FormContent()['version'][0]
imagename = cgi.FormContent()['imagename'][0]

a='0'
b='0'
c='0'
d='0'


e = cgi.FormContent()

for i in e.keys():
	if e[i][0]=="php":
		a = "php"	
	elif e[i][0]=="mysql":
		b = "mysql"
	elif e[i][0]=="net-tools":
		c =  "net-tools"
	elif e[i][0]=="httpd":
		d = "httpd" 


if os == "centos":
	status = commands.getstatusoutput("sudo docker run -dit --name {0} {1}".format(conname, os))
	if status[0]==0:
		print "<center>..Container has been launched successfully..</center> <br>"
		if a == "php":
			phpStatus = commands.getstatusoutput("sudo docker inspect {0} | sudo yum install php -y".format(conname))
			if phpStatus[0]==0:
				print "<center> php has been installed in the container </center> <br> "
			else:
				print "php not installed"
		if b == "mysql":
		        mysqlStatus = commands.getstatusoutput("sudo docker inspect {0} | sudo yum install mysql -y".format(conname))
			if mysqlStatus[0]==0:
				print "<center> mysql has been installed in the container </center> <br>"
			else:
				print "mysql not installed"
		if c == "net-tools":                
			nettoolsStatus = commands.getstatusoutput("sudo docker inspect {0} | sudo yum install net-tools -y".format(conname,c))
			if nettoolsStatus[0]==0:
				print "<center> net-tools has been installed in the container </center> <br> "
			else:
				print "net-tools not installed"
		if d == "httpd":
	                httpdStatus = commands.getstatusoutput("sudo docker inspect {0} | sudo yum install httpd -y".format(conname,d))
			if httpdStatus[0]==0:
				print "<center> httpd has been installed in the container </center> <br>"
			else:
				print "httpd not installed"        
	
	imageStatus = commands.getstatusoutput("sudo docker commit {} {}:{}".format(conname,imagename,version))
	if imageStatus[0]==0:
		print "<center> Image committed successfully </center> <br>"
		print "<center> <a href='dockerimages_list.py'> Go back to launched your committed image </a> </center>"
	else:
		print "Please try again"
