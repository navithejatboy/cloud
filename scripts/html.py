#!/usr/bin/python2

import commands
import cgi

print "content-type: text/html"
print

a=cgi.FormContent()["python"][0]

print "{0}".format(a)
