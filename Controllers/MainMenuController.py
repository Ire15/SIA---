#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  MainMenu.py
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
from PeriodoController import *
from ReportesController import *
from CrearAsientoController import *
from VerAsientosController import *
from CatalogoController import *
from CrearAsientoController import *
from UserController import *
from AdministrarMonedasController import *

class MainMenuController:
	def __init__(self, webClient, empresa, user):
		gui = Gtk.Builder()
		gui.add_from_file("../GUI/MainMenu.glade")
		events = { "on_botPeriodo_clicked": self.initPeriodoController,
			"on_botCrearUsuario_clicked": self.initUserController,
			"on_botReportes_clicked": self.initReportesController,
			"on_botVerAsientos_clicked": self.initVerAsientosController,
			"on_botCrearAsientos_clicked": self.initCrearAsientosController,
			"on_botCierre_clicked": self.initCierreController,
			"on_botAdminMonedas_clicked": self.initAdminMonedasController,
			"on_botCatalogo_clicked": self.initCatalogoController,
			"on_MainMenu_delete_event": Gtk.main_quit,
		}
		gui.connect_signals(events)
		self.Window = gui.get_object("MainMenu")
		self.Window.set_title("Menu Principal")
		self.client = webClient
		
		self.nombrelabel = gui.get_object("labEmpresa")
		self.userlabel = gui.get_object("labUsername")
		self.cedJuridicalabel = gui.get_object("labInfoEmpresa")
		self.empresa = empresa
		self.userlabel.set_text(user)
		self.nombrelabel.set_text(empresa)
		cedula = self.client.getCedulaJuridica(empresa)
		self.cedJuridicalabel.set_text(cedula)
		
	def initPeriodoController(self, button):
		self.Window.set_visible(False)
		startPeriodoController(self.client, self.empresa)
		self.Window.set_visible(True)
	
	def initReportesController(self, button):
		self.Window.set_visible(False)
		startReportesController(self.client, self.empresa)
		self.Window.set_visible(True)
	
	def initVerAsientosController(self, button):
		self.Window.set_visible(False)
		startVerAsientosController(self.client, self.empresa)
		self.Window.set_visible(True)

	def initCrearAsientosController(self, button):
		self.Window.set_visible(False)
		startCrearAsientosController(self.client, self.empresa)
		self.Window.set_visible(True)
	
	def initCrearAsientosController(self, button):
		self.Window.set_visible(False)
		startCrearAsientoController(self.client, self.empresa)
		self.Window.set_visible(True)
	
	def initCierreController(self, button):
		print("Not Implemented yet...")
	
	def initAdminMonedasController(self, button):
		self.Window.set_visible(False)
		startAdministrarMonedas(self.client, self.empresa)
		self.Window.set_visible(True)
	
	def initCatalogoController(self, button):
		self.Window.set_visible(False)
		startCatalogoController(self.client, self.empresa)
		self.Window.set_visible(True)
	
	def initUserController(self, button):
		self.Window.set_visible(False)
		startUserController(self.client, self.empresa)
		self.Window.set_visible(True)


def startMainMenuController(webClient, empresa, user):
	MainMenuController(webClient, empresa, user)
	Gtk.main()
