#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet Vuln Analysis")

targetip = raw_input("Target IP: ")

os.system("nikto -h " + targetip)