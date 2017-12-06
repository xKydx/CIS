#!/usr/bin/python
# Python script to be packaged with Multiple conky files to give users a choice
# of conkyrc/conky.conf to be used as default at startup.
#
import os
import sys
from sys import argv

usrnpt = argv

prompt = ".:|"

os.system('clear')
print "Multiple conkyrc file Python installer script"# Name of Conky
print("\n")
print("\n")
print "Please choose your conky from this list. NOTE You can only install one at a time."# Name of Conky
print("""KYD_Grey_conkyrc
Siff_Grey_conkyrc
Mini-conkyrc
QNRBconkyrc """)
print("\n")
print("\n")
usrnpt = raw_input(prompt)
if 'S' in usrnpt:
	os.system("sudo cp ~/Downloads/ci-v0.2/Siff_Grey_conkyrc /etc/conky/conky.conf")# EG: sudo cp ~/Downloads/conkyrc /etc/conky/conky.conf
if 'k' in usrnpt:
	os.system("sudo cp ~/Downloads/ci-v0.2/KYD_Grey_conkyrc /etc/conky/conky.conf")# EG: sudo cp ~/Downloads/conkyrc /etc/conky/conky.conf
if 'q' in usrnpt:
	os.system("sudo cp ~/Downloads/ci-v0.2/QNRBconkyrc /etc/conky/conky.conf")# EG: sudo cp ~/Downloads/conkyrc /etc/conky/conky.conf
if 'm' in usrnpt:
	os.system("sudo cp ~/Downloads/ci-v0.2/Mini-conkyrc /etc/conky/conky.conf")# EG: sudo cp ~/Downloads/conkyrc /etc/conky/conky.conf
else:
	print ("Not Installed")
	print("Please re-run the script and try again")
print("\n")
print("\n")

## Uncomment if your installing a font with your conky.
## No need if your not.

#print ("Install font now?")
#usrnpt = raw_input(prompt)
#if 'y' in usrnpt:
#	os.system('sudo cp Font-name.ttf /etc/fonts/Font-name.ttf')#replace Name of font.
#else:
#	print ("Not Installed")
print("\n")
print("\n")
print ("Multi-conky install script complete")# Name of conky
print("\n")
print ("You can start conky by typing 'conky' in a terminal window.")
print("\n")
