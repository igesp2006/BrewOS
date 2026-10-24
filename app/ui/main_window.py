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
        self.root.resizable(1,1)
        self.root.title("BrewOS")
        self.root.config(bg=self.bg)
        self.widget_sidebar_left()





    def widget_sidebar_left(self):

        self.sidebarleftframe = ctk.CTkFrame(self.root,
                                             width=220,
                                             height=790,
                                             corner_radius=0,
                                             bg_color=self.bg,
                                             fg_color=self.tmn.get("surface"))



        self.brewos_label = ctk.CTkLabel(self.sidebarleftframe,
                                         text="  BrewOS",
                                         font=('Inter',24,'bold'),
                                         text_color=self.tmn.get("text"),
                                         image=self.imn.get_icon("coffee",self.tmn.get("accent")),
                                         compound='left')





        self.home_tab = ctk.CTkButton(self.sidebarleftframe,
                                      text='  Home',
                                      font=('Inter',17,'bold'),
                                      width=170,
                                      height=40,
                                      anchor='w',
                                      text_color=self.tmn.get("text"),
                                      fg_color=self.tmn.get("surface"),
                                      hover_color=self.tmn.get("accent_hover"),
                                      image=self.imn.get_icon("house",self.tmn.get("accent")),
                                      compound='left'
                                      )



        self.recepies_tab = ctk.CTkButton(self.sidebarleftframe,
                                      text='  Recipies',
                                      font=('Inter',17,'bold'),
                                      width=170,
                                      height=40,
                                      anchor='w',
                                      text_color=self.tmn.get("text"),
                                      fg_color=self.tmn.get("surface"),
                                      hover_color=self.tmn.get("accent_hover"),
                                      image=self.imn.get_icon("book-open",self.tmn.get("accent")),
                                      compound='left'
                                      )


        self.brewlog_tab = ctk.CTkButton(self.sidebarleftframe,
                                      text='  Brew Log',
                                      font=('Inter',17,'bold'),
                                      width=170,
                                      height=40,
                                      anchor='w',
                                      text_color=self.tmn.get("text"),
                                      fg_color=self.tmn.get("surface"),
                                      hover_color=self.tmn.get("accent_hover"),
                                      image=self.imn.get_icon("rotate-ccw-clock",self.tmn.get("accent")),
                                      compound='left'
                                      )


        self.settings_tab = ctk.CTkButton(self.sidebarleftframe,
                                      text='  Settings',
                                      font=('Inter',17,'bold'),
                                      width=170,
                                      height=40,
                                      anchor='w',
                                      text_color=self.tmn.get("text"),
                                      fg_color=self.tmn.get("surface"),
                                      hover_color=self.tmn.get("accent_hover"),
                                      image=self.imn.get_icon("settings",self.tmn.get("accent")),
                                      compound='left'
                                      )



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




        self.sidebarleftframe.place(x=0,y=0)
        self.brewos_label.place(x=20,y=20)
        self.home_tab.place(x=20,y=70)
        self.recepies_tab.place(x=20,y=120)
        self.brewlog_tab.place(x=20,y=170)
        self.settings_tab.place(x=20,y=220)
        self.sep_label.place(x=32,y=505)
        self.quote_label_p1.place(x=30,y=530)
        self.quote_label_p2.place(x=30,y=550)
        self.widget_mainframe()





    def widget_mainframe(self):
        pass




    def update(self):
        self.root.mainloop()


    