#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  CrearMonedaController.py
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

class CrearMonedaController:
	def __init__(self, webClient, empresa):
		gui = Gtk.Builder()
		gui.add_from_file("../GUI/CrearCuenta.glade")
		events = { "on_botAceptar_clicked": self.crearMoneda,
			"on_CrearMoneda_delete_event": Gtk.main_quit,
			
		}
		gui.connect_signals(events)
		self.Window = gui.get_object("CrearMoneda")
		self.Window.set_title("Crear moneda")
		self.nombre = gui.get_object('getNombre')
		self.codigo = gui.get_object('getCodigo')
		self.tVenta = gui.get_object('getVenta')
		self.tCompra = gui.get_object('getCompra')
		self.BCCR = gui.get_object('bccr')
		self.empresa = empresa
		self.client = webClient
		
		
	def crearMonedas(self, button):
		nombre = self.nombre.get_text()
		codigo = self.codigo.get_text()
		tVenta = self.tVenta.get_text()
		tCompra = self.tCompra.get_text()
		BCCR = self.BCCR.get_active()
		a = self.client.crearMoneda(nombre, tVenta, tCompra, BCCR, "Extranjera", empresa)
	
def startCrearMonedaController(webClient, empresa):
	CrearMonedaController(webClient, empresa)
	Gtk.main()
	

