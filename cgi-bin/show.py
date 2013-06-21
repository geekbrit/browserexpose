#!/usr/bin/python   

import cgi;
import subprocess

print('Content-type: text/html\r\n\r')

import cgitb
cgitb.enable()

form = cgi.FieldStorage();
window = form.getvalue('w');

def runProcess(exe):
    try:
        retval = subprocess.check_output(exe)
    except subprocess.CalledProcessError, e:
        print '<b>something went wrong ' + str(e.returncode) + e.output + '</b>'

op = runProcess(['wmctrl', '-ia', window])

print op
