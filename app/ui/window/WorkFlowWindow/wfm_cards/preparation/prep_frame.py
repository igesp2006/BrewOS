import customtkinter as ctk
from PIL import Image
from app.ui.theme.manager import ThemeManager,IconManager
from app.ui.ui_utility.animations import slide, fade_in



class PrepFrame(ctk.CTkFrame):
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

        self.widgets()
        self.animate()



    def widgets(self):


        self.card1 = ctk.CTkButton(self,
                                    text='Coffee Info',
                                    text_color=self.tmn.get("text"),
                                    font=self.tmn.font(),
                                    width=230,
                                    height=220,
                                    corner_radius=20,
                                    bg_color=self.tmn.get("bg"),
                                    fg_color=self.tmn.get("surface"))


        self.card2 = ctk.CTkButton(self,
                                    text='Basics',
                                    text_color=self.tmn.get("text"),
                                    font=self.tmn.font(),
                                    width=230,
                                    height=220,
                                    corner_radius=20,
                                    bg_color=self.tmn.get("bg"),
                                    fg_color=self.tmn.get("surface"))
    
        
                
        self.card3 = ctk.CTkButton(self,
                                    text='Parameters',
                                    text_color=self.tmn.get("text"),
                                    font=self.tmn.font(),
                                    width=230,
                                    height=220,
                                    corner_radius=20,
                                    bg_color=self.tmn.get("bg"),
                                    fg_color=self.tmn.get("surface"))

        



    def animate(self):

  

        self.card1.place(x=17,y=320)
        self.card2.place(x=272,y=320)
        self.card3.place(x=525,y=320)