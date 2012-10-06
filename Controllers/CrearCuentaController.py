#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  CrearCuentaController.py
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
#  LISTO

from gi.repository import Gtk
from Error import *

class CrearCuentaController:
	def __init__(self, webClient, empresa):
		gui = Gtk.Builder()
		gui.add_from_file("../GUI/CrearCuenta.glade")
		events = { "on_botCrear_clicked": self.crearCta,
			"on_CrearCuenta_delete_event": Gtk.main_quit,
			"on_botAgregar_clicked": self.agregarMoneda
		}
		gui.connect_signals(events)
		self.Window = gui.get_object("CrearCuenta")
		self.Window.set_title("Crear cuenta")
		self.nombre = gui.get_object('getNombre')
		self.codigo = gui.get_object('getCodigo')
		self.nombreExtranjero = gui.get_object('getNombreExtranjero')
		self.vista = gui.get_object('treeview')
		self.moneda = gui.get_object('getMoneda')
		self.titulo = gui.get_object('getTitulo')
		self.empresa = empresa
		self.client = webClient
		self.monedasAsociadas = Gtk.ListStore(str)
		self.render=Gtk.CellRendererText()
		self.columna1=Gtk.TreeViewColumn("Nombre",self.render,text=0)
		self.vista.append_column(self.columna1)
		listaMonedas = self.client.getMonedas(self.empresa)[0]
		
		Temp = []
		for i in listaMonedas:
			Temp.append(i)
			if len(Temp) == 4:
				self.moneda.append_text(Temp[0])
				Temp = []
		self.moneda.set_active(0)
		
		
	def crearCta(self, button):
		nombre = self.nombre.get_text()
		codigo = self.codigo.get_text()
		nombreExtranjero = self.nombreExtranjero.get_text()
		titulo = self.titulo.get_active()
		codigoAux = codigo.split("-")
		nombreMoneda = self.moneda.get_active_text()
		if(len(codigoAux) > 5 or len(codigoAux) < 2):
			startErrorController("La cuenta no puede tener mas de 5 niveles o menos de 2")
		self.client.crearCuenta(codigo, nombre, nombreExtranjero, titulo, self.empresa)
		for i in self.monedasAsociadas:
			self.client.crearCuentaXMoneda(nombre, i, self.empresa)
		
		
		
	def agregarMoneda(self, button):
		moneda = self.moneda.get_active_text()
		self.monedasAsociadas.append([moneda])
		self.vista.set_model(self.monedasAsociadas)
		self.vista.show()
	
def startCrearCuentaController(webClient, empresa):
	CrearCuentaController(webClient, empresa)
	Gtk.main()
	
