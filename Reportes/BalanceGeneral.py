from reportlab.pdfgen import canvas
import datetime

class BalanceGeneral:
	
	def generarBalanceGeneral(self, Reporte, NombreEmpresa, Fecha, pListaActivos, pListaPasivos, pListaPatrimonio, pUtilidadesRetenidasPeriodoActual):
		Reporte.setFont('Times-Bold', 18)
		Reporte.drawString(30,815,NombreEmpresa)
		Reporte.setFont('Times-Bold', 14)
		Reporte.drawString(30,800,"Balance General")
		Reporte.drawString(30,785,Fecha)
		Reporte.drawString(30,770,"_____________________________________________________________________________")
		
		Reporte.setFont('Times-BoldItalic', 14)
		Reporte.drawString(30,750, 'Activos')
		Reporte.setFont('Times-Roman', 10)
		linea = 730
		SumaActivos = 0;
		for activo in pListaActivos:
			Reporte.drawString(30,linea, activo[1])
			Reporte.drawString(200,linea, activo[2])
			SumaActivos = SumaActivos + float(activo[2])
			linea = linea - 12
		Reporte.setFont('Times-Bold', 10)	
		Reporte.drawString(30,linea, "Total de activos")
		Reporte.drawString(300,linea, str(SumaActivos))
		linea = linea-12
		
		Reporte.setFont('Times-BoldItalic', 14)
		linea = linea - 20
		Reporte.drawString(30,linea, 'Pasivos')
		Reporte.setFont('Times-Roman', 10)
		linea = linea - 20
		SumaPasivos = 0
		for pasivo in pListaPasivos:
			Reporte.drawString(30,linea, pasivo[1])
			Reporte.drawString(200,linea, pasivo[2])
			SumaPasivos = SumaPasivos + float(pasivo[2])
			linea = linea - 12
		Reporte.setFont('Times-Bold', 10)	
		Reporte.drawString(30,linea, "Total de pasivos")
		Reporte.drawString(300,linea, str(SumaPasivos))
		linea = linea-40
		Reporte.setFont('Times-BoldItalic', 14)
		Reporte.drawString(30,linea, 'Patrimonio')
		Reporte.setFont('Times-Roman', 10)
		linea = linea - 20
		SumaPatrimonio = 0
		for patrimonio in pListaPatrimonio:
			Reporte.drawString(30,linea, patrimonio[1])
			Reporte.drawString(200,linea, patrimonio[2])
			SumaPatrimonio = SumaPatrimonio + float(patrimonio[2])
			linea = linea - 12
		Reporte.setFont('Times-Bold', 10)	
		Reporte.drawString(30,linea, "Total de patrimonio")
		Reporte.drawString(300,linea, str(SumaPatrimonio))
		linea = linea-20					
		
		SumaPasivosPatrimonio = SumaPasivos + SumaPatrimonio
		Reporte.drawString(30,linea, "Total de pasivos y capital")
		Reporte.drawString(300,linea, str(SumaPasivosPatrimonio))
		
	def separarListasBalanceGeneral(self, MatrizDatos, pListaActivos, pListaPasivos, pListaPatrimonio):
		for i in MatrizDatos:
			if i[0][0] == '1':
				pListaActivos.extend([i])
			elif i[0][0] == '2':
				pListaPasivos.extend([i])
			elif i[0][0] == '3':
				pListaPatrimonio.extend([i])
			else:
				print(' ')

def startBalanceGeneral(NombreEmpresa, pUtilidadesRetenidasPeriodoActual, Matriz):
	ListaActivos = []
	ListaPasivos = []
	ListaPatrimonio = []
	
	'''Matriz = [['123456789123456', 'Bancos', '-250000', '1'],['123456789123456', 'Cuentas por cobrar', '115000', '0'],
			  ['123456789123456', 'Inversiones transitorias', '25000', '1'],['223456789123456', 'Cuentas por pagar', '315000', '0'],
			  ['323456789123456', 'Capital social', '1000000', '1'],
			  ['223456789123456', 'Documentos largo plazo', '250000', '1'],['223456789123456', 'Hipoteca', '-315000', '0']]'''
	
	BalanceGeneral().separarListasBalanceGeneral(Matriz, ListaActivos, ListaPasivos, ListaPatrimonio)

	Reporte = canvas.Canvas("BalanceGeneral.pdf")
	
	Fecha = datetime.date.today()
	
	BalanceGeneral().generarBalanceGeneral(Reporte, NombreEmpresa, str(Fecha), ListaActivos, ListaPasivos, ListaPatrimonio, pUtilidadesRetenidasPeriodoActual)
	Reporte.showPage()
	Reporte.save()				
