#!/usr/bin/python2

import cgi
import commands


print "content-type: text/html"
print


a = cgi.FormContent()['python'][0]

fh=open("/webcontent/scripts/user1.py",'w')
fh.write(a)
fh.close()

commands.getstatusoutput(" chmod +x /webcontent/scripts/user1.py")
print commands.getoutput(" python /webcontent/scripts/user1.py ")


