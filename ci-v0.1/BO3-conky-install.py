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
print("Press y to install conky file or n to quit")
usrnpt = raw_input(prompt)
if 'y' in usrnpt:
    os.system('sudo apt-get install conky-all')
else:
    print ("Not Installed")
    os.system(exit)
print("\n")
print("Conky install complete.")
print("\n")
print("\n")
print "Conkyname Install"
print("\n")
print("Your conky.conf file will be backedup to conky.back \n")
print("\n")
print ("Install Conky file now?")
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
print ("Install BO3 font now?")
usrnpt = raw_input(prompt)
if 'y' in usrnpt:
    os.system('sudo cp agency-fb.ttf /etc/fonts/agency-fb.ttf')
else:
    print ("Not Installed")
print("\n")
print("\n")
print ("Conky BO3 Tweeked install script complete")
print("\n")
print ("You can start conky by typing 'conky' in a terminal window.")
print("\n")
