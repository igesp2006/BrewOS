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
        self.place_forget()

        self.create_widgets()



    def create_widgets(self):


        self.icon_label = ctk.CTkLabel(self,
                                       text='',
                                       image=self.imn.get_icon('settings',self.tmn.get("accent"),75))


        self.header_quote_label = ctk.CTkLabel(self,
                                              text='Customize your BrewOS experience!',
                                              text_color=self.tmn.get("text_secondary"),
                                              font=('Inter',15,))

        self.header_label = ctk.CTkLabel(self,
                                         text='Settings',
                                         text_color=self.tmn.get("text"),
                                         font=('Inter',33,'bold'))





    


    def animate(self):
      
        self.icon_label.place(x=25,y=25)
        self.header_quote_label.place(x=115,y=66)
        self.header_label.place(x=115,y=30)
