import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import customtkinter
# Function to create and display the bar graph
import mysql.connector
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from customtkinter import *
from PIL import Image, ImageTk
import subprocess
from subprocess import call

# Create a Tkinter window
root = customtkinter.CTk()
root.title("Bar Graph of student attendance")
root.geometry("1530x790+0+0")
root.configure(fg_color='#33186B')
frame=customtkinter.CTkFrame(root,width=650,height=700,fg_color='#7360DF')
frame.place(relx=0.18,rely=0.05)
frame2=customtkinter.CTkFrame(root,width=300,height=380,fg_color='#7360DF')
frame2.place(relx=0.63,rely=0.05)
frame3=customtkinter.CTkFrame(root,width=300,height=296,fg_color='#7360DF')
frame3.place(relx=0.63,rely=0.56)

frame4=customtkinter.CTkFrame(frame,width=570,height=570)
frame4.place(relx=0.073,rely=0.09)
roll = CTkEntry(frame2,width=248,height=50,placeholder_text='ENTER ROLL NO.....')
roll.place(relx=0.08,rely=0.7)






# Check if the connection is successful
def r1():
    # Connect to the MySQL server
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Vamshi@51124',
        database='pympr'  # Specify your database name here
    )

    # Create a cursor object
    cursor = conn.cursor()

    # Execute a query to retrieve data
    cursor.execute("SELECT subject, attendance_percentage FROM student_bargraph")

    # Fetch all rows
    rows = cursor.fetchall()

    # Process the retrieved data
    subject = []
    attendance_precentage = []
    for row in rows:
        subject.append(row[0])
        attendance_precentage.append(row[1])

    # Close cursor and connection
    cursor.close()
    conn.close()

    # Create a figure and axis for the bar plot
    fig, ax = plt.subplots()

    # Define colors for bars based on attendance percentage
    colors = ['red' if percentage < 60 else 'green' for percentage in attendance_precentage]

    # Plot the data as a bar graph with specified colors
    ax.bar(subject, attendance_precentage, color=colors)

    # Customize the plot
    ax.set_ylim(0, 100)

    ax.set_xlabel('Subject')
    ax.set_ylabel('Attendance Percentage')
    ax.set_title('ATTENDANCE of 75')
    ax.tick_params(axis='x', rotation=45)  # Rotate x-axis labels for better visibility

    # Create a Tkinter canvas
    canvas = FigureCanvasTkAgg(fig, master=frame4)
    canvas.draw()
    canvas.get_tk_widget().place(relx=0.045,rely=0.045)


def r2():
    # Connect to the MySQL server
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Vamshi@51124',
        database='pympr'  # Specify your database name here
    )
    cursor = conn.cursor()

    # Execute a query to retrieve data
    cursor.execute("SELECT subject, attendance_percentage FROM student2_bargraph")

    # Fetch all rows
    rows = cursor.fetchall()

    # Process the retrieved data
    subject = []
    attendance_precentage = []
    for row in rows:
        subject.append(row[0])
        attendance_precentage.append(row[1])

    # Close cursor and connection
    cursor.close()
    conn.close()

    # Create a figure and axis for the bar plot
    fig, ax = plt.subplots()
    colors = ['red' if percentage < 60 else 'green' for percentage in attendance_precentage]

    # Plot the data as a bar graph with specified colors
    ax.bar(subject, attendance_precentage, color=colors)
    ax.set_ylim(0, 100)
    ax.set_xlabel('subject')
    ax.set_ylabel('attendance_precentage')
    ax.set_title('ATTENDANCE of 76')
    ax.tick_params(axis='x', rotation=45)  # Rotate x-axis labels for better visibility

    # Create a Tkinter canvas
    canvas = FigureCanvasTkAgg(fig, master=frame4)
    canvas.draw()
    canvas.get_tk_widget().place(relx=0.045,rely=0.045)

def r3():
    # Connect to the MySQL server
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Vamshi@51124',
        database='pympr'  # Specify your database name here
    )
    cursor = conn.cursor()

    # Execute a query to retrieve data
    cursor.execute("SELECT subject, attendance_percentage FROM student3_bargraph")

    # Fetch all rows
    rows = cursor.fetchall()

    # Process the retrieved data
    subject = []
    attendance_precentage = []
    for row in rows:
        subject.append(row[0])
        attendance_precentage.append(row[1])

    # Close cursor and connection
    cursor.close()
    conn.close()

    # Create a figure and axis for the bar plot
    fig, ax = plt.subplots()
    colors = ['red' if percentage < 60 else 'green' for percentage in attendance_precentage]

    # Plot the data as a bar graph with specified colors
    ax.bar(subject, attendance_precentage, color=colors)
    ax.set_ylim(0, 100)
    ax.set_xlabel('subject')
    ax.set_ylabel('attendance_precentage')
    ax.set_title('ATTENDANCE of 77')
    ax.tick_params(axis='x', rotation=45)  # Rotate x-axis labels for better visibility

    # Create a Tkinter canvas
    canvas = FigureCanvasTkAgg(fig, master=frame4)
    canvas.draw()
    canvas.get_tk_widget().place(relx=0.045,rely=0.045)

def r4():
    # Connect to the MySQL server
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Vamshi@51124',
        database='pympr'  # Specify your database name here
    )
    cursor = conn.cursor()

    # Execute a query to retrieve data
    cursor.execute("SELECT subject, attendance_percentage FROM student4_bargraph")

    # Fetch all rows
    rows = cursor.fetchall()

    # Process the retrieved data
    subject = []
    attendance_precentage = []
    for row in rows:
        subject.append(row[0])
        attendance_precentage.append(row[1])

    # Close cursor and connection
    cursor.close()
    conn.close()

    # Create a figure and axis for the bar plot
    fig, ax = plt.subplots()
    colors = ['red' if percentage < 60 else 'green' for percentage in attendance_precentage]

    # Plot the data as a bar graph with specified colors
    ax.bar(subject, attendance_precentage, color=colors)
    ax.set_ylim(0, 100)
    ax.set_xlabel('subject')
    ax.set_ylabel('attendance_precentage')
    ax.set_title('ATTENDANCE of 78')
    ax.tick_params(axis='x', rotation=45)  # Rotate x-axis labels for better visibility

    # Create a Tkinter canvas
    canvas = FigureCanvasTkAgg(fig, master=frame4)
    canvas.draw()
    canvas.get_tk_widget().place(relx=0.045,rely=0.045)

def r5():
    # Connect to the MySQL server
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Vamshi@51124',
        database='pympr'  # Specify your database name here
    )
    cursor = conn.cursor()

    # Execute a query to retrieve data
    cursor.execute("SELECT subject, attendance_percentage FROM student5_bargraph")

    # Fetch all rows
    rows = cursor.fetchall()

    # Process the retrieved data
    subject = []
    attendance_precentage = []
    for row in rows:
        subject.append(row[0])
        attendance_precentage.append(row[1])

    # Close cursor and connection
    cursor.close()
    conn.close()

    # Create a figure and axis for the bar plot
    fig, ax = plt.subplots()
    colors = ['red' if percentage < 60 else 'green' for percentage in attendance_precentage]

    # Plot the data as a bar graph with specified colors
    ax.bar(subject, attendance_precentage, color=colors)
    ax.set_ylim(0, 100)
    ax.set_xlabel('subject')
    ax.set_ylabel('attendance_precentage')
    ax.set_title('ATTENDANCE of 79')
    ax.tick_params(axis='x', rotation=45)  # Rotate x-axis labels for better visibility

    # Create a Tkinter canvas
    canvas = FigureCanvasTkAgg(fig, master=frame4)
    canvas.draw()
    canvas.get_tk_widget().place(relx=0.045,rely=0.045)



def select():
    call(["python", "gmail.py"])

def choose():
    e1=roll.get()

    if e1=='75' :
        r1()
        print("FUCK")
        e1.delete(0, tk.END)
    elif e1=='76' :
        r2()
        print("button clicked")
        e1.delete(0, tk.END)
    elif e1 == '77':
        r3()
        print("button clicked")
        e1.delete(0, tk.END)
    elif e1 == '78':
        r4()
        print("button clicked")
        e1.delete(0, tk.END)
    elif e1 == '79':
        r5()
        print("button clicked")
        e1.delete(0, tk.END)


my_image=CTkImage(light_image=Image.open("pie1.jpg"),dark_image=Image.open("pie1.jpg"),
                  size=(270,270))
label = CTkLabel(frame3,text="",image=my_image)
label.place(relx=0.05,rely=0.05)


my_image2=CTkImage(light_image=Image.open("think.jpg"),dark_image=Image.open("think.jpg"),
                  size=(300,200))
label2 = CTkLabel(frame2,text="",image=my_image2)
label2.place(relx=-0.02,rely=0.1)





button=CTkButton(frame2,text='SUBMIT',width=248,height=40,command=choose)
button.place(relx=0.08,rely=0.85)

button1=CTkButton(frame4,text='SEND EMAIL',width=548,height=50,command=select)
button1.place(relx=0.02,rely=0.85)
root.mainloop()
