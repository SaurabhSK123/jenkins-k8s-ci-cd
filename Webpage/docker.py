#!/usr/bin/python3


print("content-type: text/html \n")
print()

import cgi
import subprocess

y = cgi.FieldStorage()
cmd = y.getvalue("x")


output = subprocess.getoutput("sudo "+cmd)
print(output)
