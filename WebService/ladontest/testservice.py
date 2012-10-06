import _mysql
import MySQLdb
import suds
import xml.etree.ElementTree as ET
import docutils.core
import datetime
import time
from hashlib import md5
from ladon.ladonizer import ladonize
from suds.xsd.doctor import Import, ImportDoctor
import datetime

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

class TestService(object):
	
	@ladonize(unicode,rtype=unicode)
	def helloWorld(self, name):
		return "hello " + name
		
	#Funcion Login
	@ladonize(unicode,unicode,unicode,rtype=bool)
	def checkLogin(self, empresa, user, password):
		db = _mysql.connect('localhost', 'root', 'sebasftw', 'SIA_DB')
		db.query("select idUsuario from Usuario inner join Empresa on Usuario.idEmpresa=Empresa.idEmpresa where Usuario.nombre = '"+user+"' and Usuario.pass = '"+password+"' and Empresa.nombre = '"+empresa+"'")
		result=db.store_result()
		if not result.fetch_row():
			db.close()
			return False
		else:
			db.close()
			return True
	#Retornar todas las cuentas
	@ladonize(unicode, rtype=[str])
	def getCuentas(self, empresa):
		db = _mysql.connect('localhost', 'root', 'sebasftw', empresa)
		db.query("select codigo from Cuenta")
		result=db.store_result()
		nombres = []
		item = result.fetch_row()
		while(item):
			nombres += item[0]
			item = result.fetch_row()
		db.close()
		return nombres
	#Funcion obtener las cuentas getCuentasNoTitulo(self, empresa)		
	@ladonize(unicode, rtype=[unicode])
	def getCuentasNoTitulo(self, empresa):
		db = _mysql.connect('localhost', 'root', 'sebasftw', empresa)
		db.query("select codigo, nombre from Cuenta where titulo = 0")
		result=db.store_result()
		nombres = []
		item = result.fetch_row()
		while(item):
			elem[0] = item[0]
			elem[1] = item[1]
			nombres += elem
			item = result.fetch_row()
		return nombres
	
	#Obtener todos los periodos contables
	@ladonize(unicode, rtype=[str])
	def getPeriodos(self, empresa):
		db = _mysql.connect('localhost', 'root', 'sebasftw', empresa)
		db.query("select idPeriodoContable, inicioContable, finContable from PeriodoContable")
		result = db.store_result()
		nombres = []
		item = result.fetch_row()
		while(item):
			nombres += item[0]
			item = result.fetch_row()
		db.close()
		return nombres
	
	#Obtener el estado de un periodo contable
	@ladonize(int, unicode, rtype=unicode)
	def getEstadoPeriodo(self, idCuenta, empresa):
		db = _mysql.connect('localhost', 'root', 'sebasftw', empresa)
		db.query("select Estado.nombre from PeriodoContable inner join Estado on PeriodoContable.idEstado = Estado.idEstado where idPeriodoContable = "+idCuenta)
		result = db.store_result()
		item = result.fetch_row()
		db.close()
		return item[0]
	
	#Obtener el nombre de una cuenta recibiendo el codigo
	@ladonize(unicode, unicode, rtype=str)
	def getNombreCuenta(self, codigo, empresa):
		db = _mysql.connect('localhost', 'root', 'sebasftw', empresa)
		db.query("select nombre from Cuenta where codigo = '"+ codigo+"'")
		result = db.store_result()
		item = result.fetch_row()
		nombres = item
		db.close()
		return item[0][0]
			
	#Retornar nombres de las empresas
	@ladonize(rtype=[str])
	def getEmpresas(self):
		db = _mysql.connect('localhost', 'root', 'sebasftw', 'SIA_DB')
		db.query("select nombre from Empresa")
		result=db.store_result()
		nombres = []
		item = result.fetch_row()
		while(item):
			nombres += item[0]
			item = result.fetch_row()
		db.close()
		return nombres

	#Obtener la cedula juridica de una empresa
	@ladonize(unicode,rtype=str)
	def getCedJuridica(self, empresa):
		db = _mysql.connect('localhost', 'root', 'sebasftw', 'SIA_DB')
		db.query("select cedula_juridica from Empresa where Empresa.nombre = '"+empresa+"'")
		result=db.store_result()
		row = result.fetch_row()
		if not row:
			db.close()
			return False
		else:
			ced = row[0]
			db.close()
			return ced[0]
			
	#Crear Usuario: crearUsuario(nombre password empresa) -> bool
	@ladonize(unicode,unicode,unicode,rtype=str)
	def crearUsuario(self, username, password, empresa):
		db = _mysql.connect('localhost', 'root', 'sebasftw', 'SIA_DB')
		db.query("select * from Usuario inner join Empresa on Usuario.idEmpresa = Empresa.idEmpresa where Usuario.nombre = '"+username+"' and Empresa.nombre='"+empresa+"'")
		result = db.store_result()
		if not result.fetch_row():
			db.query("call crearUsuario('"+username+"', '"+password+"', 'Administrador', '"+empresa+"')")
			db.query("select * from Usuario inner join Empresa on Usuario.idEmpresa = Empresa.idEmpresa where Usuario.nombre = '"+username+"' and Empresa.nombre='"+empresa+"'")
			result = db.store_result()
			if not result.fetch_row():
				db.close()
				return "Error creando"
			else:
				db.close()
				return "Creado con exito"
		else:
			db.close()
			return "Usuario ya existe"
			
	def crearUsuarioAux(self, username, password, empresa):
		db = _mysql.connect('localhost', 'root', 'sebasftw', 'SIA_DB')
		db.query("select * from Usuario inner join Empresa on Usuario.idEmpresa = Empresa.idEmpresa where Usuario.nombre = '"+username+"' and Empresa.nombre='"+empresa+"'")
		result = db.store_result()
		if not result.fetch_row():
			db.query("call crearUsuario('"+username+"', '"+password+"', 'Administrador', '"+empresa+"')")
			db.query("select * from Usuario inner join Empresa on Usuario.idEmpresa = Empresa.idEmpresa where Usuario.nombre = '"+username+"' and Empresa.nombre='"+empresa+"'")
			result = db.store_result()
			if not result.fetch_row():
				db.close()
				return False
			else:
				db.close()
				return True
		else:
			db.close()
			return False
		
	#Crear nueva empresa
	@ladonize(unicode, unicode, unicode, unicode, unicode, unicode, rtype=bool)	
	def crearEmpresa(self, empresa, cedula, logotipo, pais, tel, fax): 
		db = _mysql.connect('localhost', 'root', 'sebasftw', 'SIA_DB')
		db.query("select * from Empresa where Empresa.nombre = '"+empresa+"'")
		result = db.store_result()
		if not result.fetch_row():
			db.query("call crearEmpresa('"+empresa+"','"+cedula+"','"+logotipo+"','"+pais+"')")
			db.query("select idEmpresa from Empresa where nombre = '"+empresa+"'")
			result = db.store_result()
			row = result.fetch_row()
			if not row:
				db.close()
				return False
			else:
				idEmpresa = int(row[0][0])
				paramsTel = " ('%s', %i, %i)" %(tel, idEmpresa, 2)
				paramsFax = " ('%s', %i, %i)" %(fax, idEmpresa, 1)
				db.query("insert into Contacto (valor, idEmpresa, idTipoContacto) values"+paramsTel)
				db.query("insert into Contacto (valor, idEmpresa, idTipoContacto) values"+paramsFax)
				db.query("create database "+empresa)
				db.close()
				db = MySQLdb.connect(host='localhost',user='root',passwd='sebasftw',db=empresa)
				cursor = db.cursor()
				for line in open("scriptCuentasDB.sql"):
					cursor.execute(line)
				cursor.close()
				print "base de empresa lista..."
				cursor = db.cursor()
				for line in open("initInsert.sql"):
					cursor.execute(line)
				cursor.close()
				print "inserciones iniciales listas..."
				cursor = db.cursor()
				for line in open("scriptSPCuentas.sql"):
					cursor.execute(line)
				cursor.close()
				db.close()
				self.crearUsuarioAux('Administrador',md5("admin").hexdigest(),empresa)
				return True
		else:
			db.close()
			return False
			
	#Agregar Cuenta (verificar jerarquia, 5 niveles):agregarCuenta(codigo, nombre, nombreExtra, titulo (bool), saldo (float)) -> bool
	@ladonize(unicode, unicode, unicode, unicode, unicode, rtype=bool)
	def crearCuenta(self, codigo, nombre, nombreExtra, titulo, empresa):
		db = _mysql.connect('localhost', 'root', 'sebasftw', empresa)
		db.query("select * from Cuenta where codigo = '"+codigo+"'")
		result = db.store_result()
		if not result.fetch_row():
			codigoAnt = ""
			codigoSplit = codigo.split("-")
			for x in range(len(codigoSplit)-2):
				codigoAnt += codigoSplit[x] + "-"
			codigoAnt += codigoSplit[len(codigoSplit)-2]
			
			db.query("select * from Cuenta where codigo = '"+codigoAnt+"'")
			result = db.store_result()
			if not result.fetch_row():
				db.close()
				return False
			else:
				db.query("call crearCuenta('"+codigo+"','"+nombre+"','"+nombreExtra+"','"+titulo+"',0)")
				db.query("select * from Cuenta where codigo = '"+codigo+"'")
				if not result.fetch_row():
					db.close()
					return False
				else:
					db.close()
					return True
		else:
			db.close()
			return False

	#Retornar monedas: getMonedas()-> lista de nombres			
	@ladonize(unicode, rtype=[str])
	def getMonedas(self, empresa):
		db = _mysql.connect('localhost', 'root', 'sebasftw',empresa)
		db.query("select Moneda.nombre, Moneda.codigo, TipoCambio.relacionCompra, TipoCambio.relacionVenta from Moneda inner join TipoCambio on TipoCambio.idMoneda = Moneda.idMoneda")
		result=db.store_result()
		nombres = []
		item = result.fetch_row()
		while(item):
			nombres += item[0]
			item = result.fetch_row()
		db.close()
		return nombres
	
	#Retornar paises: getPaises()-> lista de nombres			
	@ladonize(rtype=[str])
	def getPaises(self):
		db = _mysql.connect('localhost', 'root', 'sebasftw','SIA_DB')
		db.query("select nombre from Pais")
		result=db.store_result()
		nombres = []
		item = result.fetch_row()
		while(item):
			nombres += item[0]
			item = result.fetch_row()
		db.close()
		return nombres
		
	def agregarTipoCambio(self, compra, venta, fecha, moneda, empresa):
		db = _mysql.connect('localhost', 'root', 'sebasftw',empresa)
		db.query("select * from TipoCambio innner join Moneda on TipoCambio.idMoneda = Moneda.idMoneda where Moneda.nombre = '"+moneda+"' AND fecha = '"+fecha+"')")
		result = db.store_result()
		if not result.fetch_row():
			#Si existe una moneda con la fecha actual en el tipo de cambio
			db.close()
			return False
		else:
			return True
			#Si es una primera insercion
			
	#Agregar Monedas: agregarMoneda(nombre, tipo de cambio compra:float, tipo de cambio venta:float, tipo moneda: int)-> bool
	@ladonize(unicode, unicode, unicode, unicode, unicode, unicode, rtype=bool)
	def crearMoneda(self, nombre, tipoDeCambioCompra, tipoDeCambioVenta, BCCR, tipoMoneda, empresa):
		db = _mysql.connect('localhost', 'root', 'sebasftw',empresa)
		db.query("select nombre from Moneda where nombre = '"+nombre+"'")
		result = db.store_result()
		if not result.fetch_row():
			db.query("call crearMoneda('"+nombre+"','"+BCCR+"','"+tipoMoneda+"')")
			if BCCR > 0:
				Cliente = ClienteTipoCambio()
				db.query("call crearTipoCambio ('"+Cliente.tipoCambioCompra()+"','"+Cliente.tipoCambioVenta()+"','2012-10-06','"+nombre+"')")
				db.close()
				return True
				#solicitar tipo cambio al webservice del BCCR
			else:
				db.query("call crearTipoCambio ('"+tipoDeCambioCompra+"','"+tipoDeCambioVenta+"','2012-10-06','"+nombre+"')")
				return True
				#crear tipo cambio alambrado
		else:
			return False	
	
	#Eliminar Cuenta: verificar q sea hoja en jerarquia: eliminarCuenta(codigo)-> bool
	@ladonize(unicode, unicode, rtype=bool)
	def eliminarCuenta(self, codigo, empresa):
		db = _mysql.connect('localhost', 'root', 'sebasftw',empresa)
		db.query("select nombre from Cuenta where codigo = '"+codigo+"'")
		result = db.store_result()
		if not result.fetch_row():
			db.query("delete from Cuenta where codigo = '"+codigo+"'")
			db.close()
			return True
		else:
			db.close()
			return False
	
	#Crear CuentaXMoneda
	@ladonize(unicode, unicode, unicode, rtype = bool)
	def crearCuentaXMoneda(self, cuenta, moneda, empresa):
		db = _mysql.connect('localhost', 'root', 'sebasftw',empresa)
		db.query("call crearCuentaXMoneda ('"+moneda+"','"+cuenta+"')")
		db.query("select Moneda.nombre from CuentaXMoneda inner join Moneda on CuentaXMoneda.idMoneda = Moneda.idMoneda inner join Cuenta on CuentaXMoneda.idCuenta = Cuenta.idCuenta where Cuenta.nombre = '"+cuenta+"' and Moneda.nombre = '"+moneda+"'")
		result = db.store_result()
		if result.fetch_row():
			db.close()
			return True
		else:
			db.close()
			return False
	#Eliminar Monedas: eliminarMoneda(nombre)-> bool
	@ladonize(unicode, unicode, rtype=bool)
	def eliminarMoneda(self, nombre, empresa):
		db = _mysql.connect('localhost', 'root', 'sebasftw',empresa)
		db.query("select nombre from Moneda where nombre = '"+nombre+"'")
		result = db.store_result()
		if not result.fetch_row():
			db.query("delete from Moneda where nombre = '"+nombre+"'")
			db.close()
			return True
		else:
			db.close()
			return False
					
	#Modificar Monedas:
	@ladonize(unicode, float, float, unicode, rtype=bool)
	def modificarMoneda(self, nombre, venta, compra, empresa):
		db = _mysql.connect('localhost', 'root', 'sebasftw',empresa)
		db.query("update TipoCambio inner join Moneda on TipoCambio.idMoneda = Moneda.idMoneda set relacionCompra = '"+str(compra)+"', relacionVenta = '"+str(venta)+"' where Moneda.nombre = '"+nombre+"'")
		db.query("select * from Moneda inner join TipoCambio on Moneda.idMoneda = TipoCambio.idMoneda where Moneda.nombre = '"+nombre+"' AND TipoCambio.relacionCompra = '"+str(compra)+"'")
		result = db.store_result()
		if not result.fetch_row():
			db.close()
			return False
		else:
			db.close()
			return True
			
	#Convertir monto a moneda del sistema	
	@ladonize (unicode, float, unicode, rtype = float)
	def convertirASistema(self, empresa, monto, monedaOrigen):
		db = _mysql.connect('localhost', 'root', 'sebasftw', empresa)
		db.query("select TipoCambio.relacionVenta from TipoCambio inner join Moneda on TipoCambio.idTipoCambio = Moneda.idTipoCambio where Moneda.nombre = '"+monedaOrigen+"'")
		result = db.store_result()
		row = result.fetch_row()
		if row:
			tipoCambio = double(row[0])
			db.close()
			return tipoCambio * monto
		else:
			db.close()
			return -1
		
	#Convertir monto de moneda del sistema a moneda destino
	@ladonize (unicode, float, unicode, rtype = float)
	def convertirDeSistema(self, empresa, monto, monedaDestino):
		db.query("select TipoCambio.relacionCompra from TipoCambio inner join Moneda on TipoCambio.idTipoCambio = Moneda.idTipoCambio where Moneda.nombre = '"+monedaDestino+"'")
		result = db.store_result()
		row = result.fetch_row()
		if row:
			tipoCambio = double(row[0])
			db.close()
			return tipoCambio * monto
		else:
			db.close()
			return -1
	
	#Configurar las monedas del sistema 
	@ladonize(unicode, unicode, unicode, unicode, unicode, float, float, rtype=bool)
	def configurarMonedas(self, empresa, sistema, codSistema, local, codLocal, compra, venta):
		hoy = datetime.date.today()
		fecha = hoy.strftime("%Y-%m-%e")
		db = _mysql.connect('localhost', 'root', 'sebasftw', empresa)
		db.query("call crearMoneda('%s', %i, 'Sistema', '%s')" %(sistema, 0, codSistema))
		db.query("call crearMoneda('%s', %i, 'Local', '%s')" %(local, 0, codLocal))
		db.query("select idMoneda from Moneda where nombre = '%s'" %(sistema))
		result = db.store_result()
		if result.fetch_row:
			db.query("select idMoneda from Moneda where nombre = '%s'" %(local))
			result = db.store_result()
			if result.fetch_row:
				db.query("call crearTipoCambio(1, 1, '%s', '%s')" %(fecha, sistema))
				db.query("call crearTipoCambio(%f, %f, '%s', '%s')" %(compra, venta, fecha, local))
				print "oui! tipo de cambio actualizado"
				db.close()
				return True
			else:
				db.close()
				return False
		else:
			db.close()
			return False
			
		
	
			
	#Cierre Contable 
	@ladonize (unicode, float, float, unicode, unicode, unicode, unicode, unicode, unicode, rtype= bool)
	def cierreContableLikeABoss(self, empresa, dividendos, impuesto, ctaPyG, ctaUtilidades, ctaDividendos, ctaDividendosxPagar, ctaIR, ctaIRxPagar):
		db = _mysql.connect('localhost', 'root', 'sebasftw', empresa)
		
		#Obtener el monto de los gastos
		db.query("select sum(saldo) from Cuenta where codigo like '6%' or codigo like '8%' or codigo like '5%'")
		result = db.store_result()
		row = result.fetch_row()
		montoGastos = float(row[0]) 
		
		#Obtener monto de ingresos
		db.query("select sum(saldo) from Cuenta where codigo like '5%' or codigo like '7%'")
		result = db.store_result()
		row = result.fetch_row()
		montoIngresos = float(row[0])
		
		#Calculo de utilidades
		utilidadOperativa = ingresos - gastos
		montoImpuesto = utilidadOperativa * impuesto
		utilidadNeta = utilidadOperativa - montoImpuesto
		montoDividendos = utilidadNeta * dividendos
		utilidadRetenida = utilidadNeta - montoDividendos
		db.close()
		
		#Obtencion de la fecha de hoy
		hoy=daytime.date.today()
		fechas = today.strftime("%Y-%m-%e")
		
		#Registro de asientos de impuestos y dividendos
		asiento = self.crearAsiento(empresa,fechas, fechas)
		#self.crearAsientoxCuenta(empresa, asiento, ctaIR, 1, montoImpuesto,  
		
		#asiento, cuenta, debe, montoLocal, montoSistema, montoExtranjero, moneda
		#Asientos de compras
		#Cierre de ingresos y gastos
		#Utilidades y Dividendos
		
		
		
		
		
	#Crear asiento
	@ladonize (unicode, unicode, unicode, rtype= int)
	def crearAsiento(self, empresa, fechaCont, fechaDoc):
		db = _mysql.connect('localhost', 'root', 'sebasftw', empresa)
		
		#Crear asiento
		db.query("call crearAsiento("+fechaCont+","+fechaDoc+", '','', 1)")
		db.query("select max(idAsiento) from Asiento")
		result = db.store_result()
		row = result.fetch_row()
		if row:
			db.close()
			return int(row[0])
		else:
			db.close()
			return -1
	
	#Crea el movimiento de una cuenta asociado a un asiento contable	
	@ladonize (unicode, int, unicode, int, float, float, float, unicode, rtype = int)
	def crearAsientoxCuenta(self, empresa, asiento, cuenta, debe, montoLocal, montoSistema, montoExtranjero, moneda):
		db = _mysql.connect('localhost', 'root', 'sebasftw', empresa)
		db.query("select idMoneda from Moneda where nombre = '"+moneda+"'")
		result = db.store_result()
		row = result.fetch_row()
		if row:
			db.query("select idCuenta from Cuenta where nombre = '"+moneda+"'")
			result2 = db.store_result()
			row2 = result2.fetch_row()
			if row2:
				params = "%i, %f, %f, %f, %i, %i, %i" %(debe, montoSistema, montoLocal, montoExtranjero, asiento, int(row2[0]), int(row[0]))
				db.query("call crearAsientoxCuenta("+params+")")
				db.close()
				return 1
			else:
				db.close()
				return -1
		else:
			db.close()
			return -1
			
	#Crea el movimiento de una cuenta asociado a un asiento contable	
	@ladonize (unicode, unicode, int, float, float, rtype = int)
	def actualizarSaldoCuenta(self, empresa, cuenta, debe, montoSistema, montoLocal):
		db = _mysql.connect('localhost', 'root', 'sebasftw', empresa)
		db.query("select saldoSistema, saldoLocal, codigo from Cuenta where nombre = '"+cuenta+"'")
		result = db.store_result()
		row = result.fetch_row()
		actualSistema = float(row[0])
		actualLocal = float(row[1])
		codigo = row[2]
		if codigo.startswith('1') or codigo.startswith('5') or codigo.startswith('6') or codigo.startswith('8'):
			if not debe:
				actualSistema -= montoSistema
				actualLocal -= montoLocal
			else:
				actualSistema += montoSistema
				actualLocal += montoLocal
		else:
			if not debe:
				actualSistema += montoSistema
				actualLocal += montoLocal
			else:
				actualSistema -= montoSistema
				actualLocal -= montoLoca
		consulta = "saldoSistema = %f , saldoLocal = %f, where nombre = %s" %(actualSistema, actualLocal, cuenta)
		db.query("update Cuenta set "+consulta)
		db.close()
			
	#Cierre Contable: cierreContableLikeABoss()
	#Generar reporte: generarReporteLikeABoss(tipo:int balance de comprobacion, general, estado de resultados)->(algun xml?)
	@ladonize(unicode, rtype=[str])
	def genReportes(self, empresa):
		db = _mysql.connect('localhost', 'root', 'sebasftw',empresa)
		db.query("select idCuenta, nombre, saldoSistema from Cuenta where Titulo = 0")
		result=db.store_result()
		nombres = []
		item = result.fetch_row()
		while(item):
			nombres += item[0]
			item = result.fetch_row()
		db.close()
		return nombres
		
	#Crear PeriodoContable
	
	@ladonize(unicode, unicode, unicode, unicode, unicode, unicode, rtype=bool)
	def crearPeriodoC (self, empresa, estado, anio, mes, fechaI, fechaF):	
		db = _mysql.connect('localhost','root', 'sebasftw', empresa)
		FechaInicio = str(anio)+"-"+str(mes)+"-"+str(fechaI)
		mesO = 1
		while(mesO <= 12):
			mes = int(mes)+1
			if mes >= 13 :
				mes = 0
				anio = int(anio) + 1
			else: # este se hace para los meses que pertenecen al periodo contable pero en el ano siguiente al establecido ejemplo si empezamos en mayo del 2012 debe terminar en abril del 2013
				FechaFin = str(anio)+"-"+str(mes)+"-"+str(fechaF)
				query = "call crearPeriodoContable ('"+estado+"', "+str(anio)+", "+str(mes)+", '"+FechaInicio+"', '"+FechaFin+"', '"+FechaInicio+"', '"+FechaFin+"', '"+FechaInicio+"', '"+FechaFin+"')"
				db.query(query)
				mesO += 1
				FechaInicio = FechaFin
		db.close()
		return True
	
	def generarReporte(self, reporte, empresa):
		if reporte == 1:
			generarEstadoResultados(self, empresa)
		else:
			generarBalance(self, empresa)
	
	@ladonize(unicode, rtype=bool)
	def generarBalance(self, empresa):	
		db = _mysql.connect('localhost', 'root', 'sebasftw', 'SIA_DB')
		db.query("select Cuentas.codigo, Cuenta.nombre, Cuenta.saldo, Cuenta.titulo from Cuenta order by Cuenta.codigo where Empresa.nombre = '"+empresa+"'")
		result = db.store_result()
		cuentas = []
		campos = ()
		item = result.fetch_row()
		while(item):
			campos = item
			cuentas += campos
			item = result.fetch_row()
		db.close()
		return True
	
	@ladonize(unicode, rtype=bool)
	def estadoResultados(self, empresa):	
		db = _mysql.connect('localhost', 'root', 'sebasftw', 'SIA_BB')
		db.query("select Cuenta.saldo, Cuenta.nombre, Cuenta.saldo from Cuenta order by Cuenta.codigo where Cuenta.codigo > 4 and Empresa.nombre = '"+empresa+"'")
		result = db.store_result()
		cuentas = []
		campos = ()
		item = result.fetch_row()
		while(item):
			campos = item
			cuentas += campos
			item = result.fetch_row()
		db.close()
		return cuentas
