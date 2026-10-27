import customtkinter as ctk
from PIL import Image
from app.ui.theme.manager import ThemeManager,IconManager
from app.ui.ui_utility.functions import center_window



class MainWindow():

    def __init__(self):

        self.tmn = ThemeManager()
        self.imn = IconManager()
        
        self.bg = self.tmn.get("bg")
        self.root = ctk.CTk()
        self.root.geometry(center_window(self.root,1000,590))
        self.root.resizable(0,0)
        self.root.title("BrewOS")
        self.root.config(bg=self.bg)
       

   

    def update(self):
        self.root.mainloop()


    