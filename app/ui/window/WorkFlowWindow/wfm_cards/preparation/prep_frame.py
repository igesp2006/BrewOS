import customtkinter as ctk
from PIL import Image
from app.ui.theme.manager import ThemeManager,IconManager,ImageManager



class PrepFrame(ctk.CTkFrame):
    def __init__(self,
                     parent:ctk.CTkFrame,
                     theme_manager:ThemeManager,
                     icon_manager:IconManager):
    
            
        self.tmn = theme_manager
        self.imn = icon_manager
        self.imgm = ImageManager()


        super().__init__(
            parent,
            width=780,
            height=590,
            fg_color=self.tmn.get("bg")
        )

        
        self.place(x=0,y=0)
        self.place_forget()

        self.create_prep_frame()


    def create_prep_frame(self):

        self.create_heading()
        self.create_coffee_info_card()
        self.create_basics_card()
        self.create_parameters_card()
        self.animate()


    def create_heading(self):

        self.title_label = ctk.CTkLabel(self,
                                        text='Preparation',
                                        text_color=self.tmn.get("text"),
                                        font=('Georgia',38,'bold','underline'),
                                        anchor='w')

        self.subtitle_label = ctk.CTkLabel(self,
                                           text='Set up your brew session',
                                           text_color=self.tmn.get("text_muted"),
                                           font=self.tmn.font(size=20,formatting='bold'),
                                           anchor='w')


    def create_coffee_info_card(self):

        self.card1 = ctk.CTkButton(self,
                                  width=225,
                                  height=450,
                                  hover=False,
                                  corner_radius=20,
                                #   border_color=self.tmn.get('accent_hover'),
                                #   border_width=3,
                                  fg_color=self.tmn.get("surface"))


        self.card1_image = ctk.CTkLabel(self.card1,
                                        text='',
                                        image=self.imgm.get_image('gunnybag',205,280))

        self.card1_icon = ctk.CTkLabel(self.card1,
                                       text='',
                                       image=self.imn.get_icon('droplets',self.tmn.get("accent"),34))

        self.card1_title = ctk.CTkLabel(self.card1,
                                        text='Coffee Info',
                                        text_color=self.tmn.get("text"),
                                        font=('Georgia',21,'bold'),
                                        anchor='w')

        self.card1_description = ctk.CTkLabel(self.card1,
                                              text='About your coffee.',
                                              text_color=self.tmn.get("text_muted"),
                                              font=self.tmn.font(size=14),
                                              anchor='w')

        self.card1_explore = ctk.CTkLabel(self.card1,
                                          text='Explore  →',
                                          text_color=self.tmn.get("accent"),
                                          font=self.tmn.font(size=14,formatting='bold'),
                                          anchor='w')


    def create_basics_card(self):

        self.card2 = ctk.CTkButton(self,
                                  width=225,
                                  height=450,
                                  hover=False,
                                  corner_radius=20,
                                #   border_color=self.tmn.get('accent_hover'),
                                #   border_width=3,
                                  fg_color=self.tmn.get("surface"))


        self.card2_image = ctk.CTkLabel(self.card2,
                                        text='',
                                        image=self.imgm.get_image('checklist',205,280))

        self.card2_icon = ctk.CTkLabel(self.card2,
                                       text='',
                                       image=self.imn.get_icon('book-open',self.tmn.get("accent"),34))

        self.card2_title = ctk.CTkLabel(self.card2,
                                        text='Basics',
                                        text_color=self.tmn.get("text"),
                                        font=('Georgia',21,'bold'),
                                        anchor='w')

        self.card2_description = ctk.CTkLabel(self.card2,
                                              text='Basic parameters.',
                                              text_color=self.tmn.get("text_muted"),
                                              font=self.tmn.font(size=14),
                                              anchor='w')

        self.card2_explore = ctk.CTkLabel(self.card2,
                                          text='Explore  →',
                                          text_color=self.tmn.get("accent"),
                                          font=self.tmn.font(size=14,formatting='bold'),
                                          anchor='w')


    def create_parameters_card(self):

        self.card3 = ctk.CTkButton(self,
                                  width=225,
                                  height=450,
                                  hover=False,
                                  corner_radius=20,
                                #   border_color=self.tmn.get('accent_hover'),
                                #   border_width=3,
                                  fg_color=self.tmn.get("surface"))


        self.card3_image = ctk.CTkLabel(self.card3,
                                        text='',
                                        image=self.imgm.get_image('pourover',205,280))

        self.card3_icon = ctk.CTkLabel(self.card3,
                                       text='',
                                       image=self.imn.get_icon('settings',self.tmn.get("accent"),34))

        self.card3_title = ctk.CTkLabel(self.card3,
                                        text='Parameters',
                                        text_color=self.tmn.get("text"),
                                        font=('Georgia',21,'bold'),
                                        anchor='w')

        self.card3_description = ctk.CTkLabel(self.card3,
                                              text='Fine-tune your brew.',
                                              text_color=self.tmn.get("text_muted"),
                                              font=self.tmn.font(size=14),
                                              anchor='w')

        self.card3_explore = ctk.CTkLabel(self.card3,
                                          text='Explore  →',
                                          text_color=self.tmn.get("accent"),
                                          font=self.tmn.font(size=14,formatting='bold'),
                                          anchor='w')

    def animate(self):


        self.title_label.place(x=24,y=22)
        self.subtitle_label.place(x=24,y=70)

        self.card1.place(x=10,y=112)
        self.card2.place(x=270,y=112)
        self.card3.place(x=530,y=112)

        self.card1_image.place(x=10,y=10)
        self.card2_image.place(x=10,y=10)
        self.card3_image.place(x=10,y=10)

        self.card1_icon.place(x=24,y=310)
        self.card2_icon.place(x=24,y=310)
        self.card3_icon.place(x=24,y=310)

        self.card1_title.place(x=24,y=349)
        self.card2_title.place(x=24,y=349)
        self.card3_title.place(x=24,y=349)

        self.card1_description.place(x=24,y=375)
        self.card2_description.place(x=24,y=375)
        self.card3_description.place(x=24,y=375)

        self.card1_explore.place(x=24,y=400)
        self.card2_explore.place(x=24,y=400)
        self.card3_explore.place(x=24,y=400)
