import wx
import wx.grid

class CategoryPage(wx.Panel):
    def __init__(self, parent):
        super(CategoryPage, self).__init__(parent)
        self.SetBackgroundColour(wx.Colour(235, 235, 235))
        
        # 1. Creación de la interfaz
        
        # 1.1 Panel superior con resumen y botón
        self._create_top_panel()

        # 1.2 Panel inferior con lista de proveedores
        self._create_bottom_panel()
        
        # 2. Configuración del layout principal
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(self.top_sizer, 0, wx.EXPAND | wx.ALL, 5)
        main_sizer.Add(self.bottom_sizer, 1, wx.EXPAND | wx.ALL, 5)
        
        self.SetSizer(main_sizer)
        self.Layout()
        
        # 3. Cargar datos iniciales
        self.load_data()

    #----------------------------------------------------------------------
    # Métodos de creación de la interfaz
    #----------------------------------------------------------------------
    def _create_top_panel(self):
        """ Panel superior con el contador y el botón."""
        top_box = wx.StaticBox(self, label="Resumen de Categorías")
        self.top_sizer = wx.StaticBoxSizer(top_box, wx.VERTICAL)
        top_panel = wx.Panel(top_box, style=wx.BORDER_SUNKEN)
        top_panel.SetBackgroundColour(wx.Colour(255, 255, 255))
        top_content_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Contador de categorías
        count_sizer = wx.BoxSizer(wx.VERTICAL)
        count_title = wx.StaticText(top_panel, label="Total de Categorías")
        count_title.SetFont(wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        
        self.category_count_label = wx.StaticText(top_panel, label="0", style=wx.ALIGN_CENTER)
        self.category_count_label.SetFont(wx.Font(32, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        self.category_count_label.SetForegroundColour(wx.Colour(255, 185, 0))
        
        count_sizer.Add(count_title, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        count_sizer.Add(self.category_count_label, 1, wx.ALIGN_CENTER)
        
        # Botón de registro
        self.register_btn = wx.Button(top_panel, label="Registrar Nueva Categoría")
        self.register_btn.SetFont(wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        self.register_btn.SetBackgroundColour(wx.Colour(52, 152, 219))
        self.register_btn.SetForegroundColour(wx.WHITE)
        
        top_content_sizer.Add(count_sizer, 1, wx.EXPAND | wx.ALL, 10)
        top_content_sizer.AddStretchSpacer()
        top_content_sizer.Add(self.register_btn, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 20)

        top_panel.SetSizer(top_content_sizer)
        self.top_sizer.Add(top_panel, 1, wx.EXPAND, 0)

    def _create_bottom_panel(self):
        """ Panel inferior con la lista de proveedores."""
        bottom_box = wx.StaticBox(self, label="Proveedores por Categoría")
        self.bottom_sizer = wx.StaticBoxSizer(bottom_box, wx.VERTICAL)

        list_panel = wx.Panel(bottom_box, style=wx.BORDER_SUNKEN)
        list_panel.SetBackgroundColour(wx.Colour(255, 255, 255))
        list_sizer = wx.BoxSizer(wx.VERTICAL)
        
        self.list_ctrl_suppliers = wx.ListCtrl(list_panel, style=wx.LC_HRULES | wx.LC_REPORT | wx.LC_VRULES)
        self.list_ctrl_suppliers.AppendColumn("Proveedor", width=200)
        self.list_ctrl_suppliers.AppendColumn("Categoría", width=150)
        self.list_ctrl_suppliers.AppendColumn("Contacto", width=200)
        
        self.no_suppliers_label = wx.StaticText(list_panel, label="No hay proveedores registrados", style=wx.ALIGN_CENTER)
        self.no_suppliers_label.Hide() 
        
        list_sizer.Add(self.list_ctrl_suppliers, 1, wx.EXPAND | wx.ALL, 5)
        list_sizer.Add(self.no_suppliers_label, 1, wx.ALIGN_CENTER, 5)
        list_panel.SetSizer(list_sizer)

        self.bottom_sizer.Add(list_panel, 1, wx.EXPAND | wx.ALL, 5)

    #----------------------------------------------------------------------
    # Métodos de manejo de datos
    #----------------------------------------------------------------------
    def load_data(self):
        """Simula la carga de datos y actualiza las tablas y el contador."""
        suppliers_data = [
            ("Proveedor A", "Electrónica", "contacto@proveedora.com"),
            ("Proveedor B", "Hogar", "info@proveedorb.es"),
            ("Proveedor C", "Alimentos", "ventas@proveedorc.net")
        ]
        
        self._load_suppliers(suppliers_data)
        
        # Actualiza el contador de categorías
        categories = set([s[1] for s in suppliers_data])
        self.category_count_label.SetLabel(str(len(categories)))
    
    def _load_suppliers(self, data):
        """Carga y muestra los datos de los proveedores en el ListCtrl."""
        self.list_ctrl_suppliers.DeleteAllItems()
        if not data:
            self.list_ctrl_suppliers.Hide()
            self.no_suppliers_label.Show()
        else:
            self.no_suppliers_label.Hide()
            self.list_ctrl_suppliers.Show()
            for row in data:
                index = self.list_ctrl_suppliers.InsertItem(self.list_ctrl_suppliers.GetItemCount(), str(row[0]))
                self.list_ctrl_suppliers.SetItem(index, 1, str(row[1]))
                self.list_ctrl_suppliers.SetItem(index, 2, str(row[2]))
        self.Layout()