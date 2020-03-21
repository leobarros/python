#!/usr/bin/env python
#-*-coding:UTF-8-*-

import subprocess
import socket
ip = raw_input("IP: ")


subprocess.call(['host', ip])
subprocess.call(['dig', 'x', ip])
subprocess.call(['ping', '-c4', ip])

