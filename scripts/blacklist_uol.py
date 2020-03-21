#!/usr/bin/env python
#-*- coding:UTF-8 -*-


import commands
#ip uol 200.98.199.78
for ip in range(35, 90):

    comando = 'host '+ str(ip) + '.199.98.200.bl.spamcop.net'
    saida = commands.getoutput(comando)
    for i in saida.split('\n'):
        if '127.0.0.2' in i:
            print "Bloqueado: 200.98.199."+str(ip)

