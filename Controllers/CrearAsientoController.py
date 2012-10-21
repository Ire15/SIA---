#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  CrearAsientosController.py
#  
#  Copyright 2012 Andres <andres@athos>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  LISTO, fecha y lista de cuentas (tree view)

from gi.repository import Gtk
from AgregarCuentasController import *
from Error import *
import datetime

class CrearAsientoController:
	def __init__(self, webClient, empresa):
		gui = Gtk.Builder()
		gui.add_from_file("../GUI/CrearAsiento.glade")
		events = { "on_botCuenta_clicked": self.crearAsiento,
			"on_botTerminar_clicked": self.terminarAsiento,
			"on_CrearAsientos_delete_event" : Gtk.main_quit,
		}
		gui.connect_signals(events)
		self.Window = gui.get_object("CrearAsientos")
		self.Window.set_title("Crear Asiento")
		self.fecha = gui.get_object('getFecha')
		self.fechaDoc = gui.get_object('getDocumento')
		self.vista = gui.get_object('treeview')
		self.client = webClient
		self.empresa = empresa
		self.listaCuentas = []
		self.listaTreeview = Gtk.ListStore(str, float, float, float, float, float, float, str)
		self.inicializarTreeView()
		
		
	def terminarAsiento(self, button):
		fecha = self.fecha.get_text()
		fechaDoc = self.fechaDoc.get_text() 
		asiento = self.client.crearAsiento(self.empresa, fecha, fechaDoc)
		temp1 = 0
		temp2 = 0
		for i in self.listaCuentas:
			temp1 += i[1]
			temp2 += i[2]
		if temp1 != temp2:
			startErrorController("Error los saldos no cierran")
		for i in self.listaCuentas:
			if i[1] == 0.0:
				self.client.crearAsientoXCuenta(self.empresa, asiento, i[0], 0, i[2], i[4], i[6], i[7])
			else:
				self.client.crearAsientoXCuenta(self.empresa, asiento, i[0], 0, i[1], i[3], i[5], i[7])
		
	def crearAsiento(self, button):
		self.Window.set_visible(False)
		startAgregarCuentasController(self.client, self.empresa, self.listaCuentas)
		self.listaTreeview.append(self.listaCuentas[-1])
		self.vista.show()
		self.Window.set_visible(True)
	
	def inicializarTreeView(self):
		today = datetime.date.today()
		day = today.strftime("%e/%m/%Y")
		self.fechaDoc.set_text(day)
		self.fecha.set_text(day)
		
		render = Gtk.CellRendererText()
		columna = Gtk.TreeViewColumn("Cuenta",render,text=0)
		columna2 = Gtk.TreeViewColumn("Debe Local",render,text=1)
		columna3 = Gtk.TreeViewColumn("Haber Local",render,text=2)
		columna4 = Gtk.TreeViewColumn("Debe Sistema",render,text=3)
		columna5 = Gtk.TreeViewColumn("Haber Sistema",render,text=4)
		columna6 = Gtk.TreeViewColumn("Debe Extranjero",render,text=5)
		columna7 = Gtk.TreeViewColumn("Haber Extranjero",render,text=6)
		columna8 = Gtk.TreeViewColumn("Moneda",render,text=7)
		self.vista.set_model(self.listaTreeview)
		self.vista.append_column(columna)
		self.vista.append_column(columna2)
		self.vista.append_column(columna3)
		self.vista.append_column(columna4)
		self.vista.append_column(columna5)
		self.vista.append_column(columna6)
		self.vista.append_column(columna7)
		self.vista.append_column(columna8)
		self.vista.show()
		
	
def startCrearAsientoController(webClient, empresa):
	CrearAsientoController(webClient, empresa)
	Gtk.main()
	
