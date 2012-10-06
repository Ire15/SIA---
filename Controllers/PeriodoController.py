#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  PeriodoController.py
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
#   LISTO

from gi.repository import Gtk

class PeriodoController:
	def __init__(self, webClient, empresa):
		gui = Gtk.Builder()
		gui.add_from_file("../GUI/PeriodoWindow.glade")
		events = { "on_botEstablecer_clicked": self.establecer,
			"on_botCambEstado_clicked": self.cambiarEstado,
			"on_startMonth_changed": self.selMesInicio,
			"on_endMonth_changed": self.selMesFinal,
			"on_PeriodoWindow_delete_event": Gtk.main_quit,
			"on_comboboxtext1_changed": self.setEstado
		}
		gui.connect_signals(events)
		self.Window = gui.get_object("PeriodoWindow")
		self.Window.set_title("Periodo Contable")
		self.box1 = gui.get_object("startMonth")
		self.box2 = gui.get_object("startDay")
		self.box3 = gui.get_object("endMonth")
		self.box4 = gui.get_object("endDay")
		self.box5 = gui.get_object("comboboxtext1")
		self.abierto = gui.get_object("radAbierto")
		self.cerrado = gui.get_object("radCerrado")
		self.otro = gui.get_object("radOtro")
		self.listaPeriodos = []
		self.client = webClient
		self.empresa = empresa
		self.popularBox()
		
		
	def selMesInicio(self, entry):
		mesInicio = self.box1.get_active_text()
		for i in range(31):
			self.box2.remove(0)
		if mesInicio == '2':
			for i in range (1,30):
				self.box2.append_text(str(i))
			self.box2.set_active(0)
		elif mesInicio == '4' or mesInicio == '6' or mesInicio == '9' or mesInicio == '11':
			for i in range (1,31):
				self.box2.append_text(str(i))
			self.box2.set_active(0)
		else:
			for i in range (1,32):
				self.box2.append_text(str(i))
			self.box2.set_active(0)
	
	def selMesFinal(self, entry):
		mesFinal = self.box3.get_active_text()
		if mesFinal == '2':
			for i in range (1,29):
				self.box4.append_text(str(i))
			self.box4.set_active(0)
		elif mesFinal == 4 or mesFinal == 6 or mesFinal == 9 or mesFinal == 11:
			for i in range (1,30):
				self.box4.append_text(str(i))
			self.box4.set_active(0)
		else:
			for i in range (1,31):
				self.box4.append_text(str(i))
			self.box4.set_active(0)
			
			
	def establecer(self, button):
		diaInicio = self.box2.get_active_text()
		diaFinal = self.box4.get_active_text()
		mesInicio = self.box1.get_active_text()
		mesFinal = self.box3.get_active_text()
		self.client.crearPeriodoC(self.empresa, "Abierto", 2012, mesInicio, diaInicio, diaFinal)
	
	
	def cambiarEstado(self, button):
		mes = self.box5.get_active_text()
		if self.abierto.get_active():
			estado = ("abierto")
		elif self.cerrado.get_active():
			estado = ("cerrado")
		elif self.otro.get_active():
			estado = ("otro")
		self.client.cambiarEstado(mes, estado)
		
	def popularBox(self):	
		if(self.listaPeriodos):
			for i in self.listaPeriodos[0]:
				self.box5.remove(0)
		self.listaPeriodos = self.client.getPeriodos(self.empresa)
		if(self.listaPeriodos):
			group = 0
			opcion = ""
			for i in self.listaPeriodos[0]:
				if group < 2:
					opcion = opcion+" "+i
					group = group + 1
					print(opcion)
				else:
					self.box5.append_text(opcion+" "+i)
					group = 0;
					opcion = ""
			self.box5.set_active(0)
			
	def setEstado(self):
		estado = self.client.getEstadoPeriodo(self.empresa)
		if estado == "Abierto":
			self.radAbierto.set_active()
		if estado == "Cerrado":
			self.radCerrado.set_active()
		else:
			self.radOtro.set_active()

def startPeriodoController(webClient, empresa):
	PeriodoController(webClient, empresa)
	Gtk.main()
