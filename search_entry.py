import tkinter as tk
import csv

#Make a class for searching info
class search_info(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)

        #create a label for searching infos
        self.search_label=tk.Label(self, text="Search Information", font=("Helvetica", "20"))
        self.search_label.place(x=350, y=50)

        self.name_label=tk.Label(self, text="Please enter the name you want to search", font=("Arial", "12"))
        self.name_label.place(x=30, y=250)
        #create an entry for searching infos
        self.name_entry=tk.Entry(self)
        self.name_entry.place(x=30, y=280, width=250)

        #Create a search button
        self.search_button=tk.Button(self, text="Search", command=self.search)
        self.search_button.place(x=30, y=310)

        #create a canvas for the result
        self.result_canvas=tk.Canvas(self, width=390, height=320, highlightbackground="black")
        self.result_canvas.place(x=450, y=130)
    
    def search(self):
        self.result_canvas.delete()

        name=self.name_entry.get()
        found = False
        with open("information.csv", "r") as file:
            read=csv.reader(file)
            for row in read:
                if len(row) > 0 and row[0] == name:
                    found = True
                    result = f"{row[0]}"
                    self.result_canvas.create_text(10, 10, anchor="nw", text=result, font=("Arial", 10), fill="black")
                    break
        
        if not found:
            self.result_canvas.create_text(10, 10, anchor="nw", text="Sorry, the name does not exist", font=("Arial", 11))
        