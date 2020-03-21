#!/usr/bin/env python
# Leonardo Barros
# 3-12-13

import subprocess

server = raw_input("Servidor: ")
subprocess.call(["ssh", server, 'su'])
subprocess.call(['df', '-h'])


