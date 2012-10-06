#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  EnterpriseController.py
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
from PIL import Image

class EnterpriseController:
	def __init__(self, webClient):
		gui = Gtk.Builder()
		gui.add_from_file("../GUI/CrearEmpresa.glade")
		events = { "on_botCrear_clicked": self.crearEmpresa,
			"on_CrearEmpresa_delete_event": Gtk.main_quit,
		}
		gui.connect_signals(events)
		self.Window = gui.get_object("CrearEmpresa")
		self.Window.set_title("Crear Empresa")
		self.empresa = gui.get_object('getEnterprise')
		self.codigo = gui.get_object('getID')
		self.tel = gui.get_object('getPhone')
		self.fax = gui.get_object('getFax')
		self.logo = gui.get_object('getLogo')
		self.pais = gui.get_object('getPais')
		self.sistema = gui.get_object('getSistema')
		self.codSistema = gui.get_object('getCodigoS')
		self.local = gui.get_object('getLocal')
		self.codLocal = gui.get_object('getCodigoL')
		self.compra = gui.get_object('getCompra')
		self.venta = gui.get_object('getVenta')
		self.client = webClient
		listaPaises = self.client.getPaises()
		
		for i in listaPaises[0]:
			self.pais.append_text(i)
		self.pais.set_active(0)
		
	def is_jpg(self, filename):
		try:
			i=Image.open(filename)
			if i.format =='JPEG' or i.format =='PNG' or i.format =='JPG':
				return True
		except IOError:
			return False
		
	def crearEmpresa(self, button):
		empresa = self.empresa.get_text()
		cedula = self.codigo.get_text()
		tel = self.tel.get_text()
		fax = self.fax.get_text()
		pais = self.pais.get_active_text()
		logo = self.logo.get_filename()
		monedaSistema = self.sistema.get_text()
		codS = self.codSistema.get_text()
		monedaLocal = self.local.get_text()
		codL = self.codLocal.get_text()
		tipoCompra = float(self.compra.get_text())
		tipoVenta = float(self.venta.get_text())
		if self.is_jpg(logo):
			if(self.client.crearEmpresa(empresa, cedula, logo, pais, tel, fax)):
				if(self.client.configurarMonedas(empresa, monedaSistema, codS, monedaLocal, codL, tipoCompra, tipoVenta)):
					Gtk.main_quit()
					self.Window.hide()
				else:
					startErrorController('Error en el procesamiento de las monedas')
			else:
				startErrorController('No se pudo crear la empresa')
		else:
			startErrorController('El archivo seleccionado para el logo no es una imagen')
			

def startEnterpriseController(webClient):
	EnterpriseController(webClient)
	Gtk.main()
	
	
