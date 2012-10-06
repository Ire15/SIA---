#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  TipoCambioClient.py
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

import suds
from suds.xsd.doctor import Import, ImportDoctor
import xml.etree.ElementTree as ET
import docutils.core
import datetime
import time

class ClienteTipoCambio:
	def __init__(self):
		self.imp = Import('http://www.w3.org/2001/XMLSchema')
		self.imp.filter.add('http://ws.sdde.bccr.fi.cr')
		self.d = ImportDoctor(self.imp)
		self.url = "http://indicadoreseconomicos.bccr.fi.cr/indicadoreseconomicos/WebServices/wsIndicadoresEconomicos.asmx?WSDL"
		self.client = suds.client.Client(self.url, doctor=self.d)
		
	def getCurrentDate(self):
		self.today = datetime.date.today()
		self.day = self.today.strftime("%e/%m/%Y")
	
	def tipoCambioCompra(self):
		self.getCurrentDate()
		a = self.client.service.ObtenerIndicadoresEconomicosXML('317', self.day, self.day, 'IMPORTADOR AZUL adm@azul.com', 'N')
		return self.getAmount(a)
	
	def tipoCambioVenta(self):
		self.getCurrentDate()
		b = self.client.service.ObtenerIndicadoresEconomicosXML('318', self.day, self.day, 'IMPORTADOR AZUL adm@azul.com', 'N')
		return self.getAmount(b)
		
	def getAmount(self, xml):
		tempFile = open('temp.xml', 'w', 0)
		tempFile.write(xml)
		tree = ET.parse('temp.xml')
		root = tree.getroot()
		return root[0][2].text

Cliente = ClienteTipoCambio()
#print Cliente.client
print 'Tipo de Cambio Compra: ', Cliente.tipoCambioCompra()
print 'Tipo de Cambio Venta: ', Cliente.tipoCambioVenta()
