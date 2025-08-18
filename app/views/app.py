import wx
# --- 1. Importaciones ---
from app.views.components.SideMenu import SideMenu
from app.views.pages.AdminPage import AdminPage
from app.views.pages.CategoryPage import CategoryPage
from app.views.pages.Login import LoginPage
from app.views.pages.Register import RegisterPage

class MiVentana(wx.Frame):
    def __init__(self, parent, title):
        super(MiVentana, self).__init__(parent, title=title, size=(900, 650))
        
        # --- 2. Configuración Inicial y Sizers Principales ---
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        
        # --- 3. Creación de Paneles Contenedores y Páginas ---
        
        # Panel contenedor para Login y Register (Auth Panel)
        self.auth_panel = wx.Panel(self)
        auth_sizer = wx.BoxSizer(wx.VERTICAL)
        self.login_page = LoginPage(self.auth_panel, self) 
        self.register_page = RegisterPage(self.auth_panel, self)
        auth_sizer.Add(self.login_page, 1, wx.EXPAND)
        auth_sizer.Add(self.register_page, 1, wx.EXPAND)
        self.auth_panel.SetSizer(auth_sizer)
        
        # Panel principal con el SideMenu y el contenido (Main Content Panel)
        self.main_content_panel = wx.Panel(self)
        self.main_content_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.side_menu = SideMenu(self, self.main_content_panel)
        self.admin_page = AdminPage(self.main_content_panel)
        self.category_page = CategoryPage(self.main_content_panel)
        self.main_pages_sizer = wx.BoxSizer(wx.VERTICAL)
        self.main_pages_sizer.Add(self.admin_page, 1, wx.EXPAND)
        self.main_pages_sizer.Add(self.category_page, 1, wx.EXPAND)
        self.main_content_sizer.Add(self.side_menu, 0, wx.EXPAND | wx.ALL, 5)
        self.main_content_sizer.Add(self.main_pages_sizer, 1, wx.EXPAND | wx.ALL, 5)
        self.main_content_panel.SetSizer(self.main_content_sizer)

        # --- 4. Ensamblaje de la Interfaz Final ---
        self.main_sizer.Add(self.auth_panel, 1, wx.EXPAND)
        self.main_sizer.Add(self.main_content_panel, 1, wx.EXPAND)
        self.SetSizer(self.main_sizer)

        # --- 5. Lógica de Visibilidad Inicial ---
        self.register_page.Hide()
        self.main_content_panel.Hide()
        self.admin_page.Hide()
        self.category_page.Hide()
        self.current_page = None
        self.Layout()

        # --- 6. Menú Superior y Barra de Estado ---
        barra_menu = wx.MenuBar()
        menu_archivo = wx.Menu()
        item_salir = menu_archivo.Append(wx.ID_EXIT, "Salir\tCtrl+Q", "Cerrar la aplicación")
        menu_ayuda = wx.Menu()
        item_acerca = menu_ayuda.Append(wx.ID_ABOUT, "Acerca de")
        barra_menu.Append(menu_archivo, "&Archivo")
        barra_menu.Append(menu_ayuda, "&Acerca de")
        self.SetMenuBar(barra_menu)
        self.CreateStatusBar()
        self.SetStatusText("Aplicación iniciada")

        # --- 7. Enlace de Eventos (Binding) ---
        self.Bind(wx.EVT_MENU, self.cerrar_aplicacion, item_salir)
        self.Bind(wx.EVT_MENU, self.mostrar_acerca_de, item_acerca)
        self.login_page.login_btn.Bind(wx.EVT_BUTTON, self.on_login_success)
    
    # --- 8. Métodos de Lógica de la Aplicación ---
    
    # Login
    def on_login_success(self, event):
        self.auth_panel.Hide()
        self.main_content_panel.Show()
        self.show_page(self.admin_page)
        self.Layout()

    def show_register_page(self):
        self.login_page.Hide()
        self.register_page.Show()
        self.Layout()

    def show_login_page(self):
        self.register_page.Hide()
        self.login_page.Show()
        self.Layout()

    # Menu
    def show_page(self, page):
        if self.current_page:
            self.current_page.Hide()
        self.current_page = page
        self.current_page.Show()
        self.Layout()

    def on_home(self, event):
        print("Botón de Inicio presionado.")

    def on_products(self, event):
        print("Botón de Productos presionado.")
        self.show_page(self.admin_page)

    def on_categories(self, event):
        print("Botón de Categorías presionado.")
        self.show_page(self.category_page)

    def cerrar_aplicacion(self, event):
        self.Close(True)
    
    def mostrar_acerca_de(self, event):
        wx.MessageBox("Aplicación creada con wxPython", "Acerca de", wx.OK | wx.ICON_INFORMATION)