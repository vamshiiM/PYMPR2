import mysql.connector
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

# Connect to the MySQL server
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Vamshi@51124',
    database='pympr'  # Specify your database name here
)

# Create a Tkinter window
root = tk.Tk()
root.title("Bar Graph of student attendance")

# Check if the connection is successful
if conn.is_connected():
    print("Connection established...")

    # Create a cursor object
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

    # Plot the data as a bar graph
    ax.bar(subject, attendance_precentage)
    ax.set_xlabel('subject')
    ax.set_ylabel('attendance_precentage')
    ax.set_title('Bar Graph of student attendance')
    ax.tick_params(axis='x', rotation=45)  # Rotate x-axis labels for better visibility

    # Create a Tkinter canvas
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()

    # Display the Tkinter window
    root.mainloop()

else:
    print("Connection failed...")
