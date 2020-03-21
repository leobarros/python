# -*- coding:UTF-8 -*-

# Limpando o cache do sistema (LINUX)
# Leonardo Barros - nickolback@gmail.com
# 12-09-13

import subprocess

print("-=| Limpando o cache do sistema |=-\n")

print ("Senha do administrador")

admin = "sudo i"
subprocess.call(['sync && echo 1 > /proc/sys/vm/drop_caches'])
print ("Logado como root")
