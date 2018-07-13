#!/usr/bin/python2
import commands

print "content-type: text/html"
print 

print """
<script>
function d_remove(cname)
{
document.location='d_remove.py?x=' + cname;
}

function d_stop(cname)
{
document.location='d_stop.py?x=' + cname;
}

function d_start(cname)
{
document.location='d_start.py?x=' + cname;
}

</script>
"""


print "<table border='9'>"
print "<tr><th> Image name </th><th> Container name </th><th> Container IP </th><th> Status </th><th> Stop container </th><th> Start container </th><th> Remove container </th> "
count=1
for i in commands.getoutput("sudo docker ps -a").split('\n'):
	if count == 1:
		count=count+1
		print "<a href='../../caas.html'>Click Here To Add New Container</a>"
	else:
		j = i.split()
		c_status=commands.getoutput("sudo docker inspect {} | jq '.[].State.Status'".format(j[-1]))
		ipaddress=commands.getoutput("sudo docker inspect {} | jq '.[].NetworkSettings.Networks.bridge.IPAddress'".format(j[-1]))
		print "<tr> <td>" + j[1] + "</td> <td>" + j[-1] + "</td> <td>" + ipaddress + "</td> <td>" + c_status + "</td> <td> <input value=' " + j[-1] + " ' type = 'button' onclick=d_stop(this.value) />  </td> <td> <input value= ' " + j[-1] + " ' type = 'button' onclick=d_start(this.value) /> </td> <td> <input value=' " + j[-1] + " ' type = 'button' onclick=d_remove(this.value) /> </td></tr>"

print "</table>"
		
