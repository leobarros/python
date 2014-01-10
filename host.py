#!/usr/bin/env python


import socket

dominio = raw_input("Dominio: ")


socket.gethostbyname(dominio)

print dominio
