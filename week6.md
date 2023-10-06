# SQLite Database Initialization and Data Insertion

This Python script is used to create and initialize a SQLite database named 'company.db'. It defines the structure of multiple tables related to a hypothetical company's database schema and inserts sample data into those tables. Here's a detailed breakdown of what this script does:

### Database Connection

```python
import sqlite3

# Create a SQLite database or connect to an existing one
conn = sqlite3.connect('company.db')
cur = conn.cursor()
```

This part establishes a connection to the SQLite database named 'company.db' and creates a cursor object for executing SQL commands.

### Table Creation

```python
# SQL statements for table creation
create_department_sql = '''
CREATE TABLE IF NOT EXISTS "DEPARTMENT"(
  dnumber INTEGER PRIMARY KEY NOT NULL,
  dname INTEGER,
  mgrssn INTEGER NOT NULL
);
'''
# ... (similar create statements for other tables)
```

Here, SQL statements are defined for creating tables such as 'DEPARTMENT', 'DEPENDENT', 'EMPLOYEE', etc. The `CREATE TABLE IF NOT EXISTS` statement ensures that the tables are created only if they don't already exist.

### Execute Table Creation SQL Statements

```python
# Execute the table creation SQL statements
cur.execute(create_department_sql)
cur.execute(create_department_locations_sql)
cur.execute(create_dependent_sql)
# ... (similar execution for other tables)
```

These lines execute the SQL statements to create the tables in the database.

### Data Insertion

```python
# Insert sample data into the tables
insert_department_data = '''
INSERT INTO "DEPARTEMENT" (dnumber, dname, mgrssn)
VALUES (1, 101, 123456789),
       (2, 102, 987654321);
'''
# ... (similar insert statements for other tables)
```

Data insertion SQL statements are defined for each table to insert sample data into them.

### Execute Data Insertion SQL Statements

```python
# Execute the data insertion SQL statements
cur.execute(insert_department_data)
cur.execute(insert_department_locations_data)
cur.execute(insert_dependent_data)
# ... (similar execution for other tables)
```

These lines execute the SQL statements to insert data into the tables.

### Commit the Changes

```python
# Commit the changes
conn.commit()
```

This commits the changes made to the database, making them permanent.

### Display Table Contents

```python
# Print the contents of the database
print("Contents of the 'DEPARTEMENT' table:")
cur.execute("SELECT * FROM 'DEPARTEMENT'")
print(cur.fetchall())

# ... (similar print statements for other tables)
```

These lines execute SQL SELECT statements to retrieve and print the contents of each table in the database.

### Closing Database Connection

```python
# Close the cursor and connection
cur.close()
conn.close()
```

Finally, the script closes the cursor and the database connection.

This script can be used as a template for creating and initializing a SQLite database for a company's data. It also provides a demonstration of how to create tables, insert data, and query the database. You can customize it by adding more tables or modifying the sample data to match your specific requirements.
