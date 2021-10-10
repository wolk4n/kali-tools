#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet MAC Change")
print("""
1) MAC Address Randomization
2) Manually specifying the MAC Address
3) Returns MAC Address to Original
""")

proccesno = raw_input("İşlem No Girin: ")

if (proccesno == "1"):
	os.system("ifconfig eth0 down")
	os.system("macchanger -r eth0")
	os.system("ifconfig eth0 up")
	print("\033[92mMAC Adress Changed")


if (proccesno == "2"):
	macadress = raw_input("Enter new MAC: ")
	os.system("ifconfig eth0 down")
	os.system("macchanger --mac " + macadress + " eth0")
	os.system("ifconfig eth0 up")
	print("\033[92mMAC Adress Changed")

if (proccesno == "3"):
	os.system("ifconfig eth0 down")
	os.system("macchanger -p eth0")
	os.system("ifconfig eth0 up")
	print("\033[92mMAC Address Reverted to Original")
