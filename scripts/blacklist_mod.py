#!/usr/bin/env python
#-*- coding:UTF-8 -*-

import commands
import subprocess

for ip in range(129, 256):
    comando = 'host ' + str(ip) + '.32.73.187.bl.spamcop.net'
    saida = commands.getoutput(comando)

    for i in saida.split('\n'):
        if '127.0.0.2' in i:
            block = '187.73.32.'+str(ip)
            print "Bloqueado: " + block
            print subprocess.call(['host', block])
            print 'http://www.spamcop.net/w3m?action=checkblock&ip=187.73.32.'+str(ip)
