#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet Vulnerability Analysis")
print("""
Welcome to Vulnerability Analysis Program.
""")

os.system("lynis audit system")