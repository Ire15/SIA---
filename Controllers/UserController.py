#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  UserController.py
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

import sys

from gi.repository import Gtk
sys.path.append('../ServicesClient/')
from WebClient import *

class UserController:
	def __init__(self, webClient, empresa):
		gui = Gtk.Builder()
		gui.add_from_file("../GUI/CrearUsuario.glade")
		events = {"on_botCrear_clicked": self.createUser,
			"on_CrearUsuario_delete_event": Gtk.main_quit,
			} 
		gui.connect_signals(events)
		self.Window = gui.get_object("CrearUsuario")
		self.user = gui.get_object("getUser")
		self.password = gui.get_object("getPass")
		self.Window.set_title("Crear Usuario")
		self.empresa = empresa
		self.client = WebClient()
	
	def createUser(self, button):
		user = self.user.get_text()
		password = md5(self.password.get_text()).hexdigest()
		print user, password, self.empresa
		print self.client.crearUsuario(user, password, self.empresa)
	
def startUserController(webClient, empresa):
	UserController(webClient, empresa)
	Gtk.main()
