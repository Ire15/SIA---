#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  AnularAsientoController.py
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

class AnularAsientoController:
	def __init__(self, webClient, empresa):
		gui = Gtk.Builder()
		gui.add_from_file("../GUI/AnularAsiento.glade")
		events = { "on_botAnular_clicked": self.anularAsiento,
			"on_AnularAsiento_delete_event": Gtk.main_quit,
		}
		gui.connect_signals(events)
		self.Window = gui.get_object("AnularAsiento")
		self.Window.set_title("Anular Asiento")
		self.codAsiento = gui.get_object('entry1')
		self.empresa = empresa
		self.client = webClient
		
	def anularAsiento(self, button):
		codAsiento = self.codAsiento.get_text()
		self.client.getAnularAsiento(codAsiento)
	
def startAnularAsientoController(webClient, empresa):
	AnularAsientoController(webClient, empresa)
	Gtk.main()
