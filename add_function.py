import tkinter as tk
import csv
from tkinter import messagebox
class add_info(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        # Create a label
        self.header1=tk.Label(self, text="Respondent's Details", font=("Arial", 10))
        self.header1.place(x=20, y=20)

        self.header2=tk.Label(self, text="Contact Person's Details", font=("Arial", 10))
        self.header2.place(x=350, y=20)

        self.header3=tk.Label(self, text="Additional informations required", font=("Arial", 15))
        self.header3.place(x=20, y=150)

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

        #Create a choice variable for vaccination status
        self.vaccination_choice=tk.StringVar()

        #Ask the respondent for vaccination status
        self.vaccination_status=tk.Label(self, text="What is your vaccination status?")
        self.vaccination_status.place(x=20, y=180)
        #choice1
        self.vacinnation_choice1_radio=tk.Radiobutton(self, text="Not yet", variable=self.vaccination_choice, value="0")
        self.vacinnation_choice1_radio.place(x=20, y=200)
        #choice2
        self.vacinnation_choice2_radio=tk.Radiobutton(self, text="1st Dose", variable=self.vaccination_choice, value="1")
        self.vacinnation_choice2_radio.place(x=20, y=220)
        #choice3
        self.vacinnation_choice3_radio=tk.Radiobutton(self, text="2nd Dose", variable=self.vaccination_choice, value="2")
        self.vacinnation_choice3_radio.place(x=20, y=240)
        #choice4
        self.vacinnation_choice4_radio=tk.Radiobutton(self, text="1st Booster Shot", variable=self.vaccination_choice, value="3")
        self.vacinnation_choice4_radio.place(x=20, y=260)
        #choice5
        self.vacinnation_choice5_radio=tk.Radiobutton(self, text="2nd Booster Shot", variable=self.vaccination_choice, value="4")
        self.vacinnation_choice5_radio.place(x=20, y=280)
        
        #create a variable for exposure
        self.exposure_choice=tk.StringVar()
        self.exposure_question=tk.Label(self, text="Have you had exposure to a probable or confirmed case in the last 14 days?")
        self.exposure_question.place(x=20, y=300)

        #choices for exposure
        self.exposure_yes=tk.Radiobutton(self, text="Yes", variable=self.exposure_choice, value="Yes")
        self.exposure_yes.place(x=20, y=320)
        self.exposure_no=tk.Radiobutton(self, text="No", variable=self.exposure_choice, value="No")
        self.exposure_no.place(x=20, y=340)

        #Create variable for symptom contact
        self.symptom_contact_choice=tk.StringVar()
        self.symptom_question=tk.Label(self, text="Have you had in contact with somebody with covid symptoms in the past 7 days?")
        self.symptom_question.place(x=200, y=180)

        #create choices for symptom contact
        self.symptom_contact_yes=tk.Radiobutton(self, text="Yes", variable=self.symptom_contact_choice, value="Yes")
        self.symptom_contact_yes.place(x=200, y=200)
        self.symptom_contact_no=tk.Radiobutton(self, text="No", variable=self.symptom_contact_choice, value="No")
        self.symptom_contact_no.place(x=200, y=220)

        #create a variable for covid testing
        self.test=tk.StringVar()
        self.tested=tk.Label(self, text="Have you been tested for Covid-19 \n in the last 14 days?")
        self.tested.place(x=650, y=180)

        #create choice for testing
        self.tested_yes=tk.Radiobutton(self, text="Yes", variable=self.test, value="Yes")
        self.tested_yes.place(x=650, y=210)
        self.tested_no=tk.Radiobutton(self, text="No", variable=self.test, value="No")
        self.tested_no.place(x=650, y=230)
        #Button for submit
        self.submit_button = tk.Button(self, text="Submit", command=self.write)
        self.submit_button.place(x=420, y=450)
    
    def write(self):
        name = self.name_entry.get()
        number = self.number_entry.get()
        email = self.email_entry.get()
        contact_person = self.contact_person_entry.get()
        contact_person_email= self.email_contact_person_entry.get()
        contact_person_number = self.person_number_entry.get()
        date = self.date_entry.get()
        Relation = self.relationship_entry.get()

        with open("information.csv", "a") as file:
            file.write(f"Full Name: {name}\n")
            file.write(f"Phone Number:{number}\n")
            file.write(f"Temperature: {email}\n")
            file.write(f"Location of visit: {contact_person}\n")
            file.write(f"Date of visit: {date}\n")
            file.write(f"Contact Person Email: {contact_person_email}\n")
            file.write(f"Relationship: {Relation}\n")
            file.write(f"Contact Person's Number: {contact_person_number}\n")
        
    def closing(self):
        close=add_info.write()
        close.place(x=0, y=0, relwidth=1, relheight=1)

    
