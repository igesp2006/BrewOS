import customtkinter as ctk
from PIL import Image
from app.ui.theme.manager import ThemeManager,IconManager
from app.ui.ui_utility.animations import slide, fade_in


class HomePage(ctk.CTkFrame):

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



    def animate(self):
        
        self.new_brew_button.place(anchor='center')

        fade_in(self,
                self.new_brew_button,
                0,24,
                390,285,
                self.tmn.get("bg"),self.tmn.get("surface"))

        self.after(50,lambda:fade_in(self,
                                     self.card1,
                                     0,24,
                                     23,340,
                                     self.tmn.get("bg"),self.tmn.get("surface")))

        self.after(70,lambda:fade_in(self,
                                     self.card2,
                                     0,24,
                                     275,340,
                                     self.tmn.get("bg"),self.tmn.get("surface")))

        self.after(90,lambda:fade_in(self,
                                     self.card3,
                                     0,24,
                                     525,340,
                                     self.tmn.get("bg"),self.tmn.get("surface")))


        
