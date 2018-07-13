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
entry='---\n- hosts: web\n  tasks:\n      - lvol:\n          vg: "/dev/vgcloud"\n          lv: "{0}-lv1"\n          size: "{1}"\n      - filesystem:\n         fstype: ext4\n         dev: "/dev/vgcloud/{0}-lv1"\n      - file:\n          path: "/object/{0}-lv1"\n          state: directory\n      - mount:\n          path: "/object/{0}-lv1"\n          src: "/dev/vgcloud/{0}-lv1"\n          fstype: ext4\n          state: mounted\n- hosts: all\n  tasks:\n      - file:\n          path: "/media/{0}"\n          state: directory\n      - mount:\n          path: "/media/{0}"\n          src: "192.168.43.113:/object/{0}-lv1"\n          fstype: nfs\n          state: mounted '.format(username,size)


f = open("create.yml" , 'w')
f.write(entry)
f.close()
object_staas_status=commands.getstatusoutput("ansible-playbook create.yml")	
print "successful"


