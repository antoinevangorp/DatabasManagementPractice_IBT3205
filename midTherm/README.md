# MidTherm

This Python script is used to create and initialize a SQLite database named 'ITS.db'. It defines the structure of multiple tables related to an Information Technology Services (ITS) database schema and inserts sample data into those tables. Here's a detailed breakdown of what this script does:

### Database Connection

```python
import sqlite3

# Create a SQLite database or connect to an existing one
conn = sqlite3.connect('ITS.db')
cur = conn.cursor()
```

This part establishes a connection to the SQLite database named 'ITS.db' and creates a cursor object for executing SQL commands.

### Table Creation

SQL statements for creating tables are defined, such as 'DEPARTMENT', 'DEPENDENT', 'EMPLOYEE', 'Vehicles', etc. The `CREATE TABLE IF NOT EXISTS` statement ensures that the tables are created only if they don't already exist.

### Execute Table Creation SQL Statements

```python
# Execute the table creation SQL statements
cur.execute(create_department_sql)
cur.execute(create_department_locations_sql)
cur.execute(create_dependent_sql)
cur.execute(create_drivers_assignments_sql)
cur.execute(create_employee_sql)
cur.execute(create_locations_sql)
cur.execute(create_transportations_assignments_sql)
cur.execute(create_vehicles_sql)
cur.execute(create_vehicles_assignments_sql)
```

These lines execute the SQL statements to create the tables in the database.

### Data Insertion

Sample data for each table is defined in SQL insert statements. For example, sample data for the 'DEPARTEMENT' table is defined as follows:

```python
# Sample data for "DEPARTEMENT" table
insert_department_data = '''
INSERT INTO "DEPARTEMENT" (dnumber, dname, mgrssn)
VALUES (1, 101, 123456789),
       (2, 102, 987654321);
'''
```

### Execute Data Insertion SQL Statements

```python
# Execute the data insertion SQL statements
cur.execute(insert_department_data)
cur.execute(insert_department_locations_data)
cur.execute(insert_dependent_data)
cur.execute(insert_drivers_assignments_data)
cur.execute(insert_employee_data)
cur.execute(insert_locations_data)
cur.execute(insert_transportations_assignments_data)
cur.execute(insert_vehicles_data)
cur.execute(insert_vehicles_assignments_data)
```

These lines execute the SQL statements to insert data into the tables.

### Commit the Changes

```python
# Commit the changes
conn.commit()
```

This commits the changes made to the database, making them permanent.

### Display Table Contents

A function `print_table_contents(table_name)` is defined to print the contents of each table. It executes a SELECT statement for each table and prints the retrieved rows.

### Print the Contents of Each Table

```python
# Print the contents of each table
print_table_contents('DEPARTEMENT')
print_table_contents('DEPARTMENT_LOCATIONS')
print_table_contents('DriversAssignments')
print_table_contents('EMPLOYEE')
print_table_contents('LOCATIONS')
print_table_contents('TransportationsAssignments')
print_table_contents('Vehicles')
print_table_contents('VehiclesAssignments')
```

These lines print the contents of each table by calling the `print_table_contents` function.

### Closing Database Connection

```python
# Close the cursor and connection
cur.close()
conn.close()
```

Finally, the script closes the cursor and the database connection.

This script can be used as a template for creating and initializing a SQLite database for an ITS database system. It also provides a demonstration of how to create tables, insert data, and query the database. You can customize it by adding more tables or modifying the sample data to match your specific requirements.
