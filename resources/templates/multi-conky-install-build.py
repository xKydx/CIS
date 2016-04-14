#!/usr/bin/python
# Python script to install multiple conky files.
#
import os
import sys
from sys import argv

usrnpt = argv

prompt = ".:|"

os.system('clear')
print "Multiple conkyrc file Python installer script"
print("\n")
print "Please choose your conky from this list"# Name of Conky
print("""KYD_Grey_conkyrc
Siff_Grey_conkyrc """)
print("\n")
print("\n")
usrnpt = raw_input(prompt)
if 'Siff' in usrnpt:
	os.system("sudo cp ~/Downloads/Siff_Grey_conkyrc /etc/conky/conky.conf")# EG: sudo cp ~/Downloads/conkyrc /etc/conky/conky.conf
if 'KYD' in usrnpt:
	os.system("sudo cp ~/Downloads/KYD_Grey_conkyrc /etc/conky/conky.conf")# EG: sudo cp ~/Downloads/conkyrc /etc/conky/conky.conf
else:
	print ("Not Installed")
	print("Please re-run the script and try again")
print("\n")
print("\n")
print("Please re-run the script and try again")

## Uncomment if your installing a font with your conky.
## No need if your not.

#print ("Install font now?")
#usrnpt = raw_input(prompt)
#if 'y' in usrnpt:
#	os.system('sudo cp Font-name.ttf /etc/fonts/Font-name.ttf')#replace Name of font.
#else:
#	print ("Not Installed")
#print("\n")
#print("\n")
print ("Multi-conky install script complete")# Name of conky
print("\n")
print ("You can start conky by typing 'conky' in a terminal window.")
print("\n")
