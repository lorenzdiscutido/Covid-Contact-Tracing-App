import tkinter as tk

# Create the main window
top = tk.Tk()
top.title("Covid Tracing App")
top.geometry("500x300")
# Create a label
name = tk.Label(top, text = "Full Name:")
name.place(x=50, y=50)
phone_number = tk.Label(top, text = "Phone Number:")
phone_number.place(x=50, y=70)
temperature = tk.Label(top, text = "Enter your temperature:")
temperature.place(x=50, y=90)
location = tk.Label(top, text = "Location of your visit:")
date = tk.Label(top, text = "Date of your visit:")
# Create an entry field
# Create a button
# Start the main event loop
top.mainloop()
