import customtkinter as ctk
from PIL import Image
from app.ui.theme.manager import ThemeManager,IconManager


class RecepiePage(ctk.CTkFrame):

    def __init__(self,parent:ctk.CTk):

        self.tmn = ThemeManager()
        self.imn = IconManager()   

        super().__init__(
            parent,
            width=1000,
            height=590,
            fg_color=self.tmn.get("bg")
        )

    
        self.place(x=0,y=0)
    