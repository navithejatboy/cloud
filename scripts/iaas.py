#!/usr/bin/python2

import cgi
import commands

print "content-type: text/html"
print 

osname = cgi.FormContent()['osname'][0]
ostype = cgi.FormContent()['ostype'][0]
cpu = cgi.FormContent()['cpu'][0]
storage = cgi.FormContent()['storage'][0]
ram = cgi.FormContent()['ram'][0]
port = cgi.FormContent()['port'][0]


ossetup="sshpass -p redhat -o ssh stricthostkeychecking=no root -l sudo virt-install --name {0} --location /os/rhel-server-7.3-x86_64-dvd.iso --os-type linux --os-variant {1} --memory {2} --vcpus {3} --disk /var/lib/libvirt/images/{0}.qcow2,size={4} --graphics vnc,password=redhat,listen=0.0.0.0,port={5} --noautoconsole".format(osname,ostype,ram,cpu,storage,port)

ossetup=commands.getstatusoutput(ossetup)

if ossetup[0] == 0:
	#print "content-type: text/html"
 	#print ("Location:red.py")
	print "<script> alert('Congratulations, your setup is complete...you can access your OS by running this command on you terminal : vncviewer 192.168.43.60:" +port +"')</script>"
	#print "Your OS has been launched <br> "
	#print "Access the OS by entering details : <br>" 
	#print "<form action='vncc.py'>"
	#print "Port Number you want to access your os <input type='text' name='portNumber' />"
	#a = cgi.FormContent()['port'][]
	#print "<input type='hidden' name='pp' value='{}'>".format(port)
	#print "<input type='submit'>"
	#print "</form>"
	#print "print <a href='/vnc/vnc.html' > click here to access your os in browser </a>"
	print "<form action='red.py'>"
	print "Your OS is Created.If you want to open you file you can access it at the given IP or we can do it for you. Just enter the given details<br>"
	print "Enter ip address <input type='text' name='ip'><br>"
	print "Enter username <input type='text' name='uname'><br>"
	print "Enter password <input type='password' name='pass'><br>"
	print "<button type='submit'>Submit</button>"
else:
	print "<script> alert('ERROR!!! TRY AGAIN')</script>"
	
	
#print "<center><h1> OR </h1></center> "
#print "<a href='/vnc/vnc.html' > click here to access your os in browser </a>"





"""
!/usr/bin/python2

import cgi
import commands
print "content-type: text/html"
print 



osname = cgi.FormContent()['osname'][0]
ostype = cgi.FormContent()['ostype'][0]
cpu = cgi.FormContent()['cpu'][0]
storage = cgi.FormContent()['storage'][0]
ram = cgi.FormContent()['ram'][0]
port = cgi.FormContent()['port'][0]


ossetup="sudo virt-install --name {0} --location /os/rhel-server-7.3-x86_64-dvd.iso --os-type linux --os-variant {1} --memory {2} --vcpus {3} --disk /var/lib/libvirt/images/{0}.qcow2,size={4} --graphics vnc,listen=0.0.0.0,port={5} --noautoconsole".format(osname,ostype,ram,cpu,storage,port)

ossetup=commands.getstatusoutput(ossetup)

if ossetup[0] == 0:
	print "<script> alert('Congratulations, your setup is complete.')</script>"
else:
	print "Error....try again"


"""

