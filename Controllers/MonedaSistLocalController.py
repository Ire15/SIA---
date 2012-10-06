#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  LoginWindow.py
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

class MonedaSistLocal:
	def __init__(self, webClient, empresa):
		gui = Gtk.Builder()
		gui.add_from_file("../GUI/CrearCuenta.glade")
		events = { "on_botAceptar_clicked": self.crearMoneda,
			"on_CrearCuenta_delete_event": Gtk.main_quit,
		}
		gui.connect_signals(events)
		self.Window = gui.get_object("MonedaSistLocal")
		self.Window.set_title("Seleccionar Moneda Local y del Sistema")
		self.monedaLocal = gui.get_object('getLocal')
		self.monedaSistema = gui.get_object('getSistema')
		self.tipoVenta = gui.get_object('getVenta')
		self.tipoCompra = gui.get_object('getCompra')
		self.bccr = gui.get_object('bccr')
		self.empresa = empresa
		self.client = webClient
		
		listaMonedas = self.client.getMonedas
		for i in listaMonedas[0]:
			self.box.append_text(i)
		self.box.set_active(0)
		
		
	def crearMoneda(self, button):
		local = self.monedaLocal.get_text()
		sistema = self.monedaSistema.get_text()
		venta = self.tipoVenta.get_text()
		compra = self.tipoCompra.get_text()
		bccr = self.bccr.get_active()
		if not self.client.crearMoneda(local, compra, venta, bccr, 'Local', empresa) or not self.client.crearMoneda(sistema, 1, 1, bccr, 'Sistema', empresa):
			startErrorController('Error en creacion de cuentas')
		
	
def startMonedaSistLocal(webClient, empresa):
	MonedaSistLocal(webClient, empresa)
	Gtk.main()
