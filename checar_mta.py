#!/usr/bin/env python
# -*- codding: UTF-8 -*-

# Verificar o ip do mta

import subprocess

mta = [153, 158, 164, 168, 171, 172, 188, 198, 199]

for i in mta:
	ip = str(i)
	maq_ip = "187.73.32."+ip
	
	subprocess.call(['host', maq_ip])
	print ""
	
