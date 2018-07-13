#!/usr/bin/python2

import cgi
import commands

print "content-type: text/html"
print 

cmd=cgi.FormContent()['code'][0]

print commands.getstatusoutput("sudo docker exec centos1 {}".format(cmd))












