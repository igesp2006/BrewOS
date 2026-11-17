import customtkinter as ctk
from app.ui.theme.manager import ThemeManager, IconManager, ImageManager


class EvalFrame(ctk.CTkFrame):
    def __init__(self,
                 parent: ctk.CTkFrame,
                 theme_manager: ThemeManager,
                 icon_manager: IconManager):

        self.tmn = theme_manager
        self.imn = icon_manager
        self.imgm = ImageManager()

        super().__init__(
            parent,
            width=780,
            height=590,
            fg_color=self.tmn.get("bg")
        )

        self.place(x=0, y=0)
        self.place_forget()
        

        self.widgets()
        self.animate()

    def widgets(self):
        self.title_label = ctk.CTkLabel(
            self,
            text="Evaluation",
            text_color=self.tmn.get("text"),
            font=("Georgia", 38, "bold", "underline"),
            anchor="w")
        self.subtitle_label = ctk.CTkLabel(
            self,
            text="Record what you taste in the cup",
            text_color=self.tmn.get("text_muted"),
            font=self.tmn.font(size=20, formatting="bold"),
            anchor="w")

        self.card1 = ctk.CTkFrame(self,
                                  width=620,
                                  height=350,
                                  corner_radius=20,
                                  fg_color=self.tmn.get("surface"))
        self.card1_image = ctk.CTkLabel(
            self.card1, text="",
            image=self.imgm.get_image(
                "tastingnote_card_coffee_cup_flavorwheel", 300, 300))
        self.card1_icon = ctk.CTkLabel(
            self.card1, text="",
            image=self.imn.get_icon("file-check", self.tmn.get("accent"), 32))
        self.card1_title = ctk.CTkLabel(
            self.card1, text="Tasting Notes",
            text_color=self.tmn.get("text"),
            font=("Georgia", 24, "bold"), anchor="w", width=270)
        self.card1_description = ctk.CTkLabel(
            self.card1, text="Capture the flavour of your brew.",
            text_color=self.tmn.get("text_muted"),
            font=self.tmn.font(size=15), anchor="w", width=270,
            wraplength=270)
        self.card1_explore = ctk.CTkLabel(
            self.card1, text="Explore  →",
            text_color=self.tmn.get("accent"),
            font=self.tmn.font(size=15, formatting="bold"), anchor="w",
            width=270)

    def animate(self):
        self.title_label.place(x=24, y=16)
        self.subtitle_label.place(x=24, y=64)

        self.card1.place(x=80, y=112)
        self.card1_image.place(x=20, y=25)
        self.card1_icon.place(x=350, y=145)
        self.card1_title.place(x=398, y=142)
        self.card1_description.place(x=350, y=195)
        self.card1_explore.place(x=350, y=245)
