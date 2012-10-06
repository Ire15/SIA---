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
		self.listaCuentas = Gtk.ListStore(str, float, float)
		self.listaCuentas.append(["Activos", None, float(30000)])
		self.inicializarTreeView()
		
		
	def terminarAsiento(self, button):
		fecha = self.fecha.get_text()
		fechaDoc = self.fechaDoc.get_text()
		codDoc = self.codDoc.get_text()  
		listaCuentas = ('a','b','c','d','e')
		self.client.getCrearAsiento(fecha, fechaDoc, codDoc, listaCuentas)
		
	def crearAsiento(self, button):
		self.Window.set_visible(False)
		startAgregarCuentasController(self.client, self.empresa)
		self.Window.set_visible(True)
	
	def inicializarTreeView(self):
		today = datetime.date.today()
		day = today.strftime("%e/%m/%Y")
		self.fechaDoc.set_text(day)
		self.fecha.set_text(day)
		
		render = Gtk.CellRendererText()
		columna = Gtk.TreeViewColumn("Cuenta",render,text=0)
		columna2 = Gtk.TreeViewColumn("Debe",render,text=1)
		columna3 = Gtk.TreeViewColumn("Haber",render,text=2)
		self.vista.set_model(self.listaCuentas)
		self.vista.append_column(columna)
		self.vista.append_column(columna2)
		self.vista.append_column(columna3)
		self.vista.show()
		
	
def startCrearAsientoController(webClient, empresa):
	CrearAsientoController(webClient, empresa)
	Gtk.main()
	
