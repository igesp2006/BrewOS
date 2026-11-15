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

        self.wfwm = WorkflowWindowManager(self.root,self.load_manager)
        self.hwm = HomeWindowManager(self.root,self.load_manager)
       
        self.managers = {'wfwm':self.wfwm,
                         'hwm':self.hwm}

    



    def load_manager(self,load_manager:ctk.CTkFrame):

        i:ctk.CTkFrame
        for i in self.managers.values():
            i.place_forget()


        self.managers[load_manager].place(x=0,y=0)
        
            
      
    


    def update(self):
        self.root.mainloop()


    