#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet Create a Wordlist")

mincharacter = raw_input("Enter Minimum Number of Characters: ")
maxcharacter = raw_input("Enter Maximum Number of Characters: ")
character = raw_input("Enter the Characters You Want: ")
regpath = raw_input("Registration Path: ")

os.system("crunch " + mincharacter + " " + maxcharacter + " " + character + " -o " + regpath)

print("Wordlist Successfully Created.")