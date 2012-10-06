#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  WebClient.py
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
import suds
from hashlib import md5
from suds.xsd.doctor import Import, ImportDoctor
sys.path.append('../Reportes/')
from BalanceComprobacion import*
from EstadoResultados import*
from BalanceGeneral import*

class WebClient:
	def __init__(self):
		self.url = "http://khal-el.local:8080/TestService/soap/description"
		self.client = suds.client.Client(self.url, cache=None)
	
	##PRUEBAS:
	def helloWorld(self, a):
		return self.client.service.helloWorld(a)
	
	##SEGURIDAD:
	def checkLogin(self, enterprise, username, password):
		return self.client.service.checkLogin(enterprise, username, password)
	
	##CRUD:
	###Crear:
	def anularAsiento(self, codigo, empresa):
		return self.client.service.anularAsiento(codigo, empresa)
		
	def crearEmpresa(self, nombre, cedula, logotipo, pais, tel, fax):
		return self.client.service.crearEmpresa(nombre, cedula, logotipo, pais, tel, fax)
	
	def crearCuenta(self, codigo, nombre, nombreExtranjero, titulo, empresa):
		return self.client.service.crearCuenta(codigo, nombre, nombreExtranjero, titulo, empresa)
	
	def crearUsuario(self, username, password, empresa):
		return self.client.service.crearUsuario(username, password, empresa)
		
	def crearCuentaXMoneda(self, cuenta, moneda, empresa):
		return self.client.service.crearCuentaXMoneda(cuenta, moneda, empresa)
	
	def crearAsiento(self, empresa, fechaCont, fechaDoc):
		return self.client.service.crearAsiento(empresa, fechaCont, fechaDoc)
	
	def crearPeriodoC(self, empresa, estado, anio, mes, fechaI, fechaF):
		return self.client.service.crearPeriodoC(empresa, estado, anio, mes, fechaI, fechaF)
	
	def crearMonedas(self, nombre, tipoCambioV, tipoCambioC, bccr, tipoMoneda, empresa):
		return self.client.service.crearMoneda(nombre, tipoCambioC, tipoCambioV, bccr, tipoMoneda, empresa)
		
	def configurarMonedas(self, nombre, tipoVenta, tipoCambio, empresa):
		return self.client.service.configurarMonedas(nombre, tipoVenta, tipoCambio, empresa)
		
	def crearAsientoXCuenta(self, empresa, asiento, cuenta, debe, montoLocal, montoSistema, montoExtranjero, moneda):
		return self.client.service.crearAsientoXCuenta()
	
	##OBTIENE:
	def getEmpresas(self):
		return self.client.service.getEmpresas()
		
	def getPaises(self):
		return self.client.service.getPaises()
		
	def getCedulaJuridica(self, nombreEmpresa):
		return self.client.service.getCedJuridica(nombreEmpresa)
	
	def getCuentas(self, empresa):
		return self.client.service.getCuentas(empresa)
		
	def getNombreCuenta(self, cuenta, empresa):
		return self.client.service.getNombreCuenta(cuenta, empresa)
	
	def getMonedas(self, empresa):
		return self.client.service.getMonedas(empresa)
	
	def getCuentasNoTitulo(self, empresa):
		return self.client.service.getCuentasNoTitulo(empresa)
		
	def getPeriodos(self, empresa):
		return self.client.service.getPeriodos(empresa)
		
	def getEstadoPeriodo(self, empresa):
		return self.client.service.getEstadoPeriodo(empresa)
	
	def generarMatrizComprobacion(self, pListaDatos, pMatrizDatos):
		Temp = []
		for i in pListaDatos:
			Temp.append(i)
			if len(Temp) == 3:
				pMatrizDatos.append([str(Temp[0]), str(Temp[1]), str(Temp[2])])
				Temp = []
		return pMatrizDatos
	
	def comprobacion(self, empresa, identificador):
		MatrizDatos = []
		ListaDatos = self.client.service.genReportes(empresa)[0]
		self.generarMatrizComprobacion(ListaDatos, MatrizDatos)
		
		if identificador == 1:
			startBalanceComprobacion(empresa, MatrizDatos)
		elif identificador ==2:
			startEstadoResultados(empresa, MatrizDatos,0,0,0)
		else:
			startBalanceGeneral(empresa, 0, MatrizDatos)
			
		
		
	def getMonedasCuenta(self, cuenta, empresa):
		return self.client.service.getMonedasCuenta(cuenta, empresa)
		
	##ELIMINAR
	#def eliminarCuenta(self, codigo, empresa):
		
	#def eliminarMoneda(self, nombre, empresa):
		
