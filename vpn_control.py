#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet VPN Control")

targetip = raw_input("Target IP: ")

os.system("ike-scan " + targetip)