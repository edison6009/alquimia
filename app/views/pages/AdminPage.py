import wx
import wx.grid

class AdminPage(wx.Panel):
    def __init__(self, parent):
        super(AdminPage, self).__init__(parent)
        self.SetBackgroundColour(wx.Colour(235, 235, 235))
        
        # 1. Creación de la interfaz
        
        # 1.1 Panel de administración de productos
        self._create_product_admin_panel()

        # 1.2 Sección inferior con tablas de datos
        self._create_data_tables_panel()
        
        # 2. Configuración del layout
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(self.product_admin_sizer, 0, wx.EXPAND | wx.ALL, 5)
        main_sizer.Add(self.data_tables_sizer, 1, wx.EXPAND | wx.ALL, 5)
        
        self.SetSizer(main_sizer)
        self.Layout()

        # 3. Cargar datos iniciales
        self.load_data()

    #----------------------------------------------------------------------
    # Métodos de creación de la interfaz
    #----------------------------------------------------------------------
    def _create_product_admin_panel(self):
        # Crea el panel para la entrada de datos de productos.
        self.product_admin_box = wx.StaticBox(self, wx.ID_ANY, "Administración de Productos")
        self.product_admin_sizer = wx.StaticBoxSizer(self.product_admin_box, wx.VERTICAL)
        
        top_panel = wx.Panel(self.product_admin_box, style=wx.BORDER_SUNKEN)
        top_panel.SetBackgroundColour(wx.Colour(255, 255, 255))
        
        # Grid de campos de entrada
        grid_input = wx.FlexGridSizer(2, 4, 10, 10)
        grid_input.Add(wx.StaticText(top_panel, label="Nombre:"), 0, wx.ALIGN_CENTER_VERTICAL)
        self.product_name_ctrl = wx.TextCtrl(top_panel)
        grid_input.Add(self.product_name_ctrl, 0, wx.EXPAND)
        grid_input.Add(wx.StaticText(top_panel, label="Código:"), 0, wx.ALIGN_CENTER_VERTICAL)
        self.product_code_ctrl = wx.TextCtrl(top_panel)
        grid_input.Add(self.product_code_ctrl, 0, wx.EXPAND)
        grid_input.Add(wx.StaticText(top_panel, label="Precio:"), 0, wx.ALIGN_CENTER_VERTICAL)
        self.product_price_ctrl = wx.TextCtrl(top_panel)
        grid_input.Add(self.product_price_ctrl, 0, wx.EXPAND)
        grid_input.Add(wx.StaticText(top_panel, label="Categoría:"), 0, wx.ALIGN_CENTER_VERTICAL)
        self.product_category_ctrl = wx.TextCtrl(top_panel)
        grid_input.Add(self.product_category_ctrl, 0, wx.EXPAND)

        # Botones de acción
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.save_btn = wx.Button(top_panel, label="Guardar")
        self.delete_btn = wx.Button(top_panel, label="Eliminar")
        self.edit_btn = wx.Button(top_panel, label="Editar")
        
        for btn in [self.save_btn, self.delete_btn, self.edit_btn]:
            btn.SetBackgroundColour(wx.Colour(52, 152, 219))
            btn.SetForegroundColour(wx.WHITE)
            button_sizer.Add(btn, 0, wx.ALL, 5)
        
        top_content_sizer = wx.BoxSizer(wx.VERTICAL)
        top_content_sizer.Add(grid_input, 1, wx.EXPAND | wx.ALL, 10)
        top_content_sizer.Add(button_sizer, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        top_panel.SetSizer(top_content_sizer)
        
        self.product_admin_sizer.Add(top_panel, 1, wx.EXPAND)

    def _create_data_tables_panel(self):
        # Crea el panel que contiene las tablas de inventario y ventas.
        self.data_tables_box = wx.StaticBox(self, wx.ID_ANY, "Inventario y Resumen")
        self.data_tables_sizer = wx.StaticBoxSizer(self.data_tables_box, wx.HORIZONTAL)

        # Panel de inventario de productos
        list_panel = wx.Panel(self.data_tables_box, style=wx.BORDER_SUNKEN)
        list_panel.SetBackgroundColour(wx.Colour(255, 255, 255))
        list_sizer = wx.BoxSizer(wx.VERTICAL)
        list_sizer.Add(wx.StaticText(list_panel, label="Inventario de Productos"), 0, wx.ALIGN_CENTER | wx.TOP, 5)
        self.list_ctrl_1 = wx.ListCtrl(list_panel, style=wx.LC_HRULES | wx.LC_REPORT | wx.LC_VRULES)
        self.list_ctrl_1.AppendColumn("Nombre", width=150)
        self.list_ctrl_1.AppendColumn("Cantidad", width=80)
        self.list_ctrl_1.AppendColumn("Código", width=100)
        self.no_products_label = wx.StaticText(list_panel, label="No hay productos registrados", style=wx.ALIGN_CENTER)
        self.no_products_label.Hide() 
        list_sizer.Add(self.list_ctrl_1, 1, wx.EXPAND | wx.ALL, 5)
        list_sizer.Add(self.no_products_label, 1, wx.ALIGN_CENTER, 5)
        
        # Barra de progreso
        gauge_sizer = wx.BoxSizer(wx.HORIZONTAL)
        gauge_sizer.Add(wx.StaticText(list_panel, label="Capacidad de Inventario:"), 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        self.inventory_gauge = wx.Gauge(list_panel, range=100, style=wx.GA_HORIZONTAL)
        gauge_sizer.Add(self.inventory_gauge, 1, wx.EXPAND | wx.ALL, 5)
        list_sizer.Add(gauge_sizer, 0, wx.EXPAND | wx.ALL, 5)
        list_panel.SetSizer(list_sizer)

        # Panel de productos más vendidos
        grid_panel = wx.Panel(self.data_tables_box, style=wx.BORDER_SUNKEN)
        grid_panel.SetBackgroundColour(wx.Colour(255, 255, 255))
        grid_sizer = wx.BoxSizer(wx.VERTICAL)
        grid_sizer.Add(wx.StaticText(grid_panel, label="Productos más vendidos"), 0, wx.ALIGN_CENTER | wx.TOP, 5)
        self.grid_2 = wx.grid.Grid(grid_panel)
        self.grid_2.CreateGrid(0, 3)
        self.grid_2.SetColLabelValue(0, "Producto")
        self.grid_2.SetColLabelValue(1, "Cantidad")
        self.grid_2.SetColLabelValue(2, "Total")
        self.no_sales_label = wx.StaticText(grid_panel, label="No hay ventas registradas", style=wx.ALIGN_CENTER)
        self.no_sales_label.Hide() 
        grid_sizer.Add(self.grid_2, 1, wx.EXPAND | wx.ALL, 5)
        grid_sizer.Add(self.no_sales_label, 1, wx.ALIGN_CENTER, 5)
        grid_panel.SetSizer(grid_sizer)
        
        self.data_tables_sizer.Add(list_panel, 1, wx.EXPAND | wx.ALL, 5)
        self.data_tables_sizer.Add(grid_panel, 1, wx.EXPAND | wx.ALL, 5)

    #----------------------------------------------------------------------
    # Métodos de manejo de datos
    #----------------------------------------------------------------------
    def load_data(self):
        # Simula la carga de datos y actualiza las tablas y la barra.
        products_data = [
            ("Vino tinto", "25", "V-101"),
            ("Cerveza", "50", "C-205"),
            ("Agua mineral", "100", "A-300")
        ]
        self._load_products(products_data)

        sales_data = [
            ("Vino tinto", 50, "$1500"),
            ("Cerveza", 30, "$600"),
            ("Refresco", 20, "$200")
        ]
        self._load_sales(sales_data)
        
        self.inventory_gauge.SetValue(75)

    def _load_products(self, data):
        # Carga y muestra los datos de los productos en el ListCtrl. 
        self.list_ctrl_1.DeleteAllItems()
        if not data:
            self.list_ctrl_1.Hide()
            self.no_products_label.Show()
        else:
            self.no_products_label.Hide()
            self.list_ctrl_1.Show()
            for row in data:
                index = self.list_ctrl_1.InsertItem(self.list_ctrl_1.GetItemCount(), str(row[0]))
                self.list_ctrl_1.SetItem(index, 1, str(row[1]))
                self.list_ctrl_1.SetItem(index, 2, str(row[2]))
        self.Layout()

    def _load_sales(self, data):
        # Carga y muestra los datos de ventas en el Grid.
        if not data:
            self.grid_2.Hide()
            self.no_sales_label.Show()
        else:
            self.no_sales_label.Hide()
            self.grid_2.Show()
            if self.grid_2.GetNumberRows() > 0:
                self.grid_2.DeleteRows(0, self.grid_2.GetNumberRows())
            
            self.grid_2.AppendRows(len(data))
            
            for row_idx, row_data in enumerate(data):
                for col_idx, cell_data in enumerate(row_data):
                    self.grid_2.SetCellValue(row_idx, col_idx, str(cell_data))
        self.Layout()