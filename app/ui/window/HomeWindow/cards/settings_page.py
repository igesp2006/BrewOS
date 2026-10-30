import customtkinter as ctk
from PIL import Image
from app.ui.theme.manager import ThemeManager,IconManager


class SettingsPage(ctk.CTkFrame):

    def __init__(self,
                 parent:ctk.CTkFrame,
                 theme_manager:ThemeManager,
                 icon_manager:IconManager):
    
    
        self.tmn = theme_manager
        self.imn = icon_manager   

        super().__init__(
            parent,
            width=780,
            height=570,
            fg_color=self.tmn.get("bg")
        )

        self.place(x=0,y=0)

        self.create_widgets()


    def create_widgets(self):


        label = ctk.CTkLabel(self,
                             text='coming soon',
                             text_color=self.tmn.get("text"))

        label.place(x=390,y=285,anchor='center')


