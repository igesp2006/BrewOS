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


        # dfc => default settings card
        self.dfc = ctk.CTkFrame(self,
                                    width=370,
                                    height=370,
                                    corner_radius=20,
                                    bg_color=self.tmn.get("bg"),
                                    fg_color=self.tmn.get("surface"))
        self.dfc_card()
        
        # aprc => apperance card
        self.aprc = ctk.CTkFrame(self,
                                    width=330,
                                    height=170,
                                    corner_radius=20,
                                    bg_color=self.tmn.get("bg"),
                                    fg_color=self.tmn.get("surface"))
        self.aprc_card()

        # ifc => info card
        self.ifc = ctk.CTkFrame(self,
                                    width=330,
                                    height=220,
                                    corner_radius=20,
                                    bg_color=self.tmn.get("bg"),
                                    fg_color=self.tmn.get("surface"))
        self.ifc_card()




    def aprc_card(self):

        # aprc
        ######

        self.aprc_title_label = ctk.CTkLabel(self.aprc,
                                                text='  Appearance',
                                                text_color=self.tmn.get("text_secondary"),
                                                font=self.tmn.font(size=20,formatting='bold'),
                                                image=self.imn.get_icon("palette",self.tmn.get("accent"),30),
                                                compound='left')

        
        self.menu_title = ctk.CTkLabel(self.aprc,
                                        text='Select Theme',
                                        text_color=self.tmn.get("text_secondary"),
                                        font=self.tmn.font(formatting='italic'))


        self.menu = ctk.CTkOptionMenu(self.aprc,
                                        height=45,
                                        width=270,
                                        corner_radius=30,
                                        values=[self.tmn.palettes[i]['name'] for i in self.tmn.palettes],
                                        font=self.tmn.font(size=19,formatting='bold'),
                                        text_color=self.tmn.get("text_secondary"),
                                        fg_color=self.tmn.get("elevated"),
                                        dropdown_fg_color=self.tmn.get("elevated"),
                                        button_color=self.tmn.get("elevated"),
                                        button_hover_color=self.tmn.get("accent_hover"),
                                        anchor='center',
                                        command=None)

            
        self.menu.set(self.tmn.colours['name'])  
        



    def ifc_card(self):
        
        # ifc
        ######
        
        self.ifc_title_label_p1 = ctk.CTkLabel(self.ifc,
                                                text='  BrewOS',
                                                text_color=self.tmn.get("text_secondary"),
                                                font=self.tmn.font(size=27,formatting='bold'),
                                                image=self.imn.get_icon("coffee",self.tmn.get("accent"),32),
                                                compound='left')
        
        self.ifc_title_label_p2 = ctk.CTkLabel(self.ifc,
                                                text='v1.0.0',
                                                text_color=self.tmn.get("text_secondary"),
                                                font=self.tmn.font(size=15,formatting='italic'),
                                                )
        


        self.ifc_ln1_label = ctk.CTkLabel(self.ifc,
                                            text='  Author: Garvit',
                                            text_color=self.tmn.get("text_secondary"),
                                            font=self.tmn.font(formatting='italic'),
                                            image=self.imn.get_icon("user",self.tmn.get("accent"),19),
                                            compound='left')

        self.ifc_ln2_label = ctk.CTkLabel(self.ifc,
                                            text='  igesp2006/BrewOS',
                                            text_color=self.tmn.get("text_secondary"),
                                            font=self.tmn.font(formatting='italic'),
                                            image=self.imn.get_icon("github",self.tmn.get("accent"),19),
                                            compound='left')

        self.ifc_ln3_label = ctk.CTkLabel(self.ifc,
                                            text='  License: MIT',
                                            text_color=self.tmn.get("text_secondary"),
                                            font=self.tmn.font(formatting='italic'),
                                            image=self.imn.get_icon("scroll-text",self.tmn.get("accent"),19),
                                            compound='left')
        


    def dfc_card(self):


        # dfc
        self.dfc_title_label = ctk.CTkLabel(self.dfc,
                                                text=' Defaults',
                                                text_color=self.tmn.get("text_secondary"),
                                                font=self.tmn.font(size=20,formatting='bold'),
                                                image=self.imn.get_icon("sliders",self.tmn.get("accent"),30),
                                                compound='left')

        dropdown_style = {
            "height": 38,
            "width": 180,
            "corner_radius":25,
            "font": self.tmn.font(size=16,formatting='bold'),
            "text_color": self.tmn.get("text_secondary"),
            "fg_color": self.tmn.get("elevated"),
            "dropdown_fg_color": self.tmn.get("elevated"),
            "button_color": self.tmn.get("elevated"),
            "button_hover_color": self.tmn.get("accent_hover"),
            "anchor": 'center',
        }

        self.default_ratio_label = ctk.CTkLabel(
            self.dfc,
            text='Default Ratio',
            text_color=self.tmn.get("text_secondary"),
            font=self.tmn.font(formatting='italic'))

        
        self.default_ratio_menu = ctk.CTkOptionMenu(
            self.dfc,
            values=['1:14','1:15','1:16','1:17','1:18','1:19'],
            **dropdown_style)
        
        self.default_ratio_menu.set('1:15')



        self.default_bloom_water_label = ctk.CTkLabel(
            self.dfc,
            text='Default Bloom Water',
            text_color=self.tmn.get("text_secondary"),
            font=self.tmn.font(formatting='italic'))
        
        self.default_bloom_water_menu = ctk.CTkOptionMenu(
            self.dfc,
            values=['30 ml', '40 ml', '50 ml', '60 ml'],
            **dropdown_style)
        
        self.default_bloom_water_menu.set('30 ml')



        self.default_bloom_time_label = ctk.CTkLabel(
            self.dfc,
            text='Default Bloom Time',
            text_color=self.tmn.get("text_secondary"),
            font=self.tmn.font(formatting='italic'))
        
        self.default_bloom_time_menu = ctk.CTkOptionMenu(
            self.dfc,
            values=['30 sec', '40 sec', '45 sec', '60 sec'],
            **dropdown_style)
        
        self.default_bloom_time_menu.set('30 sec')
        





    def animate(self):
      
        self.icon_label.place(x=25,y=25)
        self.header_quote_label.place(x=115,y=66)
        self.header_label.place(x=115,y=30)

        self.dfc.place(x=375,y=130)
        self.dfc_title_label.place(x=15,y=10)
        self.default_ratio_label.place(x=25,y=65)
        self.default_ratio_menu.place(x=20,y=95)
        self.default_bloom_water_label.place(x=25,y=155)
        self.default_bloom_water_menu.place(x=20,y=185)
        self.default_bloom_time_label.place(x=25,y=245)
        self.default_bloom_time_menu.place(x=20,y=275)


        self.aprc.place(x=25,y=130)
        self.aprc_title_label.place(x=15,y=10)
        self.menu_title.place(x=35,y=60)
        self.menu.place(x=30,y=90)


        self.ifc.place(x=25,y=330)
        self.ifc_title_label_p1.place(x=15,y=13)
        self.ifc_title_label_p2.place(x=180,y=19)
        self.ifc_ln1_label.place(x=25,y=95)
        self.ifc_ln2_label.place(x=25,y=65)
        self.ifc_ln3_label.place(x=25,y=125)