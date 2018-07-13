#!/usr/bin/python2

import cgi 
import commands

print "content-type: text/html"
print

print "<form action=customize_img.py>"



print """
<h2> Create your own customized image : </h2>
Select any os whose image you want to create <br>
<form action='custom.py'>
centos <input type='radio' name='os' value='centos'>
ubuntu <input type='radio' name='os' value='ubuntu'>
fedora <input type='radio' name='os' value='fedora'>
<br />
<br />
<h2>Select customizations from below options : </h2>
Install php <input type='checkbox' name='soft1' value ='php' />
<br />
Install mysql <input type='checkbox' name='soft2' value ='mysql' />
<br />
Install net-tools <input type='checkbox' name='soft3' value ='net-tools' />
<br />
Install httpd <input type='checkbox' name='soft4' value ='httpd' /> 
<br />
<br />
Enter container name <input type='text' name='conname'>
<br />
Enter the name you want to give to your image <input type='text' name='imagename'>
<br />
Enter version of the image <input type='text' name='version'>
<br />
<input type='submit'> 
</form>
"""
