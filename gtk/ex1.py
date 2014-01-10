#!/usr/bin/env python

import pygtk

pygtk.require('2.0')

import gtk

janela = gtk.Window(gtk.WINDOW_TOPLEVEL)
botao = gtk.Button("Clique aqui...")
janela.add(botao)
janela.show_all()
gtk.main()

