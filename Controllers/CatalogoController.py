from gi.repository import Gtk
from AgregarCuentasController import *
from EliminarCuentaController import *
from CrearCuentaController import *

class CatalogoController:
	def __init__(self, webClient, empresa):
		gui = Gtk.Builder()
		gui.add_from_file("../GUI/Catalogo.glade")
		events = { "on_botAgregar_clicked": self.agregarCta,
			"on_botEliminar_clicked": self.eliminarCta,
			"on_Catalogo_delete_event": Gtk.main_quit,
		}
		gui.connect_signals(events)
		self.Window = gui.get_object("Catalogo")
		self.Window.set_title("Catalogo de cuentas")
		self.catalogo = gui.get_object("treeview")
		self.client = webClient
		self.empresa = empresa
		self.treestore = Gtk.TreeStore(str)
		self.cuentas = self.client.getCuentas(empresa)[0]
		#print self.cuentas
		self.inicializarTreeView();
		##CUENTAS!!!!!!!!! get CUENTAS!!!!
		##GETCUENTASNOMBRE!!!!!! recibe ESA VARA y la empresa!
		
	def getCuentasLevel(self, parent):
		cuenta = parent.split("-")
		Level = []
		Level2 = []
		temp = ""
		for i in range(len(self.cuentas)):
			cuentasChild = self.cuentas[i].split("-")
			if cuenta == cuentasChild[:len(cuenta)] and len(cuenta)+1 == len(cuentasChild):
				Level.append(cuentasChild)
			for i in Level:
				temp = "-".join(i)
				Level2.append(temp)
				temp = ""
		return Level2
		
	def getRoots(self, cuentas):
		Roots = []
		for i in cuentas:
			if len(i) == 1:
				Roots.append(i)
		return Roots
		
	def agregarCta(self, button):
		self.Window.set_visible(False)
		startCrearCuentaController(self.client, self.empresa)
		self.Window.set_visible(True)

	def eliminarCta(self, button):
		self.Window.set_visible(False)
		startEliminarCuentaController(self.client, self.empresa)
		self.Window.set_visible(True)
		
	def inicializarTreeView(self):
		parents = self.getRoots(self.cuentas)
		for parent in self.cuentas:
			parentTemp2 = parent + " " + self.client.getNombreCuenta(parent, self.empresa)
			#print self.client.getNombreCuenta(parent, self.empresa)
			Nivel = self.treestore.append(None, [parentTemp2])
		self.catalogo.set_model(self.treestore)
		tvcolumn = Gtk.TreeViewColumn('Column 0')
		self.catalogo.append_column(tvcolumn)
		cell = Gtk.CellRendererText()
		tvcolumn.pack_start(cell, True)
		tvcolumn.add_attribute(cell, 'text', 0)
		
def startCatalogoController(webClient, empresa):
	CatalogoController(webClient, empresa)
	Gtk.main()

