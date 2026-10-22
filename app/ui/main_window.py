import customtkinter as ctk


class MainWindow():

    def __init__(self):

        self.root = ctk.CTk()
        self.root.geometry('1330x790')
        self.root.resizable(1,1)
        self.root.title("BrewOS")


    def update(self):
        self.root.mainloop()


    