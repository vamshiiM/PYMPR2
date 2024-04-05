import mysql.connector
import reportlab
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Vamshi@51124",
    database="pympr"
)

# Create a cursor object to execute queries
cursor = conn.cursor()

# Execute a SELECT query to fetch attendance records
cursor.execute("SELECT * FROM S2")

# Fetch all records
attendance_records = cursor.fetchall()

# Close the cursor and database connection
cursor.close()
conn.close()

# Generate PDF
pdf_filename = "attendance_records.pdf"
doc = SimpleDocTemplate(pdf_filename, pagesize=letter)
table_data = [['Roll_no', 'Name', 'Batch']]

# Populate table data with fetched records
for record in attendance_records:
    table_data.append([record[0], record[1], record[2]])

# Create table object
table = Table(table_data)

# Add style to table
style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.gray),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                    ('GRID', (0, 0), (-1, -1), 1, colors.black)])
table.setStyle(style)

# Add table to the PDF document
doc.build([table])

print(f"PDF generated successfully: {pdf_filename}")