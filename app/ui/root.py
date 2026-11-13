import customtkinter as ctk
from app.ui.theme.manager import ThemeManager,IconManager
from app.ui.ui_utility.functions import center_window
from app.ui.window.HomeWindow.hw_manager import HomeWindowManager
from app.ui.window.WorkFlowWindow.wfw_manager import WorkflowWindowManager



class MainWindow():

    def __init__(self):

        self.tmn = ThemeManager()
        self.imn = IconManager()
        
        self.bg = self.tmn.get("bg")
        self.root = ctk.CTk()
        self.root.geometry(center_window(self.root,1000,590))
        self.root.resizable(0,0)
        self.root.title("BrewOS")
        self.root.config(bg=self.bg)

        self.hwm = HomeWindowManager(self.root,self.load_manager)
        # self.wfwm = WorkflowWindowManager(self.root,self.load_manager)
       


    



    def load_manager(self):
        print('here')









    def update(self):
        self.root.mainloop()


    