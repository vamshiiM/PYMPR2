import tkinter as tk
import customtkinter
from tkinter import ttk,messagebox
import mysql.connector
from tkinter import Frame
from customtkinter import *
import pyttsx3
from subprocess import call
import openpyxl
from openpyxl import Workbook,load_workbook
import xlsxwriter
from PIL import Image, ImageTk
import subprocess
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
from pyttsx3 import *

app =customtkinter.CTk()
app.geometry("1530x790+0+0")
app.configure(fg_color='#33186B')
#6420AA
# MySQL Configuration
mysql_host = 'localhost'
mysql_user = 'root'
mysql_password = 'Vamshi@51124'
mysql_database = 'pympr'

# Dictionary to store the attendance state of each student
attendance_state = {}
attendance_var={}

font=CTkFont(family= "Work Sans ,sans-serif",
   size=20,
   weight= "bold",)
font2=CTkFont(family= "Open Sans ,sans-serif",
   size=16,
   weight= "bold",)
font3=CTkFont(family= "Work Sans ,sans-serif",
   size=15,
   weight= "normal",)

f1=CTkFrame(app,height=200,width=400,fg_color='#7360DF')
f1.place(relx=0.022,rely=0.03)
f1_1=CTkFrame(app,height=200,width=650,fg_color='#7360DF')
f1_1.place(relx=0.305,rely=0.03)
f1_2=CTkFrame(app,height=200,width=359,fg_color='#7360DF')
f1_2.place(relx=0.75,rely=0.03)
f2= customtkinter.CTkFrame(app,height=530,width=580,fg_color='#7360DF')
f2.place(relx=0.022,rely=0.31)
f3= Frame(app,height=670,width=1080)
f3.place(relx=0.42,rely=0.31)

type=CTkLabel(f1_1,text="LECT TYPE :",font=font)
type.place(relx=0.05,rely=0.2)
subject=CTkLabel(f1_1,text="SUBJECT :",font=font)
subject.place(relx=0.057,rely=0.4)
cl=CTkLabel(f1_1,text="CLASS :",font=font)
cl.place(relx=0.057,rely=0.6)
option=CTkLabel(f1_1,text="BATCH :",font=font)
option.place(relx=0.057,rely=0.8)
entry0=ttk.Combobox(f1_1,state='readonly',width=30,font=font2)#lecture type
entry0['values']=('LECTURE','LAB')
entry0.place(relx=0.29,rely=0.2)
entry1=ttk.Combobox(f1_1,state='readonly',width=30,font=font2)#subject
entry1.config(height=50)
entry1.place(relx=0.29,rely=0.4)
entry5=ttk.Combobox(f1_1,state='readonly',width=30,font=font2)#class
entry5['values'] = ('S2', 'S1')
entry5.place(relx=0.29,rely=0.6)
entry6=ttk.Combobox(f1_1,state='readonly',width=30,font=font2)#Batch
entry6.place(relx=0.29,rely=0.8)
entry7=CTkEntry(f1,placeholder_text="ENTER LECT NO.",width=200,height=40)#lect no
entry7.place(relx=0.25,rely=0.6)
l_2=CTkLabel(f1_2,text="FETCH",font=font)
l_2.place(relx=0.7,rely=0)

date=CTkLabel(f1,text="DATE:",font=font)
date.place(relx=0.05,rely=0.3)
lec=CTkLabel(f1,text="LEC NO:",font=font)
lec.place(relx=0.03,rely=0.6)
entry2=CTkEntry(f1,placeholder_text="DD",width=45,height=40)#day
entry2.place(relx=0.25,rely=0.29)
entry3=CTkEntry(f1,placeholder_text="MM",width=80,height=40)#month
entry3.place(relx=0.38,rely=0.29)
entry4=CTkEntry(f1,placeholder_text="YY",width=60,height=40)#year
entry4.place(relx=0.6,rely=0.29)
l_1=CTkLabel(f1_1,text="LECTURE INFO",font=font)
l_1.place(relx=0.7,rely=0)


atlabel=CTkLabel(f1,text="ATTENDANCE")


def on_focus_in(event):
    if entry5.get() == placeholder_text:
        entry5.set('')
        entry5.config(foreground='black')

def on_focus_out(event):
    if not entry5.get():
        entry5.set(placeholder_text)
        entry5.config(foreground='grey')



# Placeholder text
placeholder_text = "Select CLASS"

# Create Combobox


# Set placeholder text
entry5.set(placeholder_text)
entry5.config(foreground='grey')


def on_focus_in(event):
    if entry0.get() == placeholder_text:
        entry0.set('')
        entry0.config(foreground='black')

def on_focus_out(event):
    if not entry0.get():
        entry0.set(placeholder_text)
        entry0.config(foreground='grey')



# Placeholder text
placeholder_text = "Select TYPE"

# Create Combobox


# Set placeholder text
entry0.set(placeholder_text)
entry0.config(foreground='grey')



def on_focus_in(event):
    if entry1.get() == placeholder_text:
        entry1.set('')
        entry1.config(foreground='black')

def on_focus_out(event):
    if not entry1.get():
        entry1.set(placeholder_text)
        entry1.config(foreground='grey')



# Placeholder text
placeholder_text = "Select SUBJECT"

# Create Combobox


# Set placeholder text
entry1.set(placeholder_text)
entry1.config(foreground='grey')


def on_focus_in(event):
    if entry6.get() == placeholder_text:
        entry6.set('')
        entry6.config(foreground='black')

def on_focus_out(event):
    if not entry6.get():
        entry6.set(placeholder_text)
        entry6.config(foreground='grey')



# Placeholder text
placeholder_text = "Select an option"
placeholder_text2="THIS FIELD IS LOCKED"
# Create Combobox


# Set placeholder text
entry6.set(placeholder_text)
entry6.config(foreground='grey')

def check_fields():
    # Check if any entry field or combobox is left empty
    if not entry0.get():
        messagebox.showerror("Error", "Please select TYPE")
        return False
    elif not entry1.get():
        messagebox.showerror("Error", "Please select SUBJECT")
        return False
    elif not entry2.get():
        messagebox.showerror("Error", "Please enter DAY")
        return False
    elif not entry3.get():
        messagebox.showerror("Error", "Please enter MONTH")
        return False
    elif not entry4.get():
        messagebox.showerror("Error", "Please enter YEAR")
        return False
    elif not entry5.get():
        messagebox.showerror("Error", "Please select CLASS")
        return False
    elif not entry6.get():
        messagebox.showerror("Error", "Please select an option")
        return False
    elif not entry7.get():
        messagebox.showerror("Error", "Please enter lecture number")
        return False
    else:
        return True





def update_options(*args):
    # Clear previous options
    entry6['values'] = ()
    e0=entry0.get()

    # Determine options for second ComboBox based on the selection in the first ComboBox
    selected_item = entry5.get()
    if selected_item == 'S1':
        entry6['values'] = ('S11', 'S12', 'S13','none')

    elif selected_item == 'S2':
        entry6['values'] = ('S21', 'S22', 'S23','none')





def update_options2(*args):
    # Clear previous options
    entry1['values'] = ()

    # Determine options for second ComboBox based on the selection in the first ComboBox
    e0 = entry0.get()
    if e0 == 'LECTURE':
        entry1['values'] = ('AT', 'OS', 'CN', 'COA','MATHS')
        entry6.config(state='disabled')
        entry6.set(placeholder_text2)
        entry6.configure(foreground="red")
    elif e0 =='LAB':
        entry6.config(state='normal')  # To re-enable if needed
        entry1['values'] = ('PYTHON', 'UNIX', 'NL', 'MPL')




style=ttk.Style(f3)
style.theme_use("clam")
style.configure("Treeview",
                background="#0D9276",
                rowheight=50,
                )
style.configure(".",font=('Helvetica',14))
style.configure("Treeview.Heading",foreground="#33186B",font=('Helvetica',11,"bold"))




students_tree = ttk.Treeview(f3)
students_tree["columns"] = ("SR","ROLL_NO","NAME","BATCH", "Attendance")

students_tree['show']=('headings')
students_tree.column("SR", width=100, anchor=tk.CENTER)
students_tree.column("ROLL_NO", width=150, anchor=tk.CENTER)
students_tree.column("NAME", width=400, anchor=tk.CENTER)
students_tree.column("BATCH", width=200, anchor=tk.CENTER)
students_tree.column("Attendance", width=300, anchor=tk.CENTER)

students_tree.heading("SR", text="SR_NO.")
students_tree.heading("ROLL_NO", text="ROLL_NO")
students_tree.heading("NAME", text="NAME")
students_tree.heading("BATCH", text="BATCH")
students_tree.heading("Attendance", text="ATTENDANCE")
students_tree.place(relx=0.0,rely=-0.0005,height=700)

def open_file():
    call(["python","p.py"])





def fetch_students():

    e6=entry6.get()
    e5=entry5.get()
    e0=entry0.get()
    # Connect to MySQL
    tf.delete(0, tk.END)
    conn = mysql.connector.connect(
        host=mysql_host,
        user=mysql_user,
        password=mysql_password,
        database=mysql_database
    )
    cursor = conn.cursor()

    # Fetch student data

    if e5=='S2' and e0=='LECTURE':
        cursor.execute("SELECT * FROM S2")
    elif e5=='S2' and e6=='S21':
        cursor.execute("SELECT * FROM S2 where Batch ='S21'")
    elif e5=='S2' and e6=='S22':
        cursor.execute("SELECT * FROM S2 where Batch ='S22'")
    elif e5=='S2' and e6=='S23':
        cursor.execute("SELECT * FROM S2 where Batch ='S23'")
    elif e5=='S1'  and e0=='LECTURE':
        cursor.execute("SELECT * FROM S1 ")
    elif e5=='S1' and e6=='S11':
        cursor.execute("SELECT * FROM S1 where Batch ='S11'")
    elif e5=='S1' and e6=='S12':
        cursor.execute("SELECT * FROM S1 where Batch ='S12'")
    elif e5=='S1' and e6=='S13':
        cursor.execute("SELECT * FROM S1 where Batch ='S13'")


    students_data = cursor.fetchall()
    # Display students in Tkinter window
    display_students(students_data)

    # Close connection
    cursor.close()
    conn.close()




def display_students(students_data):
    # Clear previous data
    for row in students_tree.get_children():
        students_tree.delete(row)

    # Display student data
    for student in students_data:
        id=student[0]
        roll_no = student[1]
        student_name = student[2]  # Assuming name is in the second column
        batch=student[3]# Assuming roll no is in the third column

        # Check if student_name already exists in attendance_state, if not add it with "present" state
        if student_name not in attendance_state:
            attendance_state[student_name] = "PRESENT"

        students_tree.insert('', 'end', values=(id,roll_no,student_name,batch, attendance_state[student_name]))

def on_double_click(event):
    # selected_item = students_tree.selection()
    # if selected_item:
    #     id = students_tree.item(selected_item)['values'][0]
    #     roll_no = students_tree.item(selected_item)['values'][1]
    #     student_name = students_tree.item(selected_item)['values'][2]
    #     email = students_tree.item(selected_item)['values'][3]
    #     phone = students_tree.item(selected_item)['values'][4]
    #     dep = students_tree.item(selected_item)['values'][5]
    #     sem = students_tree.item(selected_item)['values'][6]
    #
    #     current_state = attendance_state.get(student_name, "PRESENT")
    #     new_state = "PRESENT" if current_state == "ABSENT" else "ABSENT"
    #     print(f"{student_name} is marked {new_state}")
    #     students_tree.item(selected_item, values=(id,roll_no,student_name,
    #                                               email,phone,dep,sem, new_state))
    #     attendance_state[student_name] = new_state
    #
    #     students_tree.tag_configure(new_state, background='green')

    item = students_tree.identify('item', event.x, event.y)
    if item:
                roll_no = students_tree.set(item, "ROLL_NO")
                current_roll_nos = tf.get().split(',')
                if roll_no in current_roll_nos:
                    # Remove the roll number from the entry field
                    current_roll_nos.remove(roll_no)
                    new_roll_nos = ','.join(current_roll_nos)
                    tf.delete(0, tk.END)
                    tf.insert(tk.END, new_roll_nos)
                    # Set attendance value to default ("PRESENT")
                    students_tree.set(item, "Attendance", "PRESENT")
                    students_tree.item(item, tags=())
                    print(f"{roll_no} is marked PRESENT")
                else:
                    cr_no= tf.get()# Add the roll number to the entry field
                    if not cr_no:
                        tf.insert(tk.END, roll_no)
                    else:
                        tf.insert(tk.END, f",{roll_no}")
                    # Set attendance value to "ABSENT"
                    students_tree.set(item, "Attendance", "ABSENT")
                    students_tree.item(item, tags=('highlighted',))
                    print(f"{roll_no} is marked ABSENT")


        # students_tree.tag_configure(new_state, background='red')
# def highlight_row(event=None):
#     # Get the roll numbers entered in the entry field
#     roll_nos = tf.get().split(',')
#
#     # Clear any existing selection in the treeview
#     students_tree.selection_remove(students_tree.selection())
#
#     # Iterate through all items in the treeview
#     for item in students_tree.get_children():
#         values = students_tree.item(item)['values']
#         if values and str(values[1]) in roll_nos:  # Check if roll number matches any of the entered roll numbers
#             # Highlight the row by changing its background color to red
#             students_tree.selection_add(item)
#             students_tree.focus(item)
#             students_tree.see(item)
#             students_tree.item(item, tags=('highlighted',))
#             students_tree.set(item, "Attendance", "ABSENT")
#             # print(f"{roll_no} is marked PRESENT")# Change attendance to "ABSENT"
#         else:
#             # Reset the background color of other rows
#             students_tree.item(item, tags=())
#             students_tree.set(item, "Attendance", "PRESENT")
#             # print(f"{roll_no} is marked ABSENT")

def highlight_row(event=None):
    # Get the roll numbers entered in the entry field
    roll_nos = tf.get().split(',')

    # Clear any existing selection in the treeview
    students_tree.selection_remove(students_tree.selection())

    # Iterate through all items in the treeview
    for item in students_tree.get_children():
        values = students_tree.item(item)['values']
        roll_no = values[1] if values else None
        if roll_no and str(roll_no) in roll_nos:  # Check if roll number matches any of the entered roll numbers
            # Highlight the row by changing its background color to red
            students_tree.selection_add(item)
            students_tree.focus(item)
            students_tree.see(item)
            students_tree.item(item, tags=('highlighted',))
            students_tree.set(item, "Attendance", "ABSENT")
            print(f"{roll_no} is marked ABSENT")
        else:
            # Reset the background color of other rows
            students_tree.item(item, tags=())
            students_tree.set(item, "Attendance", "PRESENT")
            print(f"{roll_no} is marked PRESENT")


text_speech = pyttsx3.init()
def speak_text(event=None):
    text = tf.get()
    text_speech.say(text)
    text_speech.runAndWait()
    #parts = text.split(',')  # Split the text by commas
    # for part in parts:
    #     text_speech.say(part.strip())  # Read each part separately after removing leading and trailing whitespaces
    #     text_speech.runAndWait()


def sub():
   if check_fields():

    day = entry2.get()
    mon = entry3.get()
    year = entry4.get()
    lec_no = entry7.get()
    column_name= "Date_"+day+"_" + mon + "_" + year + "_" + lec_no + ""
    e0 = entry0.get()
    e1 = entry1.get()
    e5 = entry5.get()
    e6 = entry6.get()

    conn = mysql.connector.connect(
        host=mysql_host,
        user=mysql_user,
        password=mysql_password,
        database=mysql_database
    )
    cursor = conn.cursor()

    # Fetch student data


    attendance_column = [1 if students_tree.item(item)['values'][4] == "PRESENT" else 0 for item in
                         students_tree.get_children()]
    if e5=='S2'and e1=='AT':
        cursor.execute("ALTER TABLE lect_s2at ADD COLUMN " + column_name + " INT(10)")
        print("HEMLO")
    elif e5=='S2'and  e1=='OS':
        cursor.execute("ALTER TABLE lect_s2os ADD COLUMN " + column_name + " INT(10)")
        print("HEMLO")
    elif e5=='S2'and  e1=='CN':
        cursor.execute("ALTER TABLE lect_s2cn ADD COLUMN " + column_name + " INT(10)")
        print("HEMLO")
    elif e5=='S2'and  e1=='COA':
        cursor.execute("ALTER TABLE lect_s2coa ADD COLUMN " + column_name + " INT(10)")
        print("HEMLO")
    elif e5=='S2'and  e1=='MATHS':
        cursor.execute("ALTER TABLE lect_s2am ADD COLUMN " + column_name + " INT(10)")
        print("HEMLO")
    elif e6 == 'S21' and e1 =='PYTHON':
        cursor.execute("ALTER TABLE labS21_py ADD COLUMN " + column_name + " INT(10)")
        print("heheheh")
    elif e6 == 'S21' and e1 == 'UNIX':
        cursor.execute("ALTER TABLE labs21_unix ADD COLUMN " + column_name + " INT(10)")
        print("heheheh")
    elif e6 == 'S21' and e1 =='NL':
        cursor.execute("ALTER TABLE labs21_nl ADD COLUMN " + column_name + " INT(10)")
        print("heheheh")
    elif e6 == 'S21' and e1 =='MPL':
        cursor.execute("ALTER TABLE labs21_mpl ADD COLUMN " + column_name + " INT(10)")
        print("heheheh")
    elif e6 == 'S22' and e1 == 'PYTHON':
        cursor.execute("ALTER TABLE labsS22_py ADD COLUMN " + column_name + " INT(10)")
        print("heheheh")
    elif e6 == 'S22' and e1 == 'UNIX':
        cursor.execute("ALTER TABLE labs22_unix ADD COLUMN " + column_name + " INT(10)")
        print("hehheh")
    elif e6 == 'S22' and e1 == 'NL':
        cursor.execute("ALTER TABLE labs22_nl ADD COLUMN " + column_name + " INT(10)")
        print("heheheh")
    elif e6 == 'S22' and e1 == 'MPL':
        cursor.execute("ALTER TABLE labS22_mpl ADD COLUMN " + column_name + " INT(10)")
        print("heheheh")
    elif e6 == 'S23' and e1 == 'PYTHON':
        cursor.execute("ALTER TABLE labs23_py ADD COLUMN " + column_name + " INT(10)")
        print("heheheh")
    elif e6 == 'S23' and e1 == 'UNIX':
        cursor.execute("ALTER TABLE labs23_unix ADD COLUMN " + column_name + " INT(10)")
        print("heheheh")
    elif e6 == 'S23' and e1 == 'NL':
        cursor.execute("ALTER TABLE labs23_nl ADD COLUMN " + column_name + " INT(10)")
        print("heheheh")
    elif e6 == 'S23' and e1 == 'MPL':
        cursor.execute("ALTER TABLE labs23_mpl ADD COLUMN " + column_name + " INT(10)")
        print("heheheh")

    pass

    cursor.close()
    conn.close()



def sub2():
    day = entry2.get()
    mon = entry3.get()
    year = entry4.get()
    lec_no = entry7.get()
    column_name = "Date_" + day + "_" + mon + "_" + year + "_" + lec_no+""
    e1 = entry1.get()
    e5 = entry5.get()
    e6 = entry6.get()

    attendance_column = [1 if students_tree.item(item)['values'][4] == "PRESENT" else 0 for item in
                         students_tree.get_children()]
    conn = mysql.connector.connect(
        host=mysql_host,
        user=mysql_user,
        password=mysql_password,
        database=mysql_database
    )
    cursor = conn.cursor()

    if e5=='S2'and e1=='AT':
        # Assuming there's an 'id' column in your 'attendance' table
        for index, attendance in enumerate(attendance_column, start=71):
            insert_data_query = "UPDATE lect_s2at SET " + column_name + " = %s WHERE Roll_no = %s"
            cursor.execute(insert_data_query, (attendance, index))
            conn.commit()
        print("HEMLO")
    elif e5=='S2'and  e1=='OS':
        # Assuming there's an 'id' column in your 'attendance' table
        for index, attendance in enumerate(attendance_column, start=71):
            insert_data_query = "UPDATE lect_s2os SET " + column_name + " = %s WHERE Roll_no = %s"
            cursor.execute(insert_data_query, (attendance, index))
            conn.commit()
        print("HEMLO")
    elif e5=='S2'and  e1=='CN':
        # Assuming there's an 'id' column in your 'attendance' table
        for index, attendance in enumerate(attendance_column, start=71):
            insert_data_query = "UPDATE lect_s2cn SET " + column_name + " = %s WHERE Roll_no = %s"
            cursor.execute(insert_data_query, (attendance, index))
            conn.commit()
        print("HEMLO")
    elif e5=='S2'and  e1=='COA':
        # Assuming there's an 'id' column in your 'attendance' table
        for index, attendance in enumerate(attendance_column, start=71):
            insert_data_query = "UPDATE lect_s2coa SET " + column_name + " = %s WHERE Roll_no = %s"
            cursor.execute(insert_data_query, (attendance, index))
            conn.commit()
        print("HEMLO")
    elif e5=='S2'and  e1=='MATHS':
        # Assuming there's an 'id' column in your 'attendance' table
        for index, attendance in enumerate(attendance_column, start=71):
            insert_data_query = "UPDATE lect_s2am SET " + column_name + " = %s WHERE Roll_no = %s"
            cursor.execute(insert_data_query, (attendance, index))
            conn.commit()
        print("HEMLO")
    elif e6 == 'S21' and e1 =='PYTHON':
        # Assuming there's an 'id' column in your 'attendance' table
        for index, attendance in enumerate(attendance_column, start=71):
            insert_data_query = "UPDATE labs21_py SET " + column_name + " = %s WHERE Roll_no = %s"
            cursor.execute(insert_data_query, (attendance, index))
            conn.commit()
        print("heheheh")
    elif e6 == 'S21' and e1 == 'UNIX':
        # Assuming there's an 'id' column in your 'attendance' table
        for index, attendance in enumerate(attendance_column, start=71):
            insert_data_query = "UPDATE labs21_unix SET " + column_name + " = %s WHERE Roll_no = %s"
            cursor.execute(insert_data_query, (attendance, index))
            conn.commit()
        print("heheheh")
    elif e6 == 'S21' and e1 =='NL':
        # Assuming there's an 'id' column in your 'attendance' table
        for index, attendance in enumerate(attendance_column, start=71):
            insert_data_query = "UPDATE labs21_nl SET " + column_name + " = %s WHERE Roll_no = %s"
            cursor.execute(insert_data_query, (attendance, index))
            conn.commit()
        print("heheheh")
    elif e6 == 'S21' and e1 =='MPL':
        # Assuming there's an 'id' column in your 'attendance' table
        for index, attendance in enumerate(attendance_column, start=71):
            insert_data_query = "UPDATE labs21_mpl SET " + column_name + " = %s WHERE Roll_no = %s"
            cursor.execute(insert_data_query, (attendance, index))
            conn.commit()
        print("heheheh")
    elif e6 == 'S22' and e1 =='PYTHON':
        # Assuming there's an 'id' column in your 'attendance' table
        for index, attendance in enumerate(attendance_column, start=71):
            insert_data_query = "UPDATE labs22_py SET " + column_name + " = %s WHERE Roll_no = %s"
            cursor.execute(insert_data_query, (attendance, index))
            conn.commit()
        print("heheheh")
    elif e6 == 'S22' and e1 == 'UNIX':
        # Assuming there's an 'id' column in your 'attendance' table
        for index, attendance in enumerate(attendance_column, start=71):
            insert_data_query = "UPDATE labs22_unix SET " + column_name + " = %s WHERE Roll_no = %s"
            cursor.execute(insert_data_query, (attendance, index))
            conn.commit()
        print("heheheh")
    elif e6 == 'S22' and e1 =='NL':
        # Assuming there's an 'id' column in your 'attendance' table
        for index, attendance in enumerate(attendance_column, start=71):
            insert_data_query = "UPDATE labs22_nl SET " + column_name + " = %s WHERE Roll_no = %s"
            cursor.execute(insert_data_query, (attendance, index))
            conn.commit()
        print("heheheh")
    elif e6 == 'S22' and e1 =='MPL':
        # Assuming there's an 'id' column in your 'attendance' table
        for index, attendance in enumerate(attendance_column, start=71):
            insert_data_query = "UPDATE labs22_mpl SET " + column_name + " = %s WHERE Roll_no = %s"
            cursor.execute(insert_data_query, (attendance, index))
            conn.commit()
        print("heheheh")
    elif e6 == 'S23' and e1 == 'PYTHON':
        # Assuming there's an 'id' column in your 'attendance' table
        for index, attendance in enumerate(attendance_column, start=71):
            insert_data_query = "UPDATE labs23_py SET " + column_name + " = %s WHERE Roll_no = %s"
            cursor.execute(insert_data_query, (attendance, index))
            conn.commit()
        print("heheheh")
    elif e6 == 'S23' and e1 == 'UNIX':
        # Assuming there's an 'id' column in your 'attendance' table
        for index, attendance in enumerate(attendance_column, start=71):
            insert_data_query = "UPDATE labs23_unix SET " + column_name + " = %s WHERE Roll_no = %s"
            cursor.execute(insert_data_query, (attendance, index))
            conn.commit()
        print("heheheh")
    elif e6 == 'S23' and e1 == 'NL':
        # Assuming there's an 'id' column in your 'attendance' table
        for index, attendance in enumerate(attendance_column, start=71):
            insert_data_query = "UPDATE labs23_nl SET " + column_name + " = %s WHERE Roll_no = %s"
            cursor.execute(insert_data_query, (attendance, index))
            conn.commit()
        print("heheheh")
    elif e6 == 'S23' and e1 == 'MPL':
        # Assuming there's an 'id' column in your 'attendance' table
        for index, attendance in enumerate(attendance_column, start=71):
            insert_data_query = "UPDATE labs23_mpl SET " + column_name + " = %s WHERE Roll_no = %s"
            cursor.execute(insert_data_query, (attendance, index))
            conn.commit()
        print("heheheh")
# Close connection
    cursor.close()
    conn.close()

# Make sure to replace mysql_host, mysql_user, mysql_password, and mysql_database with your actual MySQL connection details.







def com_func():
    sub()
    fetch_students()

#//////////////////////////////////////////////////////////////////////////

# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 50)
  # You can adjust the value as needed

# Function to speak the given text
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# Function to wish the user based on the time
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")


# Function to take voice command and return string output
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query


# Function to send email
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('vmarri92@gmail.com', 'Vamshi@51124')
    server.sendmail('vmarri92@gmail.com', to, content)
    server.close()

def read():
    text=tf.get()
    speak(text)

def voice():
 if __name__ == "__main__":
    wishMe()

    while True:
        query = takeCommand().lower()

        if 'speak' in query:
            speak("FUCK OFF")

        elif 'read' in query:
            speak("the following roll numbers are marked absent")
            read()

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")


        elif 'email to' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "vmarri92@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send this email")

        elif 'good boy' in query:
            speak("thank you love you sir")

        elif 'jarvis fetch students'in query:
            speak("here's the list of syudent")
            fetch_students()

        elif 'jarvis confirm' in query:
            speak("as you say sir")
            sub2()


        elif 'jarvis sleep' in query:
            speak(" okk adios amigo..!")
            break


        else:
            print("No query matched")







fetch=CTkImage(light_image=Image.open("students.jpg"),dark_image=Image.open("students.jpg"),
                  size=(250,170))
flabel = CTkLabel(f1_2,text="",image=fetch,font=font)
flabel.place(relx=0.13,rely=0.1)
attendance=CTkImage(light_image=Image.open("attendance.jpg"),dark_image=Image.open("attendance.jpg"),
                  size=(250,250))
alabel = CTkLabel(f2,text="",image=attendance,font=font)
alabel.place(relx=0.35,rely=0.46)
per=CTkImage(light_image=Image.open("per.jpg"),dark_image=Image.open("per.jpg"),
                  size=(70,70))
plabel = CTkLabel(f2,text="",image=per,font=font)
plabel.place(relx=0.1,rely=0.18)
# Fetch button
fetch_button = customtkinter.CTkButton(f1_2, text="Fetch Students", command=fetch_students,fg_color='#0C2D57',width=343,height=40)
fetch_button.place(relx=0.03,rely=0.76)

voice_but = customtkinter.CTkButton(f2, text="VOICE",command=voice,fg_color='#0C2D57',width=200,height=40)
voice_but.place(relx=0.2,rely=0.23)
# vlabel = CTkLabel(f2,text="ENTER ROLL NO WITH A (,)COMMA",font=font)
# vlabel.place(relx=0.1,rely=0.03)
submit = customtkinter.CTkButton(f2, text="SUBMIT",command=sub2,fg_color='#0C2D57',width=540,height=40)
submit.place(relx=0.035,rely=0.9)
confirmation = customtkinter.CTkButton(f1_1,text="CONFIRM",command=sub,width=185,height=35,)
confirmation.place(relx=0.7,rely=0.77)
tf= customtkinter.CTkEntry(f2,placeholder_text="ENTER ROLL NO WITH COMMA ','...",height=50,width=500,font=font3)
tf.place(relx=0.05,rely=0.1)
# def work():
#     print(tf.get("0.0", "end"))
# button4= customtkinter.CTkButton(f2,text="butt",command=work )
# button4.place(relx=0.1,rely=0.6,)
# Bind double-click event to Treeview
students_tree.bind("<Double-1>", on_double_click)
tf.bind("<KeyRelease>",highlight_row)
tf.bind("<Return>", speak_text)  # Speak text when Enter key is pressed
# tf.bind("<FocusOut>", speak_text)
entry5.bind("<<ComboboxSelected>>", update_options)
entry0.bind("<<ComboboxSelected>>", update_options2)
# Bind events to show/hide placeholder text
entry6.bind("<FocusIn>", on_focus_in)
entry6.bind("<FocusOut>", on_focus_out)
# Bind events to show/hide placeholder text
entry0.bind("<FocusIn>", on_focus_in)
entry0.bind("<FocusOut>", on_focus_out)

# Bind events to show/hide placeholder text
entry5.bind("<FocusIn>", on_focus_in)
entry5.bind("<FocusOut>", on_focus_out)

# Bind events to show/hide placeholder text
entry1.bind("<FocusIn>", on_focus_in)
entry1.bind("<FocusOut>", on_focus_out)


students_tree.tag_configure('highlighted',background='red')

update_options()
update_options2()

app.mainloop()