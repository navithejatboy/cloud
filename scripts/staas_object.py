#!/usr/bin/python2

import cgi 

print "content-type: text/html"
print

option = cgi.FormContent()['option'][0]
print option


if option == "create":
	print """
<form action='object/create.py'>
Enter username <input type='text' name='username' />
<br />
Enter size <input type='number' name='size' />
<br />
Enter ip on which the storage is to be mounted <input type='number' name='ipaddress' />
<br />
Enter root password of that ip <input type='password' name='password' />
<br />
<input type='submit'>
</form>
"""
if option == "extend":
	print """
<form action='object/extend.py'>
Enter username <input type='text' name='username' />
<br />
Enter size to which you want to extend  <input type='number' name='size' />
<br />
Enter your ip <input type='number' name='ipaddress' />
<br />
Enter root password of that ip <input type='password' name='password' />
<br />
<input type='submit'>
</form>
"""
if option == "reduce":
	print """
<form action='staas_object/reduce.py'>
Enter username <input type='text' name='username' />
<br />
How much you want to reduce  <input type='number' name='size' />
<br />
<input type='submit'>
</form>
"""
if option == "remove":
	print """
<form action='staas_object/remove.py'>
Enter username <input type='text' name='username' />
<br />
Are you sure you want to remove ??
<br />
<input type='submit'>
</form>
"""

