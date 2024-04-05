
import tkinter as tk
from tkinter import Entry, Button, Label, font, PhotoImage, messagebox
from PIL import Image, ImageTk
from tkinter import ttk
from datetime import datetime
import mysql.connector
def _init_(self):
    self.root = tk.Tk()
    self.root.title("LOGIN")

    # Load the background image using Pillow
    i1 = Image.open('logo4.jpeg')
    i1 = ImageTk.PhotoImage(i1)

    # Create a custom font
    custom_font = font.Font(family="Times New Roman", size=26, weight=font.BOLD)

    # Place the background image
    background_label = Label(self.root, image=i1)

    self.label1 = Label(self.root, text="Name", font=custom_font, background='#EFDABB', foreground="#e7753f")
    self.label1.place(x=465, y=230, width=150, height=30)

    self.tx1 = Entry(self.root, font=custom_font, foreground="#05001e", background="#fff1d7")
    self.tx1.place(x=360, y=270, width=300, height=40)

    self.label2 = Label(self.root, text="Password", font=custom_font, background='#EFDABB', foreground="#e7753f")
    self.label2.place(x=460, y=330, width=200, height=30)

    self.tx2 = Entry(self.root, show='*', font=custom_font, foreground="#05001e", background="#fff1d7")
    self.tx2.place(x=360, y=380, width=300, height=40)

    self.button1 = Button(self.root, text="Login", font=custom_font, background="#e7753f", foreground="#05001e",
                          command=self.login_action)
    self.button1.place(x=460, y=440, width=100, height=40)

    self.root.geometry("1010x630")

    # MySQL Database Connection

    self.db = mysql.connector.connect(
        host="@localhost",
        user="root",
        password="Vamshi@51124",
        database="pympr"
    )

    self.cursor = self.db.cursor()
    self.root.mainloop()
