#!/usr/bin/python
import commands
import os
import cgi

username = cgi.FormContent()['username'][0]
f=open("/webcontent/myproject",'w')
f.write("[web]\n192.168.43.113 ansible_ssh_user=root  ansible_ssh_pass=Navi7891")
f.close

f=open("/etc/exports", 'w')
f.close()
entry="""---
- hosts: web
  tasks: 
      - service: 
          name: nfs
          state: restarted
      - mount:
          path: '/object/{0}-lv1'
          src: '{0}-lv1'
          state: absent
      - lvol:
          vg: '/dev/vgcloud'
          lv: '{0}-lv1'
          state: absent
          force: yes """.format(username)
f=open("remove.yml" , 'w')
f.write(entry)
f.close()
commands.getstatusoutput("sudo ansible-playbook  remove.yml ")	
print "your driver is removed successfully."

