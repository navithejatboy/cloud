#!/usr/bin/python2

import cgi 
import commands

print "content-type: text/html"
print


print "<form action=launch.py>"
z=1
print "<h2>Currently available images </h2>"	
print "<select name='imagename'> <br>"
for i in  commands.getoutput("sudo docker images").split('\n'):
	if z == 1:
		z=z+1
		pass
	else:
		j=i.split()
		print "<option>" +  j[0] + ":" + j[1] + "</option>"

print """
</select>
<br />
<br />
Enter container name  <input type='text' name='name'>
<input type='submit'>
</form>
"""
