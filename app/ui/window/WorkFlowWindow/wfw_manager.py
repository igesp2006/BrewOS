import customtkinter as ctk
from app.ui.ui_utility.animations import slide, fade_in
from app.ui.theme.manager import ThemeManager,IconManager



class WorkflowWindowManager(ctk.CTkFrame):

    def __init__(self,parent:ctk.CTk,load_manager):

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
        self.animate()

        self.page_hash = {}


    def switch_page(self,name:str,page:ctk.CTkFrame):

        for i in self.page_hash:

            frame: ctk.CTkFrame = self.page_hash[i][0]
            tab: ctk.CTkButton = self.page_hash[i][1]

            frame.place_forget()
            tab.configure(fg_color=self.tmn.get("surface"),text_color=self.tmn.get("text"))


        selected_tab: ctk.CTkButton = self.page_hash[name][1]
        selected_tab.configure(fg_color=self.tmn.get("highlight"),text_color=self.tmn.get("accent"))

        page.place(x=0,y=0)
        page.animate()


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


        self.basics_tab = ctk.CTkButton(self.sidebarleftframe,
                                        text=' Basics',
                                        font=('Inter',17,'bold'),
                                        width=150,
                                        height=40,
                                        anchor='w',
                                        corner_radius=15,
                                        text_color=self.tmn.get("text"),
                                        fg_color=self.tmn.get("surface"),
                                        hover_color=self.tmn.get("accent_hover"),
                                        image=self.imn.get_icon("coffee",self.tmn.get("accent")),
                                        compound='left',
                                        command=None)


        self.brew_tab = ctk.CTkButton(self.sidebarleftframe,
                                        text=' Brew',
                                        font=('Inter',17,'bold'),
                                        width=150,
                                        height=40,
                                        anchor='w',
                                        corner_radius=15,
                                        text_color=self.tmn.get("text"),
                                        fg_color=self.tmn.get("surface"),
                                        hover_color=self.tmn.get("accent_hover"),
                                        image=self.imn.get_icon("droplets",self.tmn.get("accent")),
                                        compound='left',
                                        command=None)


        self.brewlog_tab = ctk.CTkButton(self.sidebarleftframe,
                                        text=' Evaluate',
                                        font=('Inter',17,'bold'),
                                        width=150,
                                        height=40,
                                        anchor='w',
                                        corner_radius=15,
                                        text_color=self.tmn.get("text"),
                                        fg_color=self.tmn.get("surface"),
                                        hover_color=self.tmn.get("accent_hover"),
                                        image=self.imn.get_icon("file-check",self.tmn.get("accent")),
                                        compound='left',
                                        command=None)





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



    def animate(self):
             
        self.brewos_label_button.place(x=35,y=35)

        self.sep_label.place(x=32,y=470)
        self.quote_label_p1.place(x=30,y=500)
        self.quote_label_p2.place(x=30,y=520)

            
        slide(self,
                self.basics_tab,
                0,24,
                -15,15,
                70,70,)

        self.after(30,lambda:slide(self,
                                    self.brew_tab,
                                    0,24,
                                    -15,15,
                                    120,120,))

        self.after(30,lambda:slide(self,
                                    self.brewlog_tab,
                                    0,24,
                                    -15,15,
                                    170,170,
                                    callback=lambda:self.after(10,lambda:fade_in(self,
                                                                            self.basics_tab,
                                                                            0,24,
                                                                            15,70,
                                                                            self.tmn.get("surface"),self.tmn.get("highlight")))))

        