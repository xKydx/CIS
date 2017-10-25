#!/usr/bin/python
# no pause.


import os
import sys
from sys import argv
usrnpt = argv
prompt = ".:|"
os.system('clear')
print ("Conky install script")
print("\n")
print "BO3conkyrc Install"
print("\n")
print("Your conky.conf file will be backedup to conky.back in your /etc/conky folder\n")
print("\n")
print ("Do you wish to backup your default conky file and install BO3conkyrc now?")
print("\n")
print("""Press y to install n to skip. You will be asked for your password for this step.""")
usrnpt = raw_input(prompt)
if 'y' in usrnpt:
        os.system("sudo cp /etc/conky/conky.conf /etc/conky/conky.back")
        os.system("sudo cp ~/Downloads/BO3conkyrc /etc/conky/conky.conf")
else:
        print ("BO3conkyrc Not Installed")
print("\n")
print("\n")
print ("BO3conkyrc install script complete")
print("\n")
print ("You can start conky by typing 'conky' in a terminal window.")
print("Script stop")
print("\n")
print("\n")
