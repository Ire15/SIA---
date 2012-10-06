import datetime
from reportlab.pdfgen import canvas

class EstadoResultados:
	
	def generarEstadoResultados(self, Reporte, NombreEmpresa, Fecha, pListaIngresos, pListaEgresos, pListaOtrosIngresos, pListaOtrosGastos, pImpuesto, pDividendos, pUtilidadesRetenidasPeriodoAnterior):
		Reporte.setFont('Times-Bold', 18)
		Reporte.drawString(30,815,NombreEmpresa)
		Reporte.setFont('Times-Bold', 14)
		Reporte.drawString(30,800,"Estado de resultados y utilidades retenidas")
		Reporte.drawString(30,785,Fecha)
		Reporte.drawString(30,770,"_____________________________________________________________________________")
		
		Reporte.setFont('Times-BoldItalic', 14)
		Reporte.drawString(30,750, 'Ingresos Operativos')
		Reporte.setFont('Times-Roman', 10)
		linea = 730
		SumaIngresos = 0;
		for ingreso in pListaIngresos:
			Reporte.drawString(30,linea, ingreso[1])
			Reporte.drawString(200,linea, ingreso[2])
			SumaIngresos = SumaIngresos + float(ingreso[2])
			linea = linea - 12
		Reporte.setFont('Times-Bold', 10)	
		Reporte.drawString(30,linea, "Total de ingresos operativos")
		Reporte.drawString(300,linea, str(SumaIngresos))
		linea = linea-12
		
		Reporte.setFont('Times-BoldItalic', 14)
		linea = linea - 20
		Reporte.drawString(30,linea, 'Egresos Operativos')
		Reporte.setFont('Times-Roman', 10)
		linea = linea - 20
		SumaEgresos = 0
		for egreso in pListaEgresos:
			Reporte.drawString(30,linea, egreso[1])
			Reporte.drawString(200,linea, egreso[2])
			SumaEgresos = SumaEgresos + float(egreso[2])
			linea = linea - 12
		Reporte.setFont('Times-Bold', 10)	
		Reporte.drawString(30,linea, "Total de egresos operativos")
		Reporte.drawString(300,linea, str(SumaEgresos))
		linea = linea-20
		Reporte.setFont('Times-Bold', 11)
		Reporte.drawString(30,linea, "Utilidad operativa")
		UtilidadOperativa = SumaIngresos-SumaEgresos
		Reporte.drawString(300,linea, str(UtilidadOperativa))
		Reporte.setFont('Times-BoldItalic', 14)
		linea = linea - 40
		Reporte.drawString(30,linea, 'Partidas extraordinarias')
		Reporte.setFont('Times-Roman', 10)
		linea = linea - 20
		SumaOtrosIngresos = 0
		for otrosIngresos in pListaOtrosIngresos:
			Reporte.drawString(30,linea, otrosIngresos[1])
			Reporte.drawString(200,linea, otrosIngresos[2])
			SumaOtrosIngresos = SumaOtrosIngresos + float(otrosIngresos[2])
			linea = linea - 12
		SumaOtrosGastos = 0
		for otrosGastos in pListaOtrosGastos:
			Reporte.drawString(30,linea, otrosGastos[1])
			Reporte.drawString(200,linea, "-" + otrosGastos[2])
			SumaOtrosGastos = SumaOtrosGastos + float (otrosGastos[2])
			linea = linea - 12
		Reporte.setFont('Times-Bold', 10)	
		Reporte.drawString(30,linea, "Total de partidas extraordinarias")
		TotalPartidasExtraordinarias = SumaOtrosIngresos-SumaOtrosGastos
		Reporte.drawString(300,linea, str(TotalPartidasExtraordinarias))
		linea = linea-20
		
		Reporte.setFont('Times-Bold', 10)	
		Reporte.drawString(30,linea, "Utilidad antes de impuesto")
		UtilidadAntesImpuesto = UtilidadOperativa + TotalPartidasExtraordinarias
		Reporte.drawString(300,linea, str(UtilidadAntesImpuesto))
		linea = linea-12	
		
		Reporte.setFont('Times-Bold', 10)	
		Reporte.drawString(30,linea, "Impuesto de renta")
		ImpuestoRenta = (UtilidadAntesImpuesto*pImpuesto)/100
		Reporte.drawString(300,linea, str(ImpuestoRenta))
		linea = linea-12
		
		Reporte.setFont('Times-Bold', 10)	
		Reporte.drawString(30,linea, "Utilidad neta del periodo")
		UtilidadNetaPeriodo = UtilidadAntesImpuesto - ImpuestoRenta
		Reporte.drawString(300,linea, str(UtilidadNetaPeriodo))
		linea = linea-20
		
		Reporte.setFont('Times-Bold', 10)	
		Reporte.drawString(30,linea, "Utilidades retenidas del periodo anterior")
		Reporte.drawString(300,linea, str(pUtilidadesRetenidasPeriodoAnterior))
		linea = linea-12
		
		Reporte.setFont('Times-Bold', 10)	
		Reporte.drawString(30,linea, "Dividendos")
		Dividendos = (UtilidadNetaPeriodo*pDividendos)/100
		Reporte.drawString(300,linea, str(Dividendos))
		linea = linea-12
		
		Reporte.setFont('Times-Bold', 10)	
		Reporte.drawString(30,linea, "Utilidades retenidas del periodo actual")
		UtilidadesRetenidasPeriodoActual = UtilidadNetaPeriodo + pUtilidadesRetenidasPeriodoAnterior + Dividendos
		Reporte.drawString(300,linea, str(UtilidadesRetenidasPeriodoActual))
		linea = linea-12						
		
		
	
	def separarListasEstadoResultados(self, MatrizDatos, pListaIngresos, pListaEgresos, pListaOtrosIngresos, pListaOtrosGastos):
		for i in MatrizDatos:
			if i[0][0] == '4':
				pListaIngresos.extend([i])
			elif i[0][0] == '6':
				pListaEgresos.extend([i])
			elif i[0][0] == '7':
				pListaOtrosIngresos.extend([i])
			elif i[0][0] == '8':
				pListaOtrosGastos.extend([i])		
			else:
				print(' ')

def startEstadoResultados(NombreEmpresa, Matriz, pImpuestos, pDividendos, pUtilidadesRetenidasPeriodoAnterior):
	ListaIngresos = []
	ListaEgresos = []
	ListaOtrosIngresos = []
	ListaOtrosGastos = []
	
	'''Matriz = [['623456789123456', 'Gastos salario', '250000', '1'],['623456789123456', 'Gastos electricidad', '315000', '0'],
			  ['423456789123456', 'Ingresos por servicios', '25000', '1'],['423456789123456', 'Ventas', '315000', '0'],
			  ['823456789123456', 'Gastos por intereses', '250000', '1'],['723456789123456', 'Ingresos por intereses', '315000', '0']]'''
	
	EstadoResultados().separarListasEstadoResultados(Matriz, ListaIngresos, ListaEgresos, ListaOtrosIngresos, ListaOtrosGastos)

	Reporte = canvas.Canvas("EstadoResultado.pdf")
	
	Fecha = datetime.date.today()
	
	EstadoResultados().generarEstadoResultados(Reporte, NombreEmpresa, str(Fecha), ListaIngresos, ListaEgresos, ListaOtrosIngresos, ListaOtrosGastos, pImpuestos, pDividendos, pUtilidadesRetenidasPeriodoAnterior)
	Reporte.showPage()
	Reporte.save()			
