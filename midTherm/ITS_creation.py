import sqlite3

# Create a SQLite database or connect to an existing one
conn = sqlite3.connect('ITS.db')
cur = conn.cursor()

# SQL statements for table creation

# Create "DEPARTEMENT" table
create_department_sql = '''
CREATE TABLE IF NOT EXISTS "DEPARTEMENT"(
  dnumber INTEGER PRIMARY KEY NOT NULL,
  dname INTEGER,
  mgrssn INTEGER NOT NULL
);
'''

# Create "DEPARTMENT_LOCATIONS" table
create_department_locations_sql = '''
CREATE TABLE IF NOT EXISTS "DEPARTMENT_LOCATIONS"(
  dnumber INTEGER NOT NULL,
  "LOCATIONS_dlocation" INTEGER NOT NULL
);
'''

# Create "DEPENDENT" table
create_dependent_sql = '''
CREATE TABLE IF NOT EXISTS "DEPENDENT"(
  dependentname TEXT PRIMARY KEY NOT NULL,
  essn INTEGER NOT NULL,
  sex CHAR,
  bdate TIMESTAMP,
  relationship TEXT
);
'''

# Create "DriversAssignments" table
create_drivers_assignments_sql = '''
CREATE TABLE IF NOT EXISTS "DriversAssignments"(
  "AssignmentID" INTEGER PRIMARY KEY NOT NULL,
  "AssignmentData" DATE,
  "EMPLOYEE_ssn" INTEGER NOT NULL,
  "Vehicles_VehicleID" INTEGER NOT NULL
);
'''

# Create "EMPLOYEE" table
create_employee_sql = '''
CREATE TABLE IF NOT EXISTS "EMPLOYEE"(
  ssn INTEGER PRIMARY KEY NOT NULL,
  "superssn (FK)" INTEGER NOT NULL,
  fname TEXT,
  minit INTEGER,
  lname TEXT,
  address TEXT,
  bdate TIMESTAMP,
  salary REAL,
  sex CHAR,
  dno INTEGER NOT NULL
);
'''

# Create "LOCATIONS" table
create_locations_sql = '''
CREATE TABLE IF NOT EXISTS "LOCATIONS"(
  dlocation INTEGER PRIMARY KEY NOT NULL
);
'''

# Create "TransportationsAssignments" table
create_transportations_assignments_sql = '''
CREATE TABLE IF NOT EXISTS "TransportationsAssignments"(
  "AssignmentID" INTEGER PRIMARY KEY NOT NULL,
  "LocationDepart" INTEGER NOT NULL,
  "LocationEnd" INTEGER NOT NULL
);
'''

# Create "Vehicles" table
create_vehicles_sql = '''
CREATE TABLE IF NOT EXISTS "Vehicles"(
  "VehicleID" INTEGER PRIMARY KEY NOT NULL,
  "CurentLocation" INTEGER,
  "LicensePlate" TEXT NOT NULL
);
'''

# Create "VehiclesAssignments" table
create_vehicles_assignments_sql = '''
CREATE TABLE IF NOT EXISTS "VehiclesAssignments"(
  "AssignmentID" INTEGER PRIMARY KEY NOT NULL,
  "AssignmentData" DATE,
  "ServicID" INTEGER NOT NULL,
  "Vehicles_VehicleID" INTEGER NOT NULL
);
'''

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

# Insert sample data into the tables

# Sample data for "DEPARTEMENT" table
insert_department_data = '''
INSERT INTO "DEPARTEMENT" (dnumber, dname, mgrssn)
VALUES (1, 101, 123456789),
       (2, 102, 987654321);
'''

# Sample data for "DEPARTMENT_LOCATIONS" table
insert_department_locations_data = '''
INSERT INTO "DEPARTMENT_LOCATIONS" (dnumber, "LOCATIONS_dlocation")
VALUES (1, 1),
       (2, 2);
'''

# Sample data for "DEPENDENT" table
insert_dependent_data = '''
INSERT INTO "DEPENDENT" (dependentname, essn, sex, bdate, relationship)
VALUES ('John Doe', 123456789, 'M', '1990-01-15', 'Child'),
       ('Jane Note', 987654321, 'F', '1992-05-20', 'Spouse');
'''

# Sample data for "DriversAssignments" table
insert_drivers_assignments_data = '''
INSERT INTO "DriversAssignments" ("AssignmentID", "AssignmentData", "EMPLOYEE_ssn", "Vehicles_VehicleID")
VALUES (1, '2023-10-01', 123456789, 1),
       (2, '2023-10-02', 987654321, 2);
'''

# Sample data for "EMPLOYEE" table
insert_employee_data = '''
INSERT INTO "EMPLOYEE" (ssn, "superssn (FK)", fname, minit, lname, address, bdate, salary, sex, dno)
VALUES (123456789, NULL, 'Alice',  'M', 'Smith', '123 Main St', '1980-03-10', 50000.00, 'F', 1),
       (987654321, 123456789, 'Bob',  'A', 'Johnson', '456 Oak St', '1975-12-05', 60000.00, 'M', 2);
'''

# Sample data for "LOCATIONS" table
insert_locations_data = '''
INSERT INTO "LOCATIONS" (dlocation)
VALUES (1),
       (2);
'''

# Sample data for "TransportationsAssignments" table
insert_transportations_assignments_data = '''
INSERT INTO "TransportationsAssignments" ("AssignmentID", "LocationDepart", "LocationEnd")
VALUES (1, 1, 2),
       (2, 2, 1);
'''

# Sample data for "Vehicles" table
insert_vehicles_data = '''
INSERT INTO "Vehicles" ("VehicleID", "CurentLocation", "LicensePlate")
VALUES (1, 1, 'ABC123'),
       (2, 2, 'XYZ789');
'''

# Sample data for "VehiclesAssignments" table
insert_vehicles_assignments_data = '''
INSERT INTO "VehiclesAssignments" ("AssignmentID", "AssignmentData", "ServicID", "Vehicles_VehicleID")
VALUES (1, '2023-10-01', 1, 1),
       (2, '2023-10-02', 2, 2);
'''

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

# Commit the changes
conn.commit()

# Print the contents of the database

# Function to print the contents of a table
def print_table_contents(table_name):
    print(f"Contents of the '{table_name}' table:")
    cur.execute(f"SELECT * FROM '{table_name}'")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    print("")

# Print the contents of each table
print_table_contents('DEPARTEMENT')
print_table_contents('DEPARTMENT_LOCATIONS')
print_table_contents('DriversAssignments')
print_table_contents('EMPLOYEE')
print_table_contents('LOCATIONS')
print_table_contents('TransportationsAssignments')
print_table_contents('Vehicles')
print_table_contents('VehiclesAssignments')

# Close the cursor and connection
cur.close()
conn.close()
