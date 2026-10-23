import customtkinter as ctk


def center_window(window:ctk.CTk, width=400, height=300):
    
    '''to centre the gui window and 
        stop the default window placement to 
        top left of the screen'''
    
    
    '''get window dimensions'''
    
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    
    adjustment = 40
    
    x = (screen_width // 2) - (width // 2) - adjustment
    y = (screen_height // 2) - (height // 2) - adjustment
    
    
    ''' Set the geometry string format: "widthxheight+x+y" '''
    return (f"{width}x{height}+{x}+{y}")
