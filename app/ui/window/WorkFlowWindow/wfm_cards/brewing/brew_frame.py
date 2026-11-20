import customtkinter as ctk
from app.ui.theme.manager import ThemeManager, IconManager, ImageManager



class BrewFrame(ctk.CTkFrame):
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

        self.widgets()
        self.animate()


    def create_heading(self):


        self.title_label = ctk.CTkLabel(self,
                                        text="Brewing",
                                        text_color=self.tmn.get("text"),
                                        font=("Georgia", 38, "bold", "underline"),
                                        anchor="w")

        
        self.subtitle_label = ctk.CTkLabel(self,
                                            text="Shape the flow and strength of your brew",
                                            text_color=self.tmn.get("text_muted"),
                                            font=self.tmn.font(size=20, formatting="bold"),
                                            anchor="w")




    def widgets(self):
        self.create_heading()

        self.card1 = ctk.CTkFrame(self,
                                  width=350,
                                  height=460,
                                  corner_radius=20,
                                  fg_color=self.tmn.get("surface"))
        self.card2 = ctk.CTkFrame(self,
                                  width=350,
                                  height=460,
                                  corner_radius=20,
                                  fg_color=self.tmn.get("surface"))

        self.card1_image = ctk.CTkLabel(self.card1, 
                                        text="",
                                        image=self.imgm.get_image("bloom", 310, 310))

        
        self.card1_icon = ctk.CTkLabel(self.card1, 
                                        text="",
                                        image=self.imn.get_icon("droplets", self.tmn.get("accent"), 32))

        
        self.card1_title = ctk.CTkLabel(self.card1, 
                                        text="Pouring",
                                        text_color=self.tmn.get("text"),
                                        font=("Georgia", 30, "bold"), anchor="w")

        
        self.card1_description = ctk.CTkLabel(self.card1, 
                                        text="Control the flow of your brew.",
                                        text_color=self.tmn.get("text_muted"),
                                        font=self.tmn.font(size=15), anchor="w")

        
        self.card1_explore = ctk.CTkLabel(self.card1, 
                                        text="Explore  →",
                                        text_color=self.tmn.get("accent"),
                                        font=self.tmn.font(size=15, formatting="bold"), anchor="w")


        self.card2_image = ctk.CTkLabel(self.card2, 
                                        text="",
                                        image=self.imgm.get_image("coffeecup", 310, 310))

        
        self.card2_icon = ctk.CTkLabel(self.card2, 
                                       text="",
                                        image=self.imn.get_icon("pipette", self.tmn.get("accent"), 32))

        
        self.card2_title = ctk.CTkLabel(self.card2, 
                                        text="Extraction",
                                        text_color=self.tmn.get("text"),
                                        font=("Georgia", 30, "bold"), anchor="w")

        
        self.card2_description = ctk.CTkLabel(self.card2, 
                                            text="Dial in your extraction.",
                                            text_color=self.tmn.get("text_muted"),
                                            font=self.tmn.font(size=15), anchor="w")

        
        self.card2_explore = ctk.CTkLabel(self.card2, 
                                            text="Explore  →",
                                            text_color=self.tmn.get("accent"),
                                            font=self.tmn.font(size=15, formatting="bold"), anchor="w")
        

    def animate(self):

        self.title_label.place(x=24, y=16)
        self.subtitle_label.place(x=24, y=64)

        self.card1.place(x=25, y=112)
        self.card2.place(x=405, y=112)

        self.card1_image.place(x=20, y=20)
        self.card2_image.place(x=20, y=20)
        self.card1_icon.place(x=24, y=355)
        self.card2_icon.place(x=24, y=355)
        self.card1_title.place(x=70, y=355)
        self.card2_title.place(x=70, y=355)
        self.card1_description.place(x=24, y=395)
        self.card2_description.place(x=24, y=395)
        self.card1_explore.place(x=24, y=420)
        self.card2_explore.place(x=24, y=420)
