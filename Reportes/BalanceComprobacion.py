from reportlab.pdfgen import canvas

class BalanceComprobacion:
	
	def generarBalanceComprobacion(self, Reporte, NombreEmpresa, Fecha, pListaActivos, pListaPasivos):
		Reporte.setFont('Times-Bold', 18)
		Reporte.drawString(30,815,NombreEmpresa)
		Reporte.setFont('Times-Bold', 14)
		Reporte.drawString(30,800,'Balance de comprobacion')
		Reporte.drawString(30,785,Fecha)
		Reporte.drawString(30,770,"_____________________________________________________________________________")
		
		Reporte.setFont('Times-Bold', 10)
		Reporte.drawString(30,750,"Cuenta")
		Reporte.drawString(200,750,"Debe")
		Reporte.drawString(300,750,"Haber")
		
		Reporte.setFont('Times-Roman', 10)
		linea = 738
		SumaDebe = 0;
		for activo in pListaActivos:
			if float(activo[2])>=0:
				Reporte.drawString(30,linea, activo[1])
				Reporte.drawString(200,linea, activo[2])
			else:
				Reporte.drawString(30,linea, activo[1])
				Reporte.drawString(300,linea, activo[2])
			SumaDebe= SumaDebe + float(activo[2])
			linea = linea - 12	
		
		SumaHaber = 0;
		for pasivo in pListaPasivos:
			if float(pasivo[2])>=0:
				Reporte.drawString(30,linea, pasivo[1])
				Reporte.drawString(300,linea, pasivo[2])
			else:
				Reporte.drawString(30,linea, pasivo[1])
				Reporte.drawString(200,linea, pasivo[2])
			SumaHaber= SumaHaber + float(pasivo[2])
			linea = linea - 12
		
		Reporte.setFont('Times-Bold', 10)
		Reporte.drawString(30,linea, "Suma de comprobacion")
		Reporte.drawString(200,linea, str(SumaDebe))
		Reporte.drawString(300,linea, str(SumaHaber))				
		
	def separarListasBalanceComprobacion(self, MatrizDatos, pListaActivos, pListaPasivos):
		for i in MatrizDatos:
			if i[0][0] == '1':
				pListaActivos.extend([i])
			else:
				pListaPasivos.extend([i])

def startBalanceComprobacion(NombreEmpresa, Matriz):
	ListaActivos = []
	ListaPasivos = []
	
	'''Matriz = [['123456789123456', 'Bancos', '-250000', '1'],['123456789123456', 'Cuentas por cobrar', '115000', '0'],
			  ['123456789123456', 'Inversiones transitorias', '25000', '1'],['223456789123456', 'Cuentas por pagar', '315000', '0'],
			  ['223456789123456', 'Documentos largo plazo', '250000', '1'],['223456789123456', 'Hipoteca', '-315000', '0']]'''
	
	BalanceComprobacion().separarListasBalanceComprobacion(Matriz, ListaActivos, ListaPasivos)

	Reporte = canvas.Canvas("BalanceComprobacion.pdf")
	
	Fecha = datetime.date.today()
	
	BalanceComprobacion().generarBalanceComprobacion(Reporte, NombreEmpresa, Fecha, ListaActivos, ListaPasivos)
	Reporte.showPage()
	Reporte.save()			
