#!/usr/bin/python
# no pause.
# Final edit

import os
import sys
from sys import argv
usrnpt = argv
prompt = ".:|"
os.system('clear')
print("\n")
print "Black Ops 3 themed conky Install"
print("\n")
print("Your conky.conf file will be backedup to conky.back in the next step \n")
print("\n")
print ("Do you wish to install Black Ops 3 themed Conky file now?")
print("\n")
print("Press y to install n to skip")
usrnpt = raw_input(prompt)
if 'y' in usrnpt:
        os.system("sudo cp /etc/conky/conky.conf /etc/conky/conky.back")
        os.system("sudo cp ~/Downloads/BO3conkyrc /etc/conky/conky.conf")
else:
        print ("Not Installed")
print("\n")
print("\n")
print ("Black Ops 3 themed conky install complete")
print("\n")
print ("You can start conky by typing 'conky' in a terminal window.")
print("\n")
print("\n")
print ("Thank you for using the Blacks Ops 3 CIS.")
print("\n")
