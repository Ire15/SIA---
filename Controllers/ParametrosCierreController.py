#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ParametrosCierreController.py
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

class ParametrosCierreController:
	def __init__(self, webClient, empresa):
		gui = Gtk.Builder()
		gui.add_from_file("../GUI/ParametrosCierre.glade")
		events = { "on_botAceptar_clicked": self.aceptarCierre,
			"on_Parametros_delete_event": Gtk.main_quit,
		}
		gui.connect_signals(events)
		self.Window = gui.get_object("Parametros")
		self.Window.set_title("Parametros de Cierre")
		self.dividendos = gui.get_object("getDividendos")
		self.impuestos = gui.get_object("getImpuestos")
		self.perdidasganancias = gui.get_object("getPyG")
		self.utilidades = gui.get_object("getUR");
		self.dividendos = gui.get_object("getDiv");
		self.dividendosxPagar = gui.get_object("getCDxP")
		self.impuestoRenta = gui.get_object("getIdR")
		self.impuestoPagar = gui.get_object("getCIxP")
		self.client = webClient
		self.empresa = empresa
		
	def aceptarCierre(self, button):
		print self.codCuenta.get_text()
			
def startParametrosCierreController(webClient, empresa):
	EliminarCuentaController(webClient, empresa)
	Gtk.main()
