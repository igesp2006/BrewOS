import customtkinter as ctk
from app.ui.theme.manager import ThemeManager, IconManager


class EvalFrame(ctk.CTkFrame):
    def __init__(self,
                 parent: ctk.CTkFrame,
                 theme_manager: ThemeManager,
                 icon_manager: IconManager):

        self.tmn = theme_manager
        self.imn = icon_manager

        super().__init__(
            parent,
            width=780,
            height=570,
            fg_color=self.tmn.get("bg")
        )

        self.place(x=0, y=0)
        self.place_forget()
        

        self.widgets()
        self.animate()

    def widgets(self):
        self.card1 = ctk.CTkButton(self,
                                   text='Tasting Notes',
                                   text_color=self.tmn.get("text"),
                                   font=self.tmn.font(),
                                   width=230,
                                   height=220,
                                   corner_radius=20,
                                   bg_color=self.tmn.get("bg"),
                                   fg_color=self.tmn.get("surface"))

    def animate(self):
        self.card1.place(x=272, y=320)
