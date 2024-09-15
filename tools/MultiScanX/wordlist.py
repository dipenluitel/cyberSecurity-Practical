#!/usr/bin/env python
import os
print("::Select Your Linux Sustem::")
print("1. Termux")
print("2. Debain")
choice = input("Enter Your Linux System:")
if choice == 1:
	os.system('pkg install crunch')
if choice == 2:
	os.system('sudo apt-get install crunch')

min = input("Enter The Minimum Value:")
max = input("Enter The Maximum Value:")
output= os.system('crunch "%s" "%s" -o passwords.txt'% (min,max))  
