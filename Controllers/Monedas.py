#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Monedas.py
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

class MonedasController:
	def __init__(self, webClient, empresa):
		gui = Gtk.Builder()
		gui.add_from_file("../GUI/Monedas.glade")
		events = { "on_button1_clicked": self.modMoneda,
			"on_button1_delete_event": Gtk.main_quit,
		}
		gui.connect_signals(events)
		self.Window = gui.get_object("ModificarMoneda")
		self.Window.set_title("Modificar Moneda")
		self.venta = gui.get_object('entry1')
		self.compra = gui.get_object('entry2')
		self.box = gui.get_object("comboboxtext1")
		self.empresa = empresa
		self.client = webClient
		listaMonedas = self.client.getMonedas(self.empresa)[0]
		for i in listaMonedas:
			self.box.append_text(i)
		self.box.set_active(0)
		
		
	def configurarMonedas(self, button):
		venta = self.venta.get_text()
		compra = self.compra.get_text()
		moneda = self.box.get_active_text()
		a = self.client.configurarMonedas(moneda,venta, compra, self.empresa)
		
		
		
	
def startMonedasController(webClient, empresa):
	MonedasController(webClient, empresa)
	Gtk.main()

