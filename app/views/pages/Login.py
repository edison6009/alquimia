import wx

class LoginPage(wx.Panel):
    def __init__(self, parent, main_frame):
        super(LoginPage, self).__init__(parent)
        self.main_frame = main_frame
        
        main_sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        # Panel izquierdo (ilustración o color sólido)
        left_panel = wx.Panel(self, wx.ID_ANY)
        left_panel.SetBackgroundColour(wx.Colour(33, 47, 61))  # Azul oscuro
        left_panel.SetMinSize((400, 450))
        main_sizer.Add(left_panel, 0, wx.EXPAND)
        
        # Panel derecho (Formulario)
        right_panel = wx.Panel(self, wx.ID_ANY)
        right_panel.SetBackgroundColour(wx.WHITE)
        right_panel_sizer = wx.BoxSizer(wx.VERTICAL)
        
        title_font = wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        title_label = wx.StaticText(right_panel, wx.ID_ANY, "Iniciar Sesión")
        title_label.SetFont(title_font)
        right_panel_sizer.Add(title_label, 0, wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, 40)
        
        # Campos
        username_label = wx.StaticText(right_panel, wx.ID_ANY, "Usuario")
        self.username_textctrl = wx.TextCtrl(right_panel, wx.ID_ANY)
        self.username_textctrl.SetMinSize((300, -1))
        
        password_label = wx.StaticText(right_panel, wx.ID_ANY, "Contraseña")
        self.password_textctrl = wx.TextCtrl(right_panel, wx.ID_ANY, style=wx.TE_PASSWORD)
        self.password_textctrl.SetMinSize((300, -1))
        
        right_panel_sizer.Add(username_label, 0, wx.ALIGN_LEFT | wx.LEFT | wx.TOP, 10)
        right_panel_sizer.Add(self.username_textctrl, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, 10)
        right_panel_sizer.Add(password_label, 0, wx.ALIGN_LEFT | wx.LEFT | wx.TOP, 10)
        right_panel_sizer.Add(self.password_textctrl, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, 10)
        
        # Botón de login
        self.login_btn = wx.Button(right_panel, wx.ID_ANY, "Iniciar Sesión")
        self.login_btn.SetBackgroundColour(wx.Colour(52, 152, 219))  # Azul
        self.login_btn.SetForegroundColour(wx.WHITE)
        self.login_btn.SetFont(wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.BOLD))
        right_panel_sizer.Add(self.login_btn, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 10)
        
        # Enlace a registro
        register_link = wx.StaticText(right_panel, wx.ID_ANY, "¿No tienes una cuenta? Regístrate aquí")
        font = wx.SystemSettings.GetFont(wx.SYS_DEFAULT_GUI_FONT)
        font.SetUnderlined(True)
        register_link.SetFont(font)
        register_link.SetForegroundColour(wx.Colour(231, 76, 60))  # Rojo
        register_link.Bind(wx.EVT_LEFT_UP, self.on_register_clicked)
        right_panel_sizer.Add(register_link, 0, wx.ALIGN_CENTER | wx.TOP, 20)
        right_panel_sizer.AddStretchSpacer()
        
        right_panel.SetSizer(right_panel_sizer)
        main_sizer.Add(right_panel, 1, wx.EXPAND)
        
        self.SetSizer(main_sizer)
        self.Layout()
    
    def on_register_clicked(self, event):
        self.main_frame.show_register_page()
    
    def on_login_clicked(self, event):
        username = self.username_textctrl.GetValue()
        password = self.password_textctrl.GetValue()
        wx.MessageBox(f"Login con Usuario: {username}", "Acción", wx.OK | wx.ICON_INFORMATION)