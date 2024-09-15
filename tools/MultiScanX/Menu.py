#!/usr/bin/env python
import threading
from queue import Queue
import time
import socket
import requests
import os
def menu():
	print("""   
	█    ▄█    ▄     ▄       ▄      ▄███▄   █     ▄███▄   ▄█▄      ▄▄▄▄▀ █▄▄▄▄ ████▄    ▄      ▄▄▄▄▄   
	█    ██     █     █  ▀▄   █     █▀   ▀  █     █▀   ▀  █▀ ▀▄ ▀▀▀ █    █  ▄▀ █   █     █    █     ▀▄ 
	█    ██ ██   █ █   █   █ ▀      ██▄▄    █     ██▄▄    █   ▀     █    █▀▀▌  █   █ ██   █ ▄  ▀▀▀▀▄   
	███▄ ▐█ █ █  █ █   █  ▄ █       █▄   ▄▀ ███▄  █▄   ▄▀ █▄  ▄▀   █     █  █  ▀████ █ █  █  ▀▄▄▄▄▀    
		▀ ▐ █  █ █ █▄ ▄█ █   ▀▄     ▀███▀       ▀ ▀███▀   ▀███▀   ▀        █         █  █ █            
			█   ██  ▀▀▀   ▀                                               ▀          █   ██            
                                                                                                   
	""")
	print ("1. Website Header Security Checker\n")
	print ("2. Open Port Scanner\n")
	print ("3. Facebook Password Generator\n")
menu()
main_input = int(input("Input Your Choice: "))
if main_input == 1:
	import header
if main_input == 2:
	import PortScanner
if main_input == 3:
	import wordlist
else:
	menu()

	
