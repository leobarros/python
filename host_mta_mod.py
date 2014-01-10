#!/usr/bin/env python
# -*- codding: UTF-8 -*-

# Verificar o ip do mta

import subprocess

smtpu = [97, 98, 99, 119]
smtpr = [87, 88, 115, 116, 125]
smtpq = [83, 85, 121, 124]
smtps = [89, 91, 92, 118]


print  "Listar MTA\n"

print "1 - SMTPU\n"
print "2 - SMTPR\n"

op_mta = raw_input("Informe o MTA: ")

while(op_mta != "0"):
	
	if(op_mta == "1"):
		print "SMTPU"
		for i in smtpu:
			ip = str(i)
			maq_ip = "mta" + ip + ".f1.k8.com.br"
			
			subprocess.call(['host', maq_ip])
			print ""
		break

