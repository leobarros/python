#!/usr/bin/env python
#-*- coding:UTF-8 -*-

import commands
import subprocess

<<<<<<< HEAD
<<<<<<< HEAD
def blacklist(inicio, fim):
  for ip in range(inicio, fim):
    comando = 'host ' + str(ip) + '.32.73.187.bl.spamcop.net'
    saida = commands.getoutput(comando)
  for i in saida.split('\n'):
    if '127.0.0.2' in i:
      print "Bloqueado: 187.73.32."+str(ip)

ini = input("IP inicial: ")
fim = input("IP final: ")

blacklist(ini, fim)




=======
=======
>>>>>>> 1c80d82... Criando um modulo da função blacklist
for ip in range(129, 256):

    comando = 'host ' + str(ip) + '.32.73.187.bl.spamcop.net'
    saida = commands.getoutput(comando)
    
    for i in saida.split('\n'):
        if '127.0.0.2' in i:
            print "Bloqueado: 187.73.32."+str(ip)
            
<<<<<<< HEAD
>>>>>>> 1c80d82... Criando um modulo da função blacklist
=======
>>>>>>> 1c80d82... Criando um modulo da função blacklist

