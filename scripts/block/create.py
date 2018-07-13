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
fh.write("[web]\n192.168.43.231 ansible_ssh_user=root  ansible_ssh_pass=Navi7891\n[{0}]\n{1} ansible_ssh_user=root  ansible_ssh_pass={2}".format(username,ipaddress,password))
fh.close()

entry="""
---
- hosts: web
  tasks:
     - lvol:
           vg: '/dev/vgcloud'
           lv: '{0}-lv2'
           size: '{1}'
     - package:
           name: 'iscsi-initiator-utils'
           state: present
           use: yum
      - blockinfile:
          block: '\\n<target {0}_block> \\nbacking-store /dev/vgcloud/{0}-lv2\\n</target>'
          path: '/etc/tgt/targets.conf'
     - service:
           name: 'tgtd'
           state: restarted

- hosts: {0}
  tasks:
     - package:
           name: 'scsi-target-utils'
           state: present
           use: yum
     - service:
           name: 'tgtd'
           state: restarted
     - open_iscsi:
           portal: '192.168.43.231'
           login: yes
           discover: yes
""".format(username,size)


fh = open("create.yml" , 'w')
fh.write(entry)
fh.close()

object_staas_status=commands.getstatusoutput("sudo ansible-playbook  create.yml -i /webcontent/myproject")
if object_staas_status[0]==0:
	print "disk is added to your pc...."
else:
	print "sorry....there was some problem"

