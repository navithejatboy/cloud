#!/usr/bin/python2

import cgi
import commands


print "content-type: text/html"
print


a = cgi.FormContent()['c'][0]

f=open("/webcontent/scripts/user.c",'w')
f.write(a)
f.close()

commands.getstatusoutput(" chmod +x user.c")
a=commands.getstatusoutput("gcc -o user user.c ")
print commands.getoutput("./user")
