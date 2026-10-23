from app.ui.theme.pallets import PALETTES, DEFAULT_PALETTE
from io import BytesIO
from pathlib import Path
from resvg_py import svg_to_bytes
import customtkinter as ctk
from PIL import Image



class ThemeManager:

    def __init__(self, palette_name=DEFAULT_PALETTE):

        self.set_palette(palette_name)


    def set_palette(self, palette_name):

        '''sets the palatte'''

        if palette_name not in PALETTES:
            raise ValueError(
                f"Unknown palette: {palette_name}"
            )

        self.palette_name = palette_name
        self.colours = PALETTES[palette_name]
        

    def get(self, colour):

        '''fetches and returns colour of the selected palatte'''
        
        return self.colours[colour]


class IconManager:
    
    def __init__(self, icon_dir="assets/icon"):
        self.icon_dir = Path(icon_dir)
        self.cache = {}

    def get_icon(self, name, color="#C58B60", size=24):
        key = (name, color, size)

        if key in self.cache:
            return self.cache[key]

        path = self.icon_dir / f"{name}.svg"
        svg = path.read_text(encoding="utf-8")
        svg = svg.replace("currentColor", color)

        png_data = svg_to_bytes(
            svg_string=svg,
            width=size,
            height=size,
        )

        image = Image.open(BytesIO(png_data)).convert("RGBA")

        icon = ctk.CTkImage(
            light_image=image,
            dark_image=image,
            size=(size, size),
        )

        self.cache[key] = icon
        return icon