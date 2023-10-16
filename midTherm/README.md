# MidTherm

This Python script is used to create and initialize a SQLite database named [ITS_Database](./db_doc.md). It defines the structure of multiple tables related to an Information Technology Services (ITS) database schema and inserts sample data into those tables. Here's a detailed breakdown of what this script does:

### Database Connection

```python
import sqlite3

# Create a SQLite database or connect to an existing one
conn = sqlite3.connect('ITS_Database.db')
cur = conn.cursor()
```

This part establishes a connection to the SQLite database named 'ITS_Database.db' and creates a cursor object for executing SQL commands.

### Table Creation

SQL statements for creating tables are defined, such as 'Vehicles', 'MaintenanceRepairs', 'Countries', 'GameOfficials', 'Drivers', etc. The `CREATE TABLE IF NOT EXISTS` statement ensures that the tables are created only if they don't already exist.

### Execute Table Creation SQL Statements

```python
# Execute the table creation SQL statements
cur.execute(create_vehicles_sql)
cur.execute(create_maintenance_repairs_sql)
cur.execute(create_countries_sql)
cur.execute(create_spoken_languages_sql)
cur.execute(create_game_officials_sql)
cur.execute(create_drivers_sql)
cur.execute(create_driver_bookings_sql)
cur.execute(create_vehicle_availability_sql)
```

These lines execute the SQL statements to create the tables in the database.

### Data Insertion

Sample data for each table is defined in SQL insert statements. For example, sample data for the 'Vehicles' table is defined as follows:

```python
# Sample data for "Vehicles" table
sample_vehicle_data = '''
INSERT INTO Vehicles (VehicleID, RegistrationID, Manufacturer, Model, Color, CurrentOdometer, PassengerCapacity)
VALUES ('V1000', '2001 ABC', 'Volvo', 'XC90 SE', 'Silver', 4350, 4),
       ('V1001', '2006 AFD', 'Kia', 'K7', 'Black', 2195, 4),
       ('V1002', '2021 AHR', 'Tesla', '2020 F', 'White', 509, 4),
       ('V1003', '2020 DXF', 'Ford', 'Transit', 'Silver', 974, 2);
'''
```

### Execute Data Insertion SQL Statements

```python
# Execute the sample data insertion SQL statements
cur.execute(sample_vehicle_data)
cur.execute(sample_countries_data)
cur.execute(sample_languages_data)
cur.execute(sample_officials_data)
cur.execute(sample_drivers_data)
cur.execute(sample_booking_data)
cur.execute(sample_availability_data)
cur.execute(sample_maintenance_repairs_data)
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
print_table_contents('Vehicles')
print_table_contents('MaintenanceRepairs')
print_table_contents('Countries')
print_table_contents('SpokenLanguages')
print_table_contents('GameOfficials')
print_table_contents('Drivers')
print_table_contents('DriverBookings')
print_table_contents('VehicleAvailability')
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