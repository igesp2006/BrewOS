import customtkinter as ctk
from PIL import Image
from app.ui.theme.manager import ThemeManager,IconManager


class HomePage(ctk.CTkFrame):

    def __init__(self,parent:ctk.CTkFrame):

        self.tmn = ThemeManager()
        self.imn = IconManager()   

        super().__init__(
            parent,
            width=780,
            height=570,
            fg_color=self.tmn.get("bg")
        )

        self.place(x=0,y=0)
        self.mainframe_widgets()






    def mainframe_widgets(self):


        image = Image.open('assets\\banner\\banner_1.png')
        banner = ctk.CTkImage(light_image=image, dark_image=image, size=(750, 200))
        self.banner_label = ctk.CTkLabel(self,
                                         image=banner,
                                         text='',
                                         bg_color=self.tmn.get("bg"),
                                         fg_color=self.tmn.get("bg"))


        self.new_brew_button = ctk.CTkButton(self,
                                             text="New Brew",
                                             font=('Inter',23,'bold'),
                                             width=190,
                                             height=60,
                                             anchor='w',
                                             corner_radius=25,
                                             border_color=self.tmn.get("border"),
                                             border_width=4,
                                             text_color=self.tmn.get("text"),
                                             fg_color=self.tmn.get("surface"),
                                             hover_color=self.tmn.get("accent_hover"),
                                             image=self.imn.get_icon("plus",self.tmn.get("accent")),
                                             compound='left',
                                             command=None)



        self.card1 = ctk.CTkFrame(self,
                                  width=230,
                                  height=220,
                                  corner_radius=20,
                                  bg_color=self.tmn.get("bg"),
                                  fg_color=self.tmn.get("surface"))


        
        self.card2 = ctk.CTkFrame(self,
                                  width=230,
                                  height=220,
                                  corner_radius=20,
                                  bg_color=self.tmn.get("bg"),
                                  fg_color=self.tmn.get("surface"))

        
        self.card3 = ctk.CTkFrame(self,
                                  width=230,
                                  height=220,
                                  corner_radius=20,
                                  bg_color=self.tmn.get("bg"),
                                  fg_color=self.tmn.get("surface"))








        
        self.banner_label.place(x=13,y=30)
        self.new_brew_button.place(anchor='center',x=390,y=285)
        self.card1.place(x=23,y=340)
        self.card2.place(x=275,y=340)
        self.card3.place(x=525,y=340)



