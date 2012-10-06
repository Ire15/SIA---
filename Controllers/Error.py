#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ErrorController.py
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
#  

from gi.repository import Gtk

class ErrorController:
	def __init__(self, descripcion):
		gui = Gtk.Builder()
		gui.add_from_file("../GUI/Error.glade")
		events = { "on_botOK_clicked": self.ocultarMensaje,
			"on_Error_delete_event": Gtk.main_quit,
		}
		gui.connect_signals(events)
		self.Window = gui.get_object("Error")
		self.Window.set_title("Error")
		self.error = gui.get_object('error')
		self.error.set_text(descripcion)
		
	def ocultarMensaje(self, button):
		Gtk.main_quit()
		self.Window.hide()
	
def startErrorController(descripcion):
	ErrorController(descripcion)
	Gtk.main()

