import wx

from app.controllers.user_controller import UserController

from app.mixins.has_error_payload import has_error_payload


class RegisterPage(wx.Panel):
    def __init__(self, parent, main_frame):
        super(RegisterPage, self).__init__(parent)
        self.main_frame = main_frame
        
        main_sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        # Panel izquierdo
        left_panel = wx.Panel(self, wx.ID_ANY)
        left_panel.SetBackgroundColour(wx.Colour(33, 47, 61))
        left_panel.SetMinSize((400, 450))
        main_sizer.Add(left_panel, 0, wx.EXPAND)
        
        # Panel derecho (Formulario)
        right_panel = wx.Panel(self, wx.ID_ANY)
        right_panel.SetBackgroundColour(wx.WHITE)
        right_panel_sizer = wx.BoxSizer(wx.VERTICAL)
        
        title_font = wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        title_label = wx.StaticText(right_panel, wx.ID_ANY, "Crear Cuenta")
        title_label.SetFont(title_font)
        right_panel_sizer.Add(title_label, 0, wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, 40)
        
        # Campos
        self.name_textctrl = wx.TextCtrl(right_panel, wx.ID_ANY)
        self.name_textctrl.SetMinSize((300, -1))

        self.last_name_textctrl = wx.TextCtrl(right_panel, wx.ID_ANY)
        self.last_name_textctrl.SetMinSize((300, -1))

        self.username_textctrl = wx.TextCtrl(right_panel, wx.ID_ANY)
        self.username_textctrl.SetMinSize((300, -1))
        
        self.email_textctrl = wx.TextCtrl(right_panel, wx.ID_ANY)
        self.email_textctrl.SetMinSize((300, -1))

        self.phone_textctrl = wx.TextCtrl(right_panel, wx.ID_ANY)
        self.phone_textctrl.SetMinSize((300, -1))
        
        self.password_textctrl = wx.TextCtrl(right_panel, wx.ID_ANY, style=wx.TE_PASSWORD)
        self.password_textctrl.SetMinSize((300, -1))
        
        self.confirm_textctrl = wx.TextCtrl(right_panel, wx.ID_ANY, style=wx.TE_PASSWORD)
        self.confirm_textctrl.SetMinSize((300, -1))
        
        fields = [
            ("Nombre", self.name_textctrl),
            ("Apellido", self.last_name_textctrl),
            ("Usuario", self.username_textctrl),
            ("Correo Electrónico", self.email_textctrl),
            ("Teléfono", self.phone_textctrl),
            ("Contraseña", self.password_textctrl),
            ("Confirmar Contraseña", self.confirm_textctrl),
        ]
        for label, ctrl in fields:
            label_ctrl = wx.StaticText(right_panel, wx.ID_ANY, label)
            right_panel_sizer.Add(label_ctrl, 0, wx.ALIGN_LEFT | wx.LEFT | wx.TOP, 10)
            right_panel_sizer.Add(ctrl, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, 10)
        
        # Botón registrar
        self.register_btn = wx.Button(right_panel, wx.ID_ANY, "Registrarse")
        self.register_btn.SetBackgroundColour(wx.Colour(52, 152, 219))
        self.register_btn.SetForegroundColour(wx.WHITE)
        self.register_btn.SetFont(wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.BOLD))
        right_panel_sizer.Add(self.register_btn, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 10)
        self.register_btn.Bind(wx.EVT_BUTTON, self.on_register_clicked)
        
        # Enlace volver a login
        login_link = wx.StaticText(right_panel, wx.ID_ANY, "¿Ya tienes cuenta? Inicia sesión aquí")
        font = wx.SystemSettings.GetFont(wx.SYS_DEFAULT_GUI_FONT)
        font.SetUnderlined(True)
        login_link.SetFont(font)
        login_link.SetForegroundColour(wx.Colour(231, 76, 60))
        login_link.Bind(wx.EVT_LEFT_UP, self.on_login_clicked)
        right_panel_sizer.Add(login_link, 0, wx.ALIGN_CENTER | wx.TOP, 20)
        right_panel_sizer.AddStretchSpacer()
        
        right_panel.SetSizer(right_panel_sizer)
        main_sizer.Add(right_panel, 1, wx.EXPAND)
        
        self.SetSizer(main_sizer)
        self.Layout()
        
    def on_register_clicked(self, event):
        name = self.name_textctrl.GetValue()
        last_name = self.last_name_textctrl.GetValue()
        username = self.username_textctrl.GetValue()
        email = self.email_textctrl.GetValue()
        phone = self.phone_textctrl.GetValue()
        password = self.password_textctrl.GetValue()
        confirm = self.confirm_textctrl.GetValue()
        
        user_controller = UserController()
        data = user_controller.register(
        name=name,
        last_name=last_name,
        username=username,
        email=email,
        phone=phone,
        password=password
        )
        
        print(data)
        
    
    def on_login_clicked(self, event):
        self.main_frame.show_login_page()