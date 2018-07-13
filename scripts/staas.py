#!/usr/bin/python2

import cgi

print "content-type: text/html"

staas_choice=cgi.FormContent()["staas_choice"][0]
if staas_choice=="staas_object":
	print "location: ../staas_object.html"
	print
if staas_choice=="staas_block":
	print "location: ../staas_block.html"
	print
