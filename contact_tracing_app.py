import tkinter as tk
import csv
from add_function import add_info
from search_entry import search_info
class front_page():
    def __init__(self):
        #Make the title window and size
        self.front = tk.Tk()
        self.front.title("Covid Tracing app")
        self.front.geometry("900x500")

        #add button for adding and searching entries
        add_button = tk.Button(self.front, text="Add Information", command=front_page.add_entries)
        add_button.place(x=405, y=170)

        search_button = tk.Button(self.front, text="Search Information", command=front_page.search_entries)
        search_button.place(x=401, y=210)

    #create the function for the add button
    def add_entries():
        info = add_info()
        info.place(x=0, y=0, relwidth=1, relheight=1)
    
    def search_entries():
        search = search_info()
        search.place(x=0, y=0, relwidth=1, relheight=1)
    
    def run(self):
        #Start the main loop
        self.front.mainloop()
        
#Call the function
if __name__=="__main__":
    app = front_page()
    app.run()
