#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet Wordpress Scaning")
print("""
1) Quick Scan
2) Plugin Scan
3) Theme Scan
4) Admin Username Scan
""")

proccesno = raw_input("Procces No: ")

if (proccesno == "1"):
	site = raw_input("Site Address: ")
	os.system("wpscan --url " + site)

elif (proccesno == "2"):
	site = raw_input("Site Adress: ")
	os.system("wpscan --url " + site + " --enumerate p")

elif (proccesno == "3"):
	site = raw_input("Site Adress: ")
	os.system("wpscan --url " + site + " --enumerate t")

elif (proccesno == "4"):
	site = raw_input("Site Adress: ")
	os.system("wpscan --url " + site + " --enumerate u")

else:
	print("Wrong choice. Program closing.")
