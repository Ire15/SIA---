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

import sys

from gi.repository import Gtk
from MainMenuController import *
from EnterpriseController import *
sys.path.append('../ServicesClient/')
from WebClient import *
from Error import *

class LoginController:
	def __init__(self):
		gui = Gtk.Builder()
		gui.add_from_file("../GUI/LoginScreen.glade")
		events = {"on_botIniciar_clicked": self.logIn,
			"on_botCrear_clicked": self.createEnterprise,
			"on_LoginScreen_delete_event": Gtk.main_quit,
			} 
		gui.connect_signals(events)
		self.Window = gui.get_object("LoginScreen")
		self.empresa = gui.get_object("getEmpresa")
		self.user = gui.get_object("getUser")
		self.password = gui.get_object("getPass")
		self.Window.set_title("Login")
		self.client = WebClient()
		self.listaEmpresas = self.client.getEmpresas()
		
		if(self.listaEmpresas):
			for i in self.listaEmpresas[0]:
				self.empresa.append_text(i)
			self.empresa.set_active(0)
	
	def logIn(self, button):
		user = self.user.get_text()
		password = md5(self.password.get_text()).hexdigest()
		empresa = self.empresa.get_active_text()
		if(user != '' and password != '' and empresa != '' and self.client.checkLogin(empresa, user, password)):
			self.Window.set_visible(False)
			startMainMenuController(self.client, empresa, user)
			self.Window.set_visible(True)
		else:
			startErrorController('Error en Inicio de Session')
			
	def createEnterprise(self, button):
		self.Window.set_visible(False)
		
		startEnterpriseController(self.client)
		
		if(self.listaEmpresas):
			for i in self.listaEmpresas[0]:
				self.empresa.remove(0)
			
		self.listaEmpresas = self.client.getEmpresas()
		
		if(self.listaEmpresas):
			for i in self.listaEmpresas[0]:
				self.empresa.append_text(i)
			self.empresa.set_active(0)
			
		self.empresa.set_active(0)
		self.Window.set_visible(True)
	
def startLogin():
	LoginController()
	Gtk.main()

startLogin()
