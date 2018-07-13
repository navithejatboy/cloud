#!/usr/bin/python2

import commands
import os
import cgi

print "content-type: text/html"
print

#username = cgi.FormContent()['username'][0]
#size = cgi.FormContent()['size'][0]
#ipaddress = cgi.FormContent()['ipaddress'][0]
#password = cgi.FormContent()['password'][0]
username=raw_input("enter name :")
size=raw_input("enter size : ")
ipaddress="192.168.43.228"
password="a"
f = open("/webcontent/myproject",'w')
f.write("[web]\n192.168.43.113 ansible_ssh_user=root  ansible_ssh_pass=Navi7891\n[{0}]\n{1} ansible_ssh_user=root  ansible_ssh_pass={2}".format(username,ipaddress,password))
f.close

entry="""---
- hosts: web
  tasks:
     - lvol:
           vg: '/dev/vgcloud'
           lv: '{0}-lv2'
           size: '{1}'
     - package:
           name: 'iscsi-initiator-utils'
           state: present
""".format(username,size)
f = open("create.yml" , 'w')
f.write(entry + "\n")
f.close()
f = open("/etc/tgt/targets.conf",'a')
f.write("'\n<target {0}_block> \nbacking-store /dev/vgcloud/{0}-lv2\n</target>'".format(username,size))
f.close()
entry1="""     - service:
           name: tgtd
           state: started
- hosts: {0}
  tasks:
     - service:
           name: 'iscsi-initiator-utils'
           state: present
           use: yum
     - command: 'iscsiadm --mode node --targetname {0}_block --portal 192.168.43.113:3260 --logout'
     - command: 'iscsiadm --mode discoveredb --type sendtargets --portal 192.168.43.113 --discover'
     - command: 'iscsiadm --mode node --targetname {0}_block --portal 192.168.43.113:3260 --login'""".format(username,size)



f = open("create.yml" , 'a')
f.write(entry1)
f.close()
object_staas_status=commands.getstatusoutput("sudo ansible-playbook  create.yml -i /webcontent/myproject")	
print "successful"
