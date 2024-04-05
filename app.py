import tkinter as tk
from tkinter import Entry, Button, Label, font, PhotoImage, messagebox, ttk
from PIL import Image, ImageTk
import mysql.connector
# import fitz  # PyMuPDF library
from io import BytesIO
from datetime import datetime
import os
import subprocess
from subprocess import call



class MainMenu:
    def __init__(self):
        self.root_menu = tk.Tk()
        self.root_menu.title("Main Menu")

        custom_font = font.Font(family="HK Grotesk", size=13, weight=font.BOLD)

        # Load the background image using Pillow
        background_image = Image.open('1.png')  # Replace 'background_image.png' with your image file
        background_image = ImageTk.PhotoImage(background_image)

        # Create a label to hold the background image
        background_label = tk.Label(self.root_menu, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Set a reference to the image to prevent garbage collection
        background_label.image = background_image

        # Add buttons to navigate to different pages
        self.button_login = Button(self.root_menu, text="Login", font=custom_font, background="#4628e7",
                                   foreground="#ECE9FC", command=self.open_login_page)
        self.button_login.place(x=760, y=430, width=120, height=40)

        # theory syllabus

        self.button1 = Button(self.root_menu, text="MATHS", font=custom_font, background='#5943F4',
                              foreground="#FFFFFF", borderwidth=0, highlightthickness=0, command=self.open_pdf_maths)
        self.button1.place(x=160, y=105, width=150, height=25)

        self.button1 = Button(self.root_menu, text="COA", font=custom_font, background="#5943F4", foreground="#FFFFFF",
                              borderwidth=0, highlightthickness=0, command=self.open_pdf_coa)
        self.button1.place(x=160, y=145, width=150, height=25)

        self.button1 = Button(self.root_menu, text="AT", font=custom_font, background="#5943F4", foreground="#FFFFFF",
                              borderwidth=0, highlightthickness=0, command=self.open_pdf_at)
        self.button1.place(x=160, y=185, width=150, height=25)

        self.button1 = Button(self.root_menu, text="OS", font=custom_font, background="#5943F4", foreground="#FFFFFF",
                              borderwidth=0, highlightthickness=0, command=self.open_pdf_os)
        self.button1.place(x=160, y=225, width=150, height=25)

        self.button1 = Button(self.root_menu, text="CNND", font=custom_font, background="#5943F4", foreground="#FFFFFF",
                              borderwidth=0, highlightthickness=0, command=self.open_pdf_cnnd)
        self.button1.place(x=160, y=265, width=150, height=25)

        # lab syllabus

        self.button2 = Button(self.root_menu, text="NL", font=custom_font, background='#5943F4', foreground="#FFFFFF",
                              borderwidth=0, highlightthickness=0, command=self.open_pdf_nl)
        self.button2.place(x=160, y=420, width=150, height=25)

        self.button2 = Button(self.root_menu, text="MPL", font=custom_font, background="#5943F4", foreground="#FFFFFF",
                              borderwidth=0, highlightthickness=0, command=self.open_pdf_mpl)
        self.button2.place(x=160, y=460, width=150, height=25)

        self.button2 = Button(self.root_menu, text="PYTHON", font=custom_font, background="#5943F4",
                              foreground="#FFFFFF", borderwidth=0, highlightthickness=0, command=self.open_pdf_python)
        self.button2.place(x=160, y=500, width=150, height=25)

        self.button2 = Button(self.root_menu, text="UNIX", font=custom_font, background="#5943F4", foreground="#FFFFFF",
                              borderwidth=0, highlightthickness=0, command=self.open_pdf_unix)
        self.button2.place(x=160, y=540, width=150, height=25)

        # MySQL Database Connection (You may want to move this to a separate module)
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Vamshi@51124",
            database="pympr"
        )

        self.root_menu.geometry("{0}x{1}+0+0".format(1354, 690))
        self.root_menu.mainloop()



    def open_login_page(self):
        self.root_menu.destroy()
        LoginApp()

    # theory

    def open_pdf_maths(self):
        self.open_pdf("MATHS SYLLABUS.pdf")

    def open_pdf_coa(self):
        self.open_pdf("COA SYLLABUS.pdf")

    def open_pdf_at(self):
        self.open_pdf("AT SYLLABUS.pdf")

    def open_pdf_os(self):
        self.open_pdf("OS SYLLABUS.pdf")

    def open_pdf_cnnd(self):
        self.open_pdf("CNND SYLLABUS.pdf")

    # lab

    def open_pdf_nl(self):
        self.open_pdf("NL SYLLABUS.pdf")

    def open_pdf_mpl(self):
        self.open_pdf("MPL SYLLABUS.pdf")

    def open_pdf_python(self):
        self.open_pdf("PYTHON SYLLABUS.pdf")

    def open_pdf_unix(self):
        self.open_pdf("UNIX SYLLABUS.pdf")

    def open_pdf(self, pdf_file):
        if pdf_file:
            try:
                os.startfile(pdf_file)
            except OSError:
                messagebox.showerror("Error", "Failed to open PDF file.")


class LoginApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("LOGIN")

        # Load the background image using Pillow
        i1 = Image.open('2.png')
        i1 = ImageTk.PhotoImage(i1)

        # Create a custom font
        custom_font = font.Font(family="Times New Roman", size=16, weight=font.BOLD)
        custom_font1 = font.Font(family="Times New Roman", size=14, weight=font.BOLD)

        # Place the background image
        background_label = Label(self.root, image=i1)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.tx1 = Entry(self.root, font=custom_font, foreground="#000000", background="#D9D9D9")
        self.tx1.place(x=600, y=300, width=250, height=25)

        self.tx2 = Entry(self.root, show='*', font=custom_font, foreground="#000000", background="#D9D9D9")
        self.tx2.place(x=600, y=370, width=250, height=25)

        self.button1 = Button(self.root, text="Login", font=custom_font1, background="#4628e7", foreground="#ECE9FC",
                              command=self.login_action)
        self.button1.place(x=600, y=465, width=120, height=35)

        self.root.geometry("{0}x{1}+0+0".format(1354, 690))

        # MySQL Database Connection
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Vamshi@51124",
            database="pympr"
        )

        self.cursor = self.db.cursor()

        self.root.mainloop()


    def login_action(self):
        username = self.tx1.get()
        password = self.tx2.get()

        call(["python", "gmail.py"])
        # Check if the provided username and password match any record in the database
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        values = (username, password)

        self.cursor.execute(query, values)
        result = self.cursor.fetchone()

        if result:
            # Successful login
            self.root.destroy()  # Close the current window
            # Open the LectureTypePage
            call(["python", "p4.py"])

        else:
            # Incorrect credentials, display an error message
            print("Invalid username or password")
            messagebox.showerror("Error", "Invalid username or password. Please try again.")




if __name__ == "__main__":
    MainMenu()