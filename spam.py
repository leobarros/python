#!/usr/bin/env python

#-*- coding:UTF-8 -*-

import subprocess
for i in range(129,254):
	maquina = str(i)
	comando = maquina + ".32.73.187.bl.spamcop.net"
	subprocess.call(['host', comando])

