#!/usr/bin/env python
# -*- codding: UTF-8 -*-

# Verificar o ip do mta

import subprocess

for i in range(83, 126):
	ip = str(i)
	maq_ip = "mta" + ip + ".f1.k8.com.br"
	
	subprocess.call(['host', maq_ip])
	print ""
	
