import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Vamshi@51124",
    database="pympr"
)

# Create a cursor object
cursor = conn.cursor()

# Query information schema to get table names
cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'pympr'")

# Fetch all table names
table_names = [row[0] for row in cursor.fetchall()]

# Iterate over table names
for table_name in table_names:
    print("Table:", table_name)

    # Query information schema to get column names for the current table
    cursor.execute(f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{s21}'")

    # Fetch all column names
    column_names = [row[0] for row in cursor.fetchall()]

    # Exclude the first column (assuming it's the primary key)
    column_names = column_names[1:]

    # Print column names
    print("Column Names:", column_names)
    print()  # Add a newline for readability

# Close cursor and connection
cursor.close()
conn.close()
