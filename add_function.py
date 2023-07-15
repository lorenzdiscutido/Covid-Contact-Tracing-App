import tkinter as tk

class add_info():
    def __init__(self, master=None):
        # Create a label
        name = tk.Label(self, text = "Full Name:")
        name.place(x=50, y=50)

        phone_number = tk.Label(self, text = "Phone Number:")
        phone_number.place(x=50, y=80)

        temperature = tk.Label(self, text = "Enter your temperature:")
        temperature.place(x=50, y=110)

        location = tk.Label(self, text = "Location of your visit:")
        location.place(x=50, y=140)

        date = tk.Label(self, text = "Date of your visit(MM/DD/YY):")
        date.place(x=50, y=170)

        # Create an entry field
        name_entry = tk.Entry(self)
        name_entry.place(x=120, y=50)

        number_entry = tk.Entry(self)
        number_entry.place(x=150, y=80)

        temp_entry = tk.Entry(self)
        temp_entry.place(x=190, y=110)

        location_entry = tk.Entry(self)
        location_entry.place(x=180, y=140)

        date_entry = tk.Entry(self)
        date_entry.place(x=225, y=170)
        # Create a button
        # Start the main event loop
        self.mainloop()
