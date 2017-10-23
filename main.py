#!/usr/bin/python2

import ctypes as t
from ctypes import cdll

lib = cdll.LoadLibrary("./lib.so")

x = 100
print "%d Add108 = %d" % (x, lib.Add108(x))
