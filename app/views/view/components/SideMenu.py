import wx

class SideMenu(wx.Panel):
    def __init__(self, parent_frame, parent_panel, size=(220, -1)):
        super(SideMenu, self).__init__(parent_panel, size=size)
        self.parent_frame = parent_frame

        # Paleta de colores 
        self.bg_color = wx.Colour(28, 40, 51)  
        self.hover_color = wx.Colour(47, 69, 89) 
        self.text_color = wx.Colour(236, 240, 241) 
        self.accent_color = wx.Colour(52, 152, 219) 

        self.SetBackgroundColour(self.bg_color)

        # Layout principal
        main_sizer = wx.BoxSizer(wx.VERTICAL)

        # --- LOGO / TÍTULO ---
        title_label = wx.StaticText(self, wx.ID_ANY, "⚙ ADMIN PANEL")
        title_label.SetForegroundColour(self.text_color)
        title_font = wx.Font(16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        title_label.SetFont(title_font)
        main_sizer.Add(title_label, 0, wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, 20)

        # --- BOTONES DEL MENÚ ---
        button_font = wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        menu_buttons = [
            ("🏠 Inicio", self.parent_frame.on_home),
            ("📁 Categorías", self.parent_frame.on_categories),
            ("🛒 Productos", self.parent_frame.on_products),
            ("💰 Ventas", lambda e: e.Skip()),
            ("📈 Reportes", lambda e: e.Skip())
        ]

        for label, handler in menu_buttons:
            btn = wx.Button(self, label=label, style=wx.NO_BORDER)
            btn.SetFont(button_font)
            btn.SetBackgroundColour(self.bg_color)
            btn.SetForegroundColour(self.text_color)
            btn.SetCursor(wx.Cursor(wx.CURSOR_HAND))
            btn.SetMinSize((220, 45))
            btn.Bind(wx.EVT_BUTTON, handler)
            btn.Bind(wx.EVT_ENTER_WINDOW, self.on_button_hover)
            btn.Bind(wx.EVT_LEAVE_WINDOW, self.on_button_leave)
            main_sizer.Add(btn, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 0)

        # --- SECCIÓN INFERIOR (FIJA) ---
        main_sizer.AddStretchSpacer()
        footer_btn = wx.Button(self, label="🚪 Salir", style=wx.NO_BORDER)
        footer_btn.SetFont(button_font)
        footer_btn.SetBackgroundColour(self.bg_color)
        footer_btn.SetForegroundColour(self.text_color)
        footer_btn.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        footer_btn.SetMinSize((220, 45))
        footer_btn.Bind(wx.EVT_BUTTON, lambda e: wx.GetTopLevelParent(self).Close())
        footer_btn.Bind(wx.EVT_ENTER_WINDOW, self.on_button_hover)
        footer_btn.Bind(wx.EVT_LEAVE_WINDOW, self.on_button_leave)
        main_sizer.Add(footer_btn, 0, wx.EXPAND)

        self.SetSizer(main_sizer)

    # --- Eventos Hover ---
    def on_button_hover(self, event):
        btn = event.GetEventObject()
        btn.SetBackgroundColour(self.hover_color)
        btn.Refresh()

    def on_button_leave(self, event):
        btn = event.GetEventObject()
        btn.SetBackgroundColour(self.bg_color)
        btn.Refresh()
