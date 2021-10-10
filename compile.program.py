#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import py_compile

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet Compile Program")

comp = raw_input("\nEnter program name: ")

py_compile.compile(comp)