#!/usr/bin/python2

import cgi
import commands

print "content-type: text/html"

cName = cgi.FormContent()['x'][0]

con_start_status=commands.getstatusoutput("sudo docker start {0}".format(cName))

if con_start_status[0]  == 0:
        print "location:  manage.py"
        print
else:
        print "not removed"
