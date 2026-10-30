import customtkinter as ctk
from PIL import Image
from app.ui.theme.manager import ThemeManager,IconManager
from app.ui.window.HomeWindow.cards.home_page import HomePage
from app.ui.window.HomeWindow.cards.recepies_page import RecepiePage
from app.ui.window.HomeWindow.cards.brewlog_page import BrewLogPage


class HomeWindowManager(ctk.CTkFrame):

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

        self.create_frames()
        self.place_widget_frame()
        self.widget_sidebar_left()


        home_page = HomePage(self.mainframe,self.tmn,self.imn)
        # recepie_page = RecepiePage(self.mainframe)
        # brewlog_page = BrewLogPage(self.mainframe)




    def place_widget_frame(self):

        self.sidebarleftframe.place(x=15,y=15)
        self.mainframe.place(x=220,y=0)



    def create_frames(self):

        self.sidebarleftframe = ctk.CTkFrame(self,
                                            width=190,
                                            height=560,
                                            corner_radius=20,
                                            bg_color=self.tmn.get("bg"),
                                            fg_color=self.tmn.get("surface"))


        self.mainframe = ctk.CTkFrame(self,
                                    width=780,
                                    height=590,
                                    corner_radius=0,
                                    bg_color=self.tmn.get("bg"),
                                    fg_color=self.tmn.get("bg"))



    def widget_sidebar_left(self):
    
    
            self.brewos_label_button = ctk.CTkButton(self,
                                                    text=" BrewOS",
                                                    font=('Inter',24,'bold'),
                                                    text_color=self.tmn.get("text"),
                                                    fg_color=self.tmn.get("surface"),
                                                    image=self.imn.get_icon("coffee",self.tmn.get("accent")),
                                                    compound='left',
                                                    hover=False,
                                                    bg_color=self.tmn.get("surface"),
                                                    command=None)
    
    
            self.home_tab = ctk.CTkButton(self.sidebarleftframe,
                                          text=' Home',
                                          font=('Inter',17,'bold'),
                                          width=150,
                                          height=40,
                                          anchor='w',
                                          corner_radius=15,
                                          text_color=self.tmn.get("text"),
                                          fg_color=self.tmn.get("surface"),
                                          hover_color=self.tmn.get("accent_hover"),
                                          image=self.imn.get_icon("house",self.tmn.get("accent")),
                                          compound='left')
    
    
            self.recepies_tab = ctk.CTkButton(self.sidebarleftframe,
                                          text=' Recipies',
                                          font=('Inter',17,'bold'),
                                          width=150,
                                          height=40,
                                          anchor='w',
                                          corner_radius=15,
                                          text_color=self.tmn.get("text"),
                                          fg_color=self.tmn.get("surface"),
                                          hover_color=self.tmn.get("accent_hover"),
                                          image=self.imn.get_icon("book-open",self.tmn.get("accent")),
                                          compound='left')
    
    
            self.brewlog_tab = ctk.CTkButton(self.sidebarleftframe,
                                          text=' Brew Log',
                                          font=('Inter',17,'bold'),
                                          width=150,
                                          height=40,
                                          anchor='w',
                                          corner_radius=15,
                                          text_color=self.tmn.get("text"),
                                          fg_color=self.tmn.get("surface"),
                                          hover_color=self.tmn.get("accent_hover"),
                                          image=self.imn.get_icon("rotate-ccw-clock",self.tmn.get("accent")),
                                          compound='left')
    
    
            self.settings_tab = ctk.CTkButton(self.sidebarleftframe,
                                          text=' Settings',
                                          font=('Inter',17,'bold'),
                                          width=150,
                                          height=40,
                                          anchor='w',
                                          corner_radius=15,
                                          text_color=self.tmn.get("text"),
                                          fg_color=self.tmn.get("surface"),
                                          hover_color=self.tmn.get("accent_hover"),
                                          image=self.imn.get_icon("settings",self.tmn.get("accent")),
                                          compound='left')
    
    
    
            self.sep_label = ctk.CTkLabel(self.sidebarleftframe,
                                        text='_________',
                                        font=('Inter',14,'bold'),
                                        text_color=self.tmn.get("text_muted"))
    
    
    
            self.quote_label_p1 = ctk.CTkLabel(self.sidebarleftframe,
                                            text='Better Coffee',
                                            font=('Inter',14,'italic','bold'),
                                            text_color=self.tmn.get("text_muted"))
    
            self.quote_label_p2 = ctk.CTkLabel(self.sidebarleftframe,
                                            text='With data',
                                            font=('Inter',14,'italic'),
                                            text_color=self.tmn.get("text_muted"))
    
    
    
    
    
            
            self.brewos_label_button.place(x=35,y=35)
    
            self.home_tab.place(x=15,y=70)
            self.recepies_tab.place(x=15,y=120)
            self.brewlog_tab.place(x=15,y=170)
            self.settings_tab.place(x=15,y=220)
            
            self.sep_label.place(x=32,y=470)
            self.quote_label_p1.place(x=30,y=500)
            self.quote_label_p2.place(x=30,y=520)
            
