#!/usr/bin/python2

import commands
import os
import cgi

print "content-type: text/html"
print

username = cgi.FormContent()['username'][0]
size = cgi.FormContent()['size'][0]
ipaddress = cgi.FormContent()['ipaddress'][0]
password = cgi.FormContent()['password'][0]


fh = open("/webcontent/myproject",'w')
fh.write("[web]\n192.168.43.113 ansible_ssh_user=root  ansible_ssh_pass=Navi7891\n[{0}]\n{1} ansible_ssh_user=root  ansible_ssh_pass={2}".format(username,ipaddress,password))
fh.close

entry="""---
- hosts: web
  tasks:
     - lvol:
           vg: '/dev/vgcloud'
           lv: '{0}-lv2'
           snapshot: {0}-snap1
           size: '100'
     - service:
           name: tgtd
           state: started
- hosts: {0}
  tasks:
     - service:
           name: 'scsi-target-utils'
           state: present
           use: yum
     - command: 'iscsiadm --mode node --targetname {0}_block --portal 192.168.43.113:3260 --logout'
     - command: 'iscsiadm --mode discoveredb --type sendtargets --portal 192.168.43.113 --discover'
     - command: 'iscsiadm --mode node --targetname {0}_block --portal 192.168.43.113:3260 --login'""".format(username,size)

f = open("snap.yml" , 'w')
f.write(entry)
f.close()
object_staas_status=commands.getstatusoutput("ansible-playbook  snap.yml -i /webcontent/myproject")
if object_staas_status[0]==0:
	print "successful"
else:
	print "naah"
