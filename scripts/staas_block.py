#!/usr/bin/python2

import cgi 

print "content-type: text/html"
print

option = cgi.FormContent()['option'][0]
print option


if option == "create":
	print"""	
<form action='block/create.py'>
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
<form action='block/extend.py'>
Enter username <input type='text' name='username' />
<br />
Enter size to which you want to extend  <input type='number' name='size' />
<br />
Enter your ip <input type='number' name='ipaddress' />
<br />
<input type='submit'>
</form>
"""
if option == "reduce":
	print """
<form action='block/reduce.py'>
Enter username <input type='text' name='username' />
<br />
How much you want to reduce  <input type='text' name='size' />
<input type='submit'>
</form>
"""
if option == "remove":
	print """
<form action='block/remove.py'>
Enter username <input type='text' name='username' />
<br />
Are you sure you want to remove ?? <input type='text' name='size' />
<input type='submit'>
</form>
"""

if option == "snap":
	print """
<form action='block/snap.py'>
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

