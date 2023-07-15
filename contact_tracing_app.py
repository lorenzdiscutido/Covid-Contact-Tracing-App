import tkinter as tk
from add_function import add_info

class front_page(add_info):
    def __init__(self):
        #Make the title window and size
        self.front = tk.Tk()
        self.front.title("Covid Tracing app")
        self.front.geometry("500x300")

        #add button for adding and searching entries
        add_button = tk.Button(self.front, text="Add")
        add_button.place(x=0, y=0)
        #Start the main loop
        self.front.mainloop()

#Call the function
if __name__=="__main__":
    app = front_page()
    app.run()
