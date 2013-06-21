#!/usr/bin/python   
print('Content-type: text/html\r\n\r')

import re
import subprocess
import json

def runProcess(exe):
    retval = 'ok'
    try:
        retval = subprocess.check_output(exe)
    except subprocess.CalledProcessError, e:
        pass #print '<b>something went wrong ' + str(e.returncode) + e.output + '</b>'
    return retval

#runProcess(['xauth', 'merge', '/home/user/peter/.Xauthority'])

windows = []

op = runProcess(['wmctrl', '-lG'])

lines = op.split("\n")

for l in lines:
    if( l != '' ):
        words = l.split()
        title = l[l.find(words[6])+len(words[6]):]
        windows.append({'id':words[0],'desktop':words[1],'x':words[2],'y':words[3],'w':words[4],'h':words[5],'title':title})
        try:
            with open(words[0]+'.jpg'): pass
        except IOError:
            runProcess(['wmctrl','-ia',words[0]])
            runProcess(['convert','x:'+words[0], words[0]+'.jpg'])

print json.dumps( windows )