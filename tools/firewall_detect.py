#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet  Firewall Detect")

site = raw_input("Site name: ")
os.system("wafw00f " + site)