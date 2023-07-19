import tkinter as tk
import csv
class add_info(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        # Create a label
        self.header1=tk.Label(self, text="Respondent's Details", font=("Arial", 10))
        self.header1.place(x=20, y=20)

        self.header2=tk.Label(self, text="Contact Person's Details", font=("Arial", 10))
        self.header2.place(x=350, y=20)

        #Label for name
        self.name = tk.Label(self, text = "Full Name")
        self.name.place(x=20, y=50)
        #Entry for name
        self.name_entry = tk.Entry(self, width=40)
        self.name_entry.place(x=85, y=50)

        #Label for phone number
        self.phone_number = tk.Label(self, text = "Phone Number")
        self.phone_number.place(x=20, y=80)
        #Entry for number
        self.number_entry = tk.Entry(self, width=36)
        self.number_entry.place(x=110, y=80)

        #Label for email
        self.email = tk.Label(self, text = "Email")
        self.email.place(x=20, y=110)
        #Entry for email
        self.email_entry = tk.Entry(self, width=44)
        self.email_entry.place(x=60, y=110)

        #Label for contact person
        self.contact_person = tk.Label(self, text = "Full Name")
        self.contact_person.place(x=350, y=50)
        #Entry for contact person
        self.contact_person_entry = tk.Entry(self, width=29)
        self.contact_person_entry.place(x=415, y=50)

        #Label for email of contact person
        self.email_contact_person=tk.Label(self, text="Email")
        self.email_contact_person.place(x=600, y=50)
        #Entry for email of contact person
        self.email_contact_person_entry=tk.Entry(self, width=35)
        self.email_contact_person_entry.place(x=640, y=50)

        #Relationship to the respondent
        self.relationship=tk.Label(self, text="Relationship")
        self.relationship.place(x=350, y=80)
        #Entry for relationship
        self.relationship_entry=tk.Entry(self, width=27)
        self.relationship_entry.place(x=425, y=80)

        #Contact number of contact person
        self.person_number=tk.Label(self, text="Phone Number")
        self.person_number.place(x=600, y=80)
        #Entry for number of contact person
        self.person_number_entry=tk.Entry(self, width=27)
        self.person_number_entry.place(x=690, y=80)
        #Label for date
        self.date = tk.Label(self, text = "Date of visit")
        self.date.place(x=350, y=110)
        #Entry for date
        self.date_entry = tk.Entry(self, width=39)
        self.date_entry.place(x=425, y=110)

        #Button for submit
        self.submit_button = tk.Button(self, text="Submit", command=self.write)
        self.submit_button.place(x=225, y=200)
    
    def write(self):
        name = self.name_entry.get()
        number = self.number_entry.get()
        email = self.email_entry.get()
        contact_person = self.contact_person_entry.get()
        date = self.date_entry.get()

        with open("information.csv", "a") as file:
            file.write(f"Full Name: {name}\n")
            file.write(f"Phone Number:{number}\n")
            file.write(f"Temperature: {email}\n")
            file.write(f"Location of visit: {contact_person}\n")
            file.write(f"Date of visit: {date}\n")

    
