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

fh=open("/webcontent/myproject",'w')
fh.write("[web]\n192.168.43.231 ansible_ssh_user=root  ansible_ssh_pass=Navi7891\n[{0}]\n{1}           ansible_ssh_user=root  ansible_ssh_pass={2}".format(username,ipaddress,password))
fh.close()


entry="""
---
- hosts: web
  tasks:
      - lvol:
          vg: '/dev/vgcloud'
          lv: '{0}-lv1'
          size: '{1}'
      - filesystem:
         fstype: ext4
         dev: '/dev/vgcloud/{0}-lv1'
      - file:
          path: '/object/{0}-lv1'
          state: directory
      - blockinfile:
          block: '/object/{0}-lv1  *(rw,no_root_squash)'
          path: '/etc/exports'
      - mount:
          path: '/object/{0}-lv1'
          src: '/dev/vgcloud/{0}-lv1'
          fstype: ext4
          state: mounted
      - service:
          name: 'nfs'
          state: restarted
- hosts: {0}
  tasks:
      - service:
          name: 'nfs'
          state: restarted
      - file:
          path: '/media/{0}'
          state: directory
      - mount:
          path: '/media/{0}'
          src: '192.168.43.231:/object/{0}-lv1'
          fstab: /webcontent/faltu.txt
          fstype: nfs
          state: mounted""".format(username,size)


fh = open("create.yml" , 'w')
fh.write(entry)
fh.close()


#in this code there is some error this code is run manually perfect but not through browser
add_obj=commands.getstatusoutput("sudo ansible-playbook create.yml -i /webcontent/myproject")	

if add_obj[0]==0:
	print "your driver is created and attached successfully."
else:
	print "sorry please try again ....................!!!!!!!"
