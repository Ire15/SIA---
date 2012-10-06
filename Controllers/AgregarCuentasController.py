#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  AgregarCuentasController.py
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
# LISTO 

from gi.repository import Gtk

class AgregarCuentasController:
	def __init__(self, webClient, empresa):
		gui = Gtk.Builder()
		gui.add_from_file("../GUI/AgregarCuentas.glade")
		events = { "on_botAceptar_clicked": self.agregarCta,
		"on_AgregarCuentas_delete_event": Gtk.main_quit,
		}
		gui.connect_signals(events)
		self.Window = gui.get_object("AgregarCuentas")
		self.Window.set_title("Agregar cuenta")
		self.monto = gui.get_object('getMonto')
		self.debe = gui.get_object("butDebe")
		self.haber = gui.get_object("butHaber")
		self.box = gui.get_object("boxCuentas")
		self.empresa = empresa
		listaCuentas = self.client.getCuentas
		for i in listaCuentas:
			self.box.append_text(i)
		self.box.set_active(0)
		self.client = webClient
		
	def agregarCta(self, button):
		cuenta = self.box.get_active_text()
		monto = self.monto.get_text()
		if self.debe.get_active():
			debeHaber = ("debe")
		elif self.haber.get_active():
			debeHaber = ("haber")
		self.client.agregarCuenta(cuenta, monto, debeHaber)
	
def startAgregarCuentasController(webClient, empresa):
	AgregarCuentasController(webClient, empresa)
	Gtk.main()



