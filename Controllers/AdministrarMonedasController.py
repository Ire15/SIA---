from gi.repository import Gtk

class AdministrarMonedasController:
	def __init__(self, webClient, empresa):
		gui = Gtk.Builder()
		gui.add_from_file("../GUI/AdministrarMonedas.glade")
		events = {"on_botAgregar_clicked": self.on_botAgregar_clicked,
			"on_botModificar_clicked": self.on_botModificar_clicked,
			"on_adminMonedas_delete_event": Gtk.main_quit,
			}
		gui.connect_signals(events)
		self.Window = gui.get_object("adminMonedas")
		self.Window.set_title("Administrador de Monedas")
		self.vista = gui.get_object('treeview')
		self.empresa = empresa
		self.client = webClient
		self.monedas = self.client.getMonedas(empresa)[0]
		print self.monedas
		self.listaCuentas = Gtk.ListStore(str, str, float, float)
		Temp = []
		for i in self.monedas:
			Temp.append(i)
			print Temp
			if len(Temp) == 4:
				self.listaCuentas.append([str(Temp[0]), str(Temp[1]), float(Temp[2]), float(Temp[3])])
				#self.listaCuentas.append(["Activos", "holaMundo", float(3000), float(30000)])
				Temp = []
		self.inicializarTreeView()
		
	def on_botAgregar_clicked(self, button):
		self.Window.show(False)
		startCrearMonedaController(self.cliente, self.empresa)
		self.Window.show(True)
		
	def on_botModificar_clicked(self, button):
		self.Window.show(False)
		startMonedasController(self.cliente, self.empresa)
		self.Window.show(True)
		
	def inicializarTreeView(self):		
		render = Gtk.CellRendererText()
		columna = Gtk.TreeViewColumn("Moneda",render,text=0)
		columna1 = Gtk.TreeViewColumn("Codigo",render,text=1)
		columna2 = Gtk.TreeViewColumn("Compra",render,text=2)
		columna3 = Gtk.TreeViewColumn("Venta",render,text=3)
		self.vista.set_model(self.listaCuentas)
		self.vista.append_column(columna)
		self.vista.append_column(columna1)
		self.vista.append_column(columna2)
		self.vista.append_column(columna3)
		self.vista.show()
		
def startAdministrarMonedas(webClient, empresa):
	AdministrarMonedasController(webClient, empresa)
	Gtk.main()
