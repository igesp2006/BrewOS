''' module for widget animation by altering place() of widgets '''

import customtkinter as ctk



def hex_to_rgb(hex_color: str) -> tuple:

    '''converts a hex color string to an (r, g, b) tuple'''

    hex_color = hex_color.lstrip('#')

    red_hex = hex_color[0:2]
    green_hex = hex_color[2:4]
    blue_hex = hex_color[4:6]

    red = int(red_hex, 16)
    green = int(green_hex, 16)
    blue = int(blue_hex, 16)

    return (red, green, blue)


