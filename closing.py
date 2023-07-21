import tkinter as tk

#create a class for closing message
class Closing(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)

        message=tk.Label(self, text="Your information has been submitted successfully!!!\n Keep safe", font=("Helvetica","20"))
        message.place(x=0, y=0, relheight=1, relwidth=1)

        exit_button=tk.Button(self, text="exit", command=self.exit)
        exit_button.place(x=450, y=300)

        back_button=tk.Button(self, text="Back to menu")
        back_button.place(x=423, y=330)
    
    def exit(self):
        self.master.destroy()