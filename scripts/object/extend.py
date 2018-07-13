#!/usr/bin/python2

import commands
import os
import cgi

print "content-type: text/html"
print

username = cgi.FormContent()['username'][0]
size = cgi.FormContent()['size'][0]
#username=raw_input("enter name :")
#size=raw_input("enter size : ")
entry="""---
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
          block: '/cloud/{0}-lv1  *(rw,no_root,squash)'
          path: '/etc/exports'
      - mount:
          path: '/object/{0}-lv1'
          src: '/dev/vgcloud/{0}-lv1'
          fstype: ext4
          state: mounted
- hosts: all
  tasks:
      - file:
          path: '/media/{0}'
          state: directory
      - mount:
          path: '/media/{0}'
          src: '192.168.43.113:/object/{0}-lv1'
          fstype: nfs
          state: mounted """.format(username,size)


f = open("extend.yml" , 'w')
f.write(entry)
f.close()
object_staas_status=commands.getstatusoutput("ansible-playbook create.yml")	
print "successful"








