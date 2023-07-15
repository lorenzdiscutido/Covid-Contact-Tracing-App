import tkinter as tk

class add_info(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        # Create a label
        self.name = tk.Label(self, text = "Full Name:")
        self.name.place(x=50, y=50)

        self.phone_number = tk.Label(self, text = "Phone Number:")
        self.phone_number.place(x=50, y=80)

        self.temperature = tk.Label(self, text = "Enter your temperature:")
        self.temperature.place(x=50, y=110)

        self.location = tk.Label(self, text = "Location of your visit:")
        self.location.place(x=50, y=140)

        self.date = tk.Label(self, text = "Date of your visit(MM/DD/YY):")
        self.date.place(x=50, y=170)

        # Create an entry field
        self.name_entry = tk.Entry(self)
        self.name_entry.place(x=120, y=50)

        self.number_entry = tk.Entry(self)
        self.number_entry.place(x=150, y=80)

        self.temp_entry = tk.Entry(self)
        self.temp_entry.place(x=190, y=110)

        self.location_entry = tk.Entry(self)
        self.location_entry.place(x=180, y=140)

        self.date_entry = tk.Entry(self)
        self.date_entry.place(x=225, y=170)