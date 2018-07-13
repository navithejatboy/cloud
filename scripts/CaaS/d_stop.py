#!/usr/bin/python2

import cgi
import commands

print "content-type: text/html"

cName = cgi.FormContent()['x'][0]

con_stop_status=commands.getstatusoutput("sudo docker kill {0}".format(cName))

if con_stop_status[0]  == 0:
        print "location:  manage.py"
        print
else:
        print "not removed"
