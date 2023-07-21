import tkinter as tk

#create a class for closing message
class Closing(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)

        message=tk.Label(self, text="Your information has been submitted successfully!!!\n Keep safe")