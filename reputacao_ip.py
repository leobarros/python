#!/usr/bin/env python
#-*- coding:UTF-8 -*-

import subprocess
 
for i in range(129,254):
    maquina = str(i)
    comando = maquina + '.32.73.187.dnsbl.httpbl.org'
    subprocess.call(['host', comando])

