from app.ui.theme.pallets import PALETTES, DEFAULT_PALETTE

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
