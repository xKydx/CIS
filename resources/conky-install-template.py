#!/usr/bin/python
# Python script to install conky files
#
import os
import sys
from sys import argv

usrnpt = argv

prompt = ".:|"

os.system('clear')
print "Name-of-Conky-to-be-installed-here"# Name of Conky
print("\n")
print("\n")
print ("Install Conky file now?")
usrnpt = raw_input(prompt)
if 'y' in usrnpt:
	os.system("sudo cp /NAME/OF/DIRECTORY /etc/conky/conky.conf")# EG: sudo cp ~/Downloads/conkyrc /etc/conky/conky.conf
else:
	print ("Not Installed")
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
#print("\n")
#print("\n")
print ("Name-Of-Conky install script complete")# Name of conky
print("\n")
print ("You can start conky by typing 'conky' in a terminal window.")
print("\n")
