import tkinter as tk
import csv

#Make a class for searching info
class search_info(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)

        #create a label for searching infos
        self.search_label=tk.Label(self, text="Search Information", font=("Helvetica", "14"))
        self.search_label.place(x=375, y=150)

        self.name_label=tk.Label(self, text="Please enter the name you want to search", font=("Arial", "10"))
        self.name_label.place(x=335, y=200)
        #create an entry for searching infos
        