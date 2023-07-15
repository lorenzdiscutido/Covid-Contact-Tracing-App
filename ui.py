import tkinter as tk

# Create the main window
info = tk.Tk()
info.title("Covid Tracing App")
info.geometry("500x300")
# Create a label
name = tk.Label(info, text = "Full Name:")
name.place(x=50, y=50)
phone_number = tk.Label(info, text = "Phone Number:")
phone_number.place(x=50, y=70)
temperature = tk.Label(info, text = "Enter your temperature:")
temperature.place(x=50, y=90)
location = tk.Label(info, text = "Location of your visit:")
location.place(x=50, y=110)
date = tk.Label(info, text = "Date of your visit:")
date.place(x=50, y=130)
# Create an entry field
# Create a button
# Start the main event loop
info.mainloop()
