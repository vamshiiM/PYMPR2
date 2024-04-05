import mysql.connector
import matplotlib.pyplot as plt
from email.message import EmailMessage
import smtplib
import ssl
import os

def send_email(subject, body, to_email, attachment_path, sender_email, sender_password):
    em = EmailMessage()
    em['From'] = sender_email
    em['To'] = to_email
    em['Subject'] = subject
    em.set_content(body)

    with open(attachment_path, 'rb') as attachment:
        em.add_attachment(attachment.read(), maintype='application', subtype='octet-stream', filename=os.path.basename(attachment_path))

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(sender_email, sender_password)
        smtp.send_message(em)

try:
    # Connect to the MySQL server
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Vamshi@51124',
        database='pympr'  # Specify your database name here
    )

    # Check if the connection is successful
    if conn.is_connected():
        print("Connection established...")

        # Create a cursor object
        cursor = conn.cursor()

        # Execute a query to retrieve data including recipient email addresses
        cursor.execute("SELECT subject, attendance_percentage, email FROM student_bargraph")

        # Fetch all rows
        rows = cursor.fetchall()

        # Process the retrieved data
        subjects = []
        attendance_percentages = []
        for row in rows:
            subjects.append(row[0])
            attendance_percentages.append(row[1])

        # Plot the data as a bar graph
        plt.bar(subjects, attendance_percentages)
        plt.xlabel('Subject')
        plt.ylabel('Attendance Percentage')
        plt.title('Bar Graph of Student Attendance')
        plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility
        plt.tight_layout()  # Adjust layout to prevent clipping of labels

        # Save the plot as an image
        image_path = 'student_attendance_graph.png'
        plt.savefig(image_path)

        # Close cursor and connection
        cursor.close()
        conn.close()

        # Send email to each recipient with the full bar graph as attachment
        for row in rows:
            subject = row[0]
            recipient_email = row[2]

            # Check if recipient email exists
            if recipient_email:
                send_email("Student Attendance Bar Graph", "Please find the attached attendance graph.",
                           recipient_email, image_path,
                           'simranyelave1@gmail.com', 'febw orfn mivn bbhd')
                print("Email sent successfully to:", recipient_email)

    else:
        print("Connection failed...")

except mysql.connector.Error as e:
    print("Error connecting to MySQL:", e)
except Exception as e:
    print("An error occurred:", e)

