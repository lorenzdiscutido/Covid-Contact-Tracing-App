import tkinter as tk

# Create the main window
info = tk.Tk()
info.title("Covid Tracing App")
info.geometry("500x300")
# Create a label
name = tk.Label(info, text = "Full Name:")
name.place(x=50, y=50)

phone_number = tk.Label(info, text = "Phone Number:")
phone_number.place(x=50, y=80)

temperature = tk.Label(info, text = "Enter your temperature:")
temperature.place(x=50, y=110)

location = tk.Label(info, text = "Location of your visit:")
location.place(x=50, y=140)

date = tk.Label(info, text = "Date of your visit(MM/DD/YY):")
date.place(x=50, y=170)

# Create an entry field
name_entry = tk.Entry(info)
name_entry.place(x=120, y=50)

number_entry = tk.Entry(info)
number_entry.place(x=150, y=80)

temp_entry = tk.Entry(info)
temp_entry.place(x=190, y=110)

location_entry = tk.Entry(info)
location_entry.place(x=180, y=140)

date_entry = tk.Entry(info)
date_entry.place(x=225, y=170)
# Create a button
# Start the main event loop
info.mainloop()
