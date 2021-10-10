#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet Port Scanning")
print("""1) Quick Scan
2) Service and Version Information
3) Operating System Information
""")

proccesno = raw_input("Enter Procces No: ")


if (proccesno == "1"):
	targetip = raw_input("Target IP: ")
	os.system("nmap " + targetip)
elif (proccesno == "2"):
	targetip = raw_input("Target IP: ")
	os.system("nmap -sS -sV " + targetip)
elif (proccesno == "3"):
	targetip = raw_input("Target IP: ")
	os.system("nmap -O " + targetip)
else:
	print("You made the wrong choice. Program Closing.")
