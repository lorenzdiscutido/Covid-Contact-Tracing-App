import tkinter as tk
import csv
from add_function import add_info

class front_page():
    def __init__(self):
        #Make the title window and size
        self.front = tk.Tk()
        self.front.title("Covid Tracing app")
        self.front.geometry("900x500")

        #add button for adding and searching entries
        add_button = tk.Button(self.front, text="Add", command=front_page.add_entries)
        add_button.place(x=425, y=170)

        search_button = tk.Button(self.front, text="Search")
        search_button.place(x=421, y=200)

    #create the function for the add button
    def add_entries():
        info = add_info()
        info.place(x=0, y=0, relwidth=1, relheight=1)
    
    
    def run(self):
        #Start the main loop
        self.front.mainloop()
        
#Call the function
if __name__=="__main__":
    app = front_page()
    app.run()
