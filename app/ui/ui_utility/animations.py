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




def fade_in(window: ctk.CTk, widget: ctk.CTkBaseClass, step, total_steps, x_coord, y_coord, bg_hex, target_hex, callback=lambda: None):

    '''creates a simple fade in animation for a button by altering the background color'''

    if step > total_steps:
        callback()                      # callback to continue flow if required
        return

    bg_rgb = hex_to_rgb(bg_hex)
    target_rgb = hex_to_rgb(target_hex)

    progress = step / total_steps
    eased = 1 - (1 - progress) ** 3

    r = int(bg_rgb[0] + (target_rgb[0] - bg_rgb[0]) * eased)
    g = int(bg_rgb[1] + (target_rgb[1] - bg_rgb[1]) * eased)
    b = int(bg_rgb[2] + (target_rgb[2] - bg_rgb[2]) * eased)
    fade_color = f'#{r:02x}{g:02x}{b:02x}'

    widget.place(x=x_coord, y=y_coord)
    widget.configure(fg_color=fade_color)

    window.after(16, lambda: fade_in(window, widget, step + 1, total_steps, x_coord, y_coord, bg_hex, target_hex, callback))


#################################


def slide(window: ctk.CTk, widget: ctk.CTkBaseClass, step, total_steps, start_x, target_x, start_y, target_y, bg_hex=None, target_hex=None, callback=lambda: None):

    '''creates a simple slide animation for the label with progressive gradient color smoothing'''

    if step > total_steps:
        callback()                      # callback to continue flow if required
        return

    progress = step / total_steps
    eased = 1 - (1 - progress) ** 3
    

    if bg_hex and target_hex is not None:

        bg_rgb = hex_to_rgb(bg_hex)
        target_rgb = hex_to_rgb(target_hex)


        # fade
        r = int(bg_rgb[0] + (target_rgb[0] - bg_rgb[0]) * progress)
        g = int(bg_rgb[1] + (target_rgb[1] - bg_rgb[1]) * progress)
        b = int(bg_rgb[2] + (target_rgb[2] - bg_rgb[2]) * progress)
        
        widget.configure(text_color=f'#{r:02x}{g:02x}{b:02x}')



    # slide
    current_y = start_y + (target_y - start_y) * eased
    current_x = start_x + (target_x - start_x) * eased
    widget.place(x=current_x, y=current_y)

  
    window.after(16, lambda: slide(window, widget, step + 1, total_steps, start_x, target_x, start_y, target_y, bg_hex, target_hex, callback))