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
print("Press y to install the latest version of Conky or n to skip")
usrnpt = raw_input(prompt)
if 'y' in usrnpt:
    os.system('sudo apt-get install conky-all')
else:
    print ("Not Installed")
print("\n")
print("You now have the lattest Conky version")
print("\n")
print("\n")
print "Conkyname Install"
print("\n")
print("Your conky.conf file will be backedup to conky.back \n")
print("\n")
print ("Do you wish to backup your default conky file and install Conkyname now?")
print("\n")
print("""Press y to install n to skip.You will be asked for your admin password for this step.""")
usrnpt = raw_input(prompt)
if 'y' in usrnpt:
        os.system("sudo cp /etc/conky/conky.conf /etc/conky/conky.back")
        os.system("sudo cp ~/Downloads/BO3conkyrc /etc/conky/conky.conf")
else:
        print ("Not Installed")
print("\n")
print("\n")
print ("Install Conkyname font now?")
usrnpt = raw_input(prompt)
if 'y' in usrnpt:
    os.system('sudo cp fontname.ttf /etc/fonts/fontname.ttf')
else:
    print ("Not Installed")
print("\n")
print("\n")
print ("Conkyname install script complete")
print("\n")
print ("You can start conky by typing 'conky' in a terminal window.")
print("\n")
